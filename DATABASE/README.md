# NADIC-DATABASE

Este diretório contém o projeto de banco de dados para o sistema de Controle de Finanças Pessoais. O projeto abrange desde um nível de abstração mais elevado, com o modelo Entidade-Relacionamento (ER), até a implementação no banco de dados relacional.

## Descrição do Projeto

O projeto de banco de dados visa fornecer uma estrutura para o controle de finanças pessoais, permitindo o registro e a análise de transações financeiras associadas a diferentes contas e categorias de despesas/receitas.

### Entidades e Relacionamentos

- **Entidades:**
  - Contas
  - Transações
  - Categorias

- **Relacionamentos:**
  - Uma transação está associada a uma conta.
  - Uma transação pertence a uma categoria.

## Modelagem do Banco de Dados

O modelo de banco de dados foi desenvolvido seguindo as melhores práticas de modelagem de dados, começando pelo diagrama Entidade-Relacionamento (ER) e mapeando-o para tabelas no modelo relacional. Foram consideradas as necessidades de consulta, inserção, exclusão e atualização de informações, bem como os relacionamentos entre os dados e as restrições adequadas.

## Tecnologias Utilizadas

Para a implementação do banco de dados, foram considerados os seguintes sistemas de gerenciamento de banco de dados (SGBD):
- MySQL (Escolhido)
- PostgreSQL
- SQLite

## Pendências

- [x] Criar diagrama ER para representar as entidades e relacionamentos do sistema.
- [x] Mapear o diagrama ER para o modelo relacional, identificando tabelas, atributos e chaves.
- [x] Implementar o esquema do banco de dados em pelo menos um dos SGBDs listados.
- [x] Desenvolver consultas SQL para consulta, inserção, deleção e atualização de dados.
- [x] Testar e validar o funcionamento do banco de dados em diferentes cenários.
