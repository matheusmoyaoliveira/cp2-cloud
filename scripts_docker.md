# Scripts Docker - CP2 Cloud Computing

Este arquivo contém os comandos equivalentes para criação manual dos objetos Docker utilizados no projeto.

## 1. Criar a rede Docker

```bash
docker network create rm562822_rm562145_network
```

## 2. Criar o volume nomeado do PostgreSQL

```bash
docker volume create rm562822_rm562145_postgres_data
```

## 3. Criar e executar o container do banco PostgreSQL

### Windows CMD

```bash
docker run --name rm562822_rm562145_db_clientes -d ^
-e POSTGRES_DB=cp2_cloud ^
-e POSTGRES_USER=cp2_user ^
-e POSTGRES_PASSWORD=cp2_password ^
-p 5432:5432 ^
-v rm562822_rm562145_postgres_data:/var/lib/postgresql/data ^
-v "%cd%/db/init.sql":/docker-entrypoint-initdb.d/init.sql ^
--network rm562822_rm562145_network ^
postgres:16
```

### Linux / Git Bash

```bash
docker run --name rm562822_rm562145_db_clientes -d \
-e POSTGRES_DB=cp2_cloud \
-e POSTGRES_USER=cp2_user \
-e POSTGRES_PASSWORD=cp2_password \
-p 5432:5432 \
-v rm562822_rm562145_postgres_data:/var/lib/postgresql/data \
-v $(pwd)/db/init.sql:/docker-entrypoint-initdb.d/init.sql \
--network rm562822_rm562145_network \
postgres:16
```

## 4. Criar a imagem da API Flask

```bash
docker build -t cp2-cloud-app ./app
```

## 5. Criar e executar o container da API

### Windows CMD

```bash
docker run --name rm562822_rm562145_api_clientes -d ^
-e DB_HOST=rm562822_rm562145_db_clientes ^
-e DB_NAME=cp2_cloud ^
-e DB_USER=cp2_user ^
-e DB_PASSWORD=cp2_password ^
-e DB_PORT=5432 ^
-p 5000:5000 ^
--network rm562822_rm562145_network ^
cp2-cloud-app
```

## 6. Verificações

```bash
docker ps --filter "name=rm562822_rm562145"
```

```bash
docker image ls
```

```bash
docker volume ls
```

```bash
docker network ls
```

## 7. Acessar banco para validar CRUD

```bash
docker exec -it rm562822_rm562145_db_clientes psql -U cp2_user -d cp2_cloud
```

```sql
SELECT * FROM clientes;
```

## 8. Remover containers

```bash
docker rm -f rm562822_rm562145_api_clientes
docker rm -f rm562822_rm562145_db_clientes
```

## 9. Execução principal do projeto (oficial)

A forma principal adotada no projeto é via Docker Compose:

```bash
docker compose up -d --build
```

Parar ambiente:

```bash
docker compose down
```

Remover inclusive volumes:

```bash
docker compose down -v
```

## Objetos Docker criados por este projeto

- Network Docker customizada
- Volume nomeado para persistência
- Container da API
- Container do Banco PostgreSQL
- Comunicação entre containers em rede bridge
- Port mapping
- Variáveis de ambiente
- Execução em segundo plano

## Requisitos do checkpoint atendidos por estes scripts

- Uso de imagens do Docker Hub
- Dois containers interagindo
- Banco com volume nomeado
- Containers em rede Docker
- Containers com portas expostas
- Variáveis de ambiente (-e)
- Containers em segundo plano (-d)
- Containers com nomes contendo RM

---

Projeto acadêmico desenvolvido para o CP2 de Cloud Computing (FIAP).

