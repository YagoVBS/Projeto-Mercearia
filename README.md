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
├── models/
│   ├── produto.py
│   ├── cliente.py
│   └── fornecedor.py
├── views/
│   └── main_view.py
├── controllers/
│   ├── produto_controller.py
│   ├── cliente_controller.py
│   └── fornecedor_controller.py
├── tests/
│   ├── test_produto.py
│   └── test_cliente.py
├── data/
│   ├── produtos.txt
│   ├── clientes.txt
│   └── fornecedores.txt
└── README.md
