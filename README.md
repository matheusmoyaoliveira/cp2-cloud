# CP2 Cloud Computing - API de Clientes com Docker

## Integrantes
- Matheus Moya de Oliveira — RM562822
- Ana Carolina Pereira Fontes — RM562145

---

## Descrição
Projeto desenvolvido para validar migração de ambiente para containers Docker utilizando dois containers integrados em rede:

- Container Flask API
- Container PostgreSQL

Implementação de CRUD completo da entidade clientes.

---

## Arquitetura

App Container:
- Python Flask

Database Container:
- PostgreSQL

Recursos Docker:
- Network dedicada
- Volume nomeado
- Variáveis de ambiente
- Containers em segundo plano

---

## Estrutura

```text
app/
db/
docker-compose.yml
README.md
```

---

## Subir projeto

```bash
docker compose up -d --build
```

Verificar:

```bash
docker compose ps
```

---

## Testar API

Listar clientes:

```http
GET http://localhost:5000/clientes
```

Criar:

```http
POST /clientes
```

```json
{
 "nome":"Carlos",
 "email":"carlos@email.com",
 "telefone":"11999999999"
}
```

Atualizar:

```http
PUT /clientes/3
```

Excluir:

```http
DELETE /clientes/3
```

---

## Consultar banco

```bash
docker exec -it rm562822_rm562145_db_clientes psql -U cp2_user -d cp2_cloud
```

```sql
SELECT * FROM clientes;
```

---

## Derrubar ambiente

```bash
docker compose down
```

Com volumes:

```bash
docker compose down -v
```