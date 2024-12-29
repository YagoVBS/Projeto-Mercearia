from models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(f'{categoria}')
            arq.writelines('\n')
     
    @classmethod        
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        categorias = []
        for categoria in cls.categoria:
            categorias.append(Categoria(categoria))
            
        return categorias    
            
class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(f'{produto.nome}|{produto.preco}|{produto.categoria}|{quantidade}')
            arq.writelines('\n')
            
    @classmethod    
    def ler(cls):
        
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
            
        estoque_list = []
        if len(cls.estoque) > 0:
            for produto in cls.estoque:
                estoque_list.append(Estoque(Produto(produto[0], produto[1], produto[2]), int(produto[3])))
                    
        return estoque_list

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(f'{fornecedor.nome}|{fornecedor.cnpj}|{fornecedor.telefone}|{fornecedor.categoria}\n')
                           
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        
        fornecedores = []
        for fornecedor in cls.fornecedor:
            fornecedores.append(Fornecedor(fornecedor[0], fornecedor[1], fornecedor[2], fornecedor[3]))
            
        return fornecedores
       
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            linha = (venda.itens_vendidos.nome,'|', venda.itens_vendidos.preco, '|', venda.itens_vendidos.categoria, '|',
                      venda.vendedor, '|', venda.comprador, '|', str(venda.qtd_vendida), '|', venda.data)
            
            arq.writelines(linha)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vendas = []
        for venda in cls.venda:
            vendas.append(Venda(Produto(venda[0], venda[1], venda[2]),venda[3], venda[4], venda[5], venda[6]))
            
        return vendas
    
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            linha = (funcionario.clt, '|', funcionario.nome, '|', funcionario.cpf, '|', funcionario.telefone, '|', funcionario.email,
                     '|', funcionario.endereco, '|', funcionario.salario)
            
            arq.writelines(linha)
            arq.writelines('\n')            
            
                      
    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        
        funcionarios = []
        for funcionario in cls.funcionario:

            funcionarios.append(Funcionario(funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4],
                                            funcionario[5], funcionario[6]))
            
        return funcionarios
    
class DaoPessoa:
    @classmethod
    def salvar(cls, cliente : Pessoa):
        with open('clientes.txt', 'a') as arq:
            linha = (cliente.nome,'|', cliente.cpf, '|', cliente.telefone, '|', cliente.email, '|', cliente.endereco)
            arq.writelines(linha)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open ('clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()
            
        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))
        
        clientes = []
        for cliente in cls.cliente:
            clientes.append(Pessoa(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))
            
        return clientes
    
