# CP2 Cloud Computing - API de Clientes com Docker

## Integrantes

- Matheus Moya de Oliveira — RM562822
- Ana Carolina Pereira Fontes — RM562145

---

# Descrição do Projeto

Projeto desenvolvido para o Checkpoint 2 da disciplina **DevOps Tools & Cloud Computing**, com objetivo de validar a migração de ambiente para containers Docker utilizando múltiplos containers integrados em rede.

A solução implementa:

- API REST em Python com Flask
- Banco de Dados PostgreSQL
- CRUD completo da entidade clientes
- Comunicação entre containers em rede Docker
- Persistência com volume nomeado
- Variáveis de ambiente
- Containers em segundo plano
- Execução via Docker Compose

---

# Arquitetura da Solução

## Containers

### Container 1 — API

- Nome:

```text
rm562822_rm562145_api_clientes
```

Responsável por:

- Expor endpoints REST
- Executar operações CRUD
- Conectar com banco PostgreSQL

Porta:

```text
5000
```

---

## Container 2 — Banco de Dados

- Nome:

```text
rm562822_rm562145_db_clientes
```

Banco:

```text
PostgreSQL 16
```

Porta:

```text
5432
```

Persistência:

```text
rm562822_rm562145_postgres_data
```

---

## Rede Docker

```text
rm562822_rm562145_network
```

Containers comunicam-se internamente via rede bridge Docker.

---

# Estrutura do Projeto

```text
CP2-CLOUD/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── db/
│   └── init.sql
│
├── evidencias/
├── create-docker-objects.bat
├── create-docker-objects.sh
├── scripts-docker.md
└── README.md
```

---

# Tecnologias Utilizadas

- Python 3.12
- Flask
- PostgreSQL
- Docker
- Docker Compose

---

# Pré-Requisitos

Instalar:

- Docker Desktop
- Git
- Insomnia ou Postman (para testes)

Verificar:

```bash
docker --version
docker compose version
```

---

# Como Executar o Projeto

## Clonar repositório

```bash
git clone <url-do-repositorio>
cd CP2-CLOUD
```

---

## Subir ambiente

```bash
docker compose up -d --build
```

---

## Verificar containers

```bash
docker compose ps
```

ou

```bash
docker ps --filter "name=rm562822_rm562145"
```

---

# Endpoints da API

## Listar clientes

```http
GET http://localhost:5000/clientes
```

---

## Buscar cliente por ID

```http
GET http://localhost:5000/clientes/1
```

---

## Criar cliente

```http
POST http://localhost:5000/clientes
```

Body:

```json
{
 "nome":"Carlos Silva",
 "email":"carlos@email.com",
 "telefone":"11999999999"
}
```

---

## Atualizar cliente

```http
PUT http://localhost:5000/clientes/1
```

```json
{
 "nome":"Carlos Atualizado",
 "email":"carlos@email.com",
 "telefone":"11911110000"
}
```

---

## Deletar cliente

```http
DELETE http://localhost:5000/clientes/1
```

---

# Validar no Banco de Dados

Entrar no container:

```bash
docker exec -it rm562822_rm562145_db_clientes psql -U cp2_user -d cp2_cloud
```

Consultar:

```sql
SELECT * FROM clientes;
```

---

# Objetos Docker Criados

## Containers

```bash
docker ps
```

## Imagens

```bash
docker image ls
```

## Volumes

```bash
docker volume ls
```

## Redes

```bash
docker network ls
```

---

# Scripts Manuais dos Objetos Docker

Além do Docker Compose, os scripts manuais dos objetos Docker encontram-se em:

```text
scripts-docker.md
```

Contém:

- docker network create
- docker volume create
- docker run containers
- build da imagem
- comandos de verificação

Atende ao requisito de scripts para criação dos objetos Docker.

---

# Derrubar Ambiente

Parar containers:

```bash
docker compose down
```

Remover incluindo volume:

```bash
docker compose down -v
```

---

# Evidências do Projeto

Na pasta:

```text
evidencias/
```

Contém:

- docker-compose-ps
- docker-ps
- docker-image-ls
- docker-volume-ls
- docker-network-ls
- evidências CRUD

---

# Requisitos do Checkpoint Atendidos

## Regras

- Dois containers interagindo em rede Docker
- Um container de banco de dados
- Volume nomeado para persistência
- Containers com portas expostas
- Variáveis de ambiente
- Containers em segundo plano
- Containers com RM no nome

## Entrega

- CRUD completo evidenciado
- Scripts dos objetos Docker
- How To no GitHub
- Código fonte completo no repositório

---

# Melhorias Futuras

Possíveis evoluções:

- Healthcheck no PostgreSQL
- Containerização com Nginx
- Deploy em nuvem
- Pipeline CI/CD

---

Projeto acadêmico desenvolvido para FIAP - DevOps Tools & Cloud Computing.

