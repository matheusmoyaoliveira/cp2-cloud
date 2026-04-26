import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


@app.route("/")
def home():
    return jsonify({
        "mensagem": "API de Clientes - CP2 Cloud Computing",
        "endpoints": {
            "listar_clientes": "GET /clientes",
            "buscar_cliente": "GET /clientes/<id>",
            "criar_cliente": "POST /clientes",
            "atualizar_cliente": "PUT /clientes/<id>",
            "deletar_cliente": "DELETE /clientes/<id>"
        }
    })


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, nome, email, telefone, criado_em
        FROM clientes
        ORDER BY id;
    """)

    clientes = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {
            "id": cliente[0],
            "nome": cliente[1],
            "email": cliente[2],
            "telefone": cliente[3],
            "criado_em": cliente[4].strftime("%Y-%m-%d %H:%M:%S")
        }
        for cliente in clientes
    ])


@app.route("/clientes/<int:id>", methods=["GET"])
def buscar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, nome, email, telefone, criado_em
        FROM clientes
        WHERE id = %s;
    """, (id,))

    cliente = cur.fetchone()

    cur.close()
    conn.close()

    if cliente is None:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify({
        "id": cliente[0],
        "nome": cliente[1],
        "email": cliente[2],
        "telefone": cliente[3],
        "criado_em": cliente[4].strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/clientes", methods=["POST"])
def criar_cliente():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO clientes (nome, email, telefone)
        VALUES (%s, %s, %s)
        RETURNING id, nome, email, telefone, criado_em;
    """, (nome, email, telefone))

    novo_cliente = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "id": novo_cliente[0],
        "nome": novo_cliente[1],
        "email": novo_cliente[2],
        "telefone": novo_cliente[3],
        "criado_em": novo_cliente[4].strftime("%Y-%m-%d %H:%M:%S")
    }), 201


@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE clientes
        SET nome = %s, email = %s, telefone = %s
        WHERE id = %s
        RETURNING id, nome, email, telefone, criado_em;
    """, (nome, email, telefone, id))

    cliente_atualizado = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    if cliente_atualizado is None:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify({
        "id": cliente_atualizado[0],
        "nome": cliente_atualizado[1],
        "email": cliente_atualizado[2],
        "telefone": cliente_atualizado[3],
        "criado_em": cliente_atualizado[4].strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM clientes
        WHERE id = %s
        RETURNING id;
    """, (id,))

    cliente_deletado = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    if cliente_deletado is None:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify({
        "mensagem": f"Cliente com ID {id} deletado com sucesso"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)