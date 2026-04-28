@echo off

echo Criando rede Docker...
docker network create rm562822_rm562145_network

echo Criando volume nomeado...
docker volume create rm562822_rm562145_postgres_data

echo Criando container PostgreSQL...
docker run --name rm562822_rm562145_db_clientes -d ^
-e POSTGRES_DB=cp2_cloud ^
-e POSTGRES_USER=cp2_user ^
-e POSTGRES_PASSWORD=cp2_password ^
-p 5432:5432 ^
-v rm562822_rm562145_postgres_data:/var/lib/postgresql/data ^
-v "%cd%/db/init.sql":/docker-entrypoint-initdb.d/init.sql ^
--network rm562822_rm562145_network ^
postgres:16

echo Aguardando o banco inicializar...
timeout /t 10

echo Criando container da API com imagem oficial Python...
docker run --name rm562822_rm562145_api_clientes -d ^
-v "%cd%/app":/app ^
-w /app ^
-e DB_HOST=rm562822_rm562145_db_clientes ^
-e DB_NAME=cp2_cloud ^
-e DB_USER=cp2_user ^
-e DB_PASSWORD=cp2_password ^
-e DB_PORT=5432 ^
-p 5000:5000 ^
--network rm562822_rm562145_network ^
python:3.12-slim ^
sh -c "pip install -r requirements.txt && python app.py"

echo Objetos Docker criados com sucesso.
docker ps --filter "name=rm562822_rm562145"