# Sistema de Gestão para Mercearias 🛒

Este é um sistema desenvolvido em **Python**, utilizando o padrão arquitetural **MVC** (Model-View-Controller), com foco no gerenciamento de mercearias. Ele é totalmente acessível via terminal e foi projetado para consolidar conceitos fundamentais de **POO** e boas práticas de programação.

---

## 🚀 Funcionalidades

- **Produtos**: Cadastro, listagem, atualização e remoção de produtos, com controle de estoque.
- **Clientes**: Gerenciamento de cadastro e consulta de clientes.
- **Fornecedores**: Controle de fornecedores registrados.
- **Vendas**: Registro de vendas com controle detalhado de itens vendidos.

---

## 🛠️ Tecnologias e Práticas

- **Python 3.10+**  
- Estrutura em **MVC** para organização e separação de responsabilidades.  
- Utilização de **POO** com herança, encapsulamento e polimorfismo.  
- Persistência de dados com arquivos `.txt`.  
- **Validações** e **tratamento de exceções** para maior robustez.  
- **Testes unitários** para garantir a qualidade do código.  

---

## 📂 Estrutura do Projeto

```plaintext
├── core/
│   ├── controllers.py
│   ├── models.py
│   ├── views.py
|   └── DAO.py
├── categorias.txt
├── clientes.txt
├── estoque.txt
├── fornecedores.txt
├── vendas.txt
└── README.md
