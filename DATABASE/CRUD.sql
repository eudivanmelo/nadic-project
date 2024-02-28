-- Arquivo destino as consultas, inserções, deleção e atualizações de dados.

-- INSERÇÕES
-- Inserir usuários
INSERT INTO User (email, password) VALUES
('usuario1@example.com', 'senha123'),
('usuario2@example.com', 'senha456'),
('usuario3@example.com', 'senha789');

-- Inserir contas
INSERT INTO Account (user_id, name, balance) VALUES
(1, 'Conta Corrente', 5000.00),
(1, 'Conta Poupança', 10000.00),
(2, 'Conta Poupança', 7500.00),
(3, 'Conta Corrente', 3000.00),
(3, 'Conta Salário', 6000.00);

-- Inserir categorias
INSERT INTO Category (name, type) VALUES
('Alimentação', 'Expense'),
('Transporte', 'Expense'),
('Salário', 'Revenue'),
('Lazer', 'Expense'),
('Educação', 'Expense'),
('Investimento', 'Expense'),
('Presente', 'Expense');

-- Inserir transações
INSERT INTO Transaction (account_id, category_id, date, value) VALUES
(1, 1, '2024-02-25', 150.50),
(1, 2, '2024-02-26', 80.00),
(2, 3, '2024-02-25', 3000.00),
(2, 4, '2024-02-26', 200.00),
(3, 5, '2024-02-25', 120.00),
(3, 6, '2024-02-26', 500.00),
(4, 1, '2024-02-25', 50.00),
(4, 2, '2024-02-26', 70.00),
(5, 3, '2024-02-25', 1500.00),
(5, 4, '2024-02-26', 300.00);

-- CONSULTAS
-- Consultar todos os usuários
SELECT * FROM User;

-- Consultar todas as contas de um usuário específico
SELECT * FROM Account WHERE user_id = 1;

-- Consultar todas a transações de uma determinada conta
SELECT * FROM Transaction WHERE account_id = 2;

-- Consultar todas as transações de uma determinada categoria
SELECT * FROM Transaction WHERE category_id = 1;

-- DELEÇÃO
-- Deletar um usuário pelo ID
DELETE FROM User WHERE user_id = 3;

-- ATUALIZAÇÃO
-- Atualizar o email de um usuário pelo ID
UPDATE User SET email = 'novousuario@example.com' WHERE user_id = 2;