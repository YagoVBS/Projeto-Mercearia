from datetime import datetime

class Categoria:
    def __init__(self,categoria):
        self.categoria = categoria
             
             
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
class Estoque:
    def __init__(self,produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
  
class Venda:
    def __init__(self, itens_vendidos: Produto, vendedor, comprador, qtd_vendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itens_vendidos = itens_vendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.qtd_vendida = qtd_vendida
        self.data = data  
       
class Fornecedor:
    def __init__(self, nome , cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
        
class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
class Funcionario(Pessoa):
    def __init__(self, clt, nome, cpf, telefone, email, endereco, salario):
        super().__init__(nome, cpf, telefone, email, endereco)
        self.clt = clt
        self.salario = salario
             
        

                