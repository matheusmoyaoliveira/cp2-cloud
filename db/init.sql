CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clientes (nome, email, telefone)
VALUES
('Matheus Moya', 'matheus@email.com', '11999990000'),
('Ana Carolina', 'ana@email.com', '11988880000')
ON CONFLICT (email) DO NOTHING;