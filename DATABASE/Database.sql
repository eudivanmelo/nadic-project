-- Criar banco de dados
CREATE DATABASE NADIC_PROJECT;

-- Selecionar bando de dados utilizado no projeto
USE NADIC_PROJECT;

-- Criar tabela do usuário
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Criar tabela de contas
CREATE TABLE Account (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    name CHAR(50) NOT NULL,
    balance DECIMAL(16, 2) NOT NULL
);

-- Criar tabela de categorias
CREATE TABLE Category(
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name CHAR(50) NOT NULL,
    type ENUM('Expense', 'Revenue')
);

-- Criar tabela de transações
CREATE TABLE Transaction (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Account(account_id),
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    date DATE NOT NULL,
    value DECIMAL(16, 2) NOT NULL
);