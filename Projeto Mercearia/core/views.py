from controllers import *
import os

def criar_arquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")
                
criar_arquivos("categorias.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", 
               "funcionarios.txt", "vendas.txt")

def limpar_tela():
    return os.system('cls')           
     
if __name__ == "__main__":
    while True:
        decisao = int(input("========== MENU ==========\n"
                            "1 - Categorias\n"
                            "2 - Estoque\n"
                            "3 - Fornecedores\n"
                            "4 - Clientes\n"
                            "5 - Funcionarios\n"
                            "6 - Vendas\n"
                            "7 - Produtos mais Vendidos\n"
                            "8 - Sair\n"
                            "===========================\n"
                            ))
        
        limpar_tela()
        
        if decisao == 1:
            categorias = ControllerCategoria()
            while True:
                opcao = int(input(
                    "========== CATEGORIAS ==========\n"
                    "1 - Cadastrar Categoria\n"
                    "2 - Remover Categoria\n"
                    "3 - Alterar Categoria\n"
                    "4 - Listar Categorias\n"
                    "5 - Voltar\n"
                    "================================\n"
                    ))
                limpar_tela()
                
                if opcao == 1:
                    categoria = input("Digite a categoria que deseja cadastrar:\n")
                    limpar_tela()
                    categorias.cadastrar_categoria(categoria)
                    
                elif opcao == 2:
                    categoria = input("Digite a categoria que deseja remover: \n")
                    categorias.remover_categoria(categoria)
                    
                elif opcao == 3:
                    categoria = input("Digite a categoria que deseja alterar: \n")
                    nova_categoria = input("Digite a nova categoria: \n")
                    categorias.alterar_categoria(categoria, nova_categoria)
                
                elif opcao == 4:
                    categorias.mostrar_categoria()
                    
                elif opcao == 5:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
                    
        if decisao == 2:
            estoque = ControllerEstoque()
            while True:
                opcao = int(input(
                    "========== ESTOQUE ==========\n"
                    "1 - Cadastrar Produto\n"
                    "2 - Remover Produto\n"
                    "3 - Alterar Produto\n"
                    "4 - Listar Produtos\n"
                    "5 - Voltar\n"
                    "=============================\n"
                ))
                limpar_tela()
                
                if opcao == 1:
                    produto = input("Digite o nome do produto que deseja cadastrar:\n")
                    preco = input("Digite o preço do produto:\n")
                    categoria = input("Digite a categoria do produto:\n")
                    quantidade = input("Digite a quantidade do produto:\n")
                    estoque.cadastrar_produto(produto, preco, categoria, quantidade)
                    
                elif opcao == 2:
                    produto = input("Digite o nome do produto que deseja remover: \n")
                    estoque.remover_produto(produto)
                    
                elif opcao == 3:
                    nome_alterar = input("Digite o nome do produto que deseja alterar: \n")
                    novo_nome = input("Digite o novo nome do produto:\n")
                    novo_preco = input("Digite o novo preço:\n")
                    nova_categoria = input("Digite a nova categoria:\n")
                    nova_quantidade = input("Digite a nova quantidade:\n")
                    estoque.alterar_produto(nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade)
                    
                elif opcao == 4:
                    estoque.mostrar_estoque()
                    
                elif opcao == 5:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
                    
        if decisao == 3:
            fornecedor = ControllerFornecedor()
            while True:
                opcao = int(input(
                    "========== FORNECEDOR ==========\n"
                    "1 - Cadastrar Fornecedor\n"
                    "2 - Remover Fornecedor\n"
                    "3 - Alterar Fornecedor\n"
                    "4 - Listar Fornecedores\n"
                    "5 - Voltar\n"
                    "=============================\n"
                ))
                limpar_tela()
                
                if opcao == 1:
                    nome = input("Digite o nome do fornecedor:\n")
                    cnpj = input("Digite o CNPJ do fornecedor:\n")
                    telefone = input("Digite o telefone do fornecedor:\n")
                    categoria = input("Digite a categoria do fornecedor:\n")
                    fornecedor.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                    
                elif opcao == 2:
                    nome = input("Digite o nome do fornecedor que deseja remover: \n")
                    fornecedor.remover_fornecedor(nome)
                    
                elif opcao == 3:
                    nome_alterar = input("Digite o nome do fornecedor que deseja alterar:\n")
                    novo_nome = input("Digite o novo nome do fornecedor:\n")
                    novo_cnpj = input("Digite o novo CNPJ do fornecedor:\n")
                    novo_telefone = input("Digite o novo telefone do fornecedor:\n")
                    nova_categoria = input("Digite a nova categoria do fornecedor:\n")
                    fornecedor.alterar_fornecedor(nome_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria)
                    
                elif opcao == 4:
                    fornecedor.mostrar_fornecedores()
                    
                elif opcao == 5:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
        
        if decisao == 4:
            cliente = ControllerCliente()
            while True:
                opcao = int(input(
                    "========== CLIENTE ==========\n"
                    "1 - Cadastrar Cliente\n"
                    "2 - Remover Cliente\n"
                    "3 - Alterar Cliente\n"
                    "4 - Listar Clientes\n"
                    "5 - Voltar\n"
                    "=============================\n"
                    ))
                limpar_tela()
                
                if opcao == 1:
                    nome = input("Digite o nome do cliente:\n")
                    cpf = input("Digite o CPF do cliente:\n")
                    telefone = input("Digite o telefone do cliente:\n")
                    email = input("Digite o email do cliente:\n")
                    endereco = input("Digite o endereço do cliente:\n")
                    cliente.cadastrar_cliente(nome, cpf, telefone, email, endereco)
                    
                elif opcao == 2:
                    cpf = input("Digite o CPF do cliente para remover:\n")
                    cliente.remover_cliente(cpf)
                    
                elif opcao == 3:
                    cpf_alterar = input("Digite o CPF do cliente que deseja alterar:\n")
                    novo_nome = input("Digite o novo nome do cliente:\n")
                    novo_cpf = input("Digite o novo CPF do cliente:\n")
                    novo_telefone = input("Digite o novo telefone do cliente:\n")
                    novo_email = input("Digite o novo email do cliente:\n")
                    novo_endereco = input("Digite o novo endereço do cliente:\n")
                    cliente.alterar_cliente(cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco)
                    
                elif opcao == 4:
                    cliente.mostrar_cliente()
                    
                elif opcao == 5:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
        
        if decisao == 5:
            funcionario = ControllerFuncionario()
            while True:
                opcao = int(input(
                    "========== FUNCIONARIO ==========\n"
                    "1 - Cadastrar Funcionario\n"
                    "2 - Remover Funcionario\n"
                    "3 - Alterar Funcionario\n"
                    "4 - Listar Funcionarios\n"
                    "5 - Voltar\n"
                    "=============================\n"
                    ))
                limpar_tela()
                
                if opcao == 1:
                    clt = input("Digite o codigo do clt:\n")
                    nome = input("Digite o nome do funcionario:\n")
                    cpf = input("Digite o CPF do funcionario:\n")
                    telefone = input("Digite o telefone do funcionario:\n")
                    email = input("Digite o email do funcionario:\n")
                    endereco = input("Digite o endereço do funcionario:\n")
                    salario = input("Digite o salario do funcionario:\n")
                    funcionario.cadastrar_funcionario(clt, nome, cpf, telefone, email, endereco, salario)
                
                elif opcao == 2:
                    cpf = input("Digite o CPF do funcionario para remover:\n")
                    funcionario.remover_funcionario(cpf)
                    
                elif opcao == 3:
                    cpf_alterar = input("Digite o CPF do funcionario que deseja alterar:\n")
                    novo_clt = input("Digite o número do CLT:\n")
                    novo_nome = input("Digite o novo nome do funcionario:\n")
                    novo_cpf = input("Digite o novo CPF do funcionario:\n")
                    novo_telefone = input("Digite o novo telefone do funcionario:\n")
                    novo_email = input("Digite o novo email do funcionario:\n")
                    novo_endereco = input("Digite o novo endereço do funcionario:\n")
                    novo_salario = input("Digite o novo salario do funcionario:\n")
                    funcionario.alterar_funcionario(cpf_alterar, novo_clt, novo_nome, novo_cpf, novo_telefone,
                                                    novo_email, novo_endereco, novo_salario)
                    
                elif opcao == 4:
                    funcionario.mostrar_funcionario()
                    
                elif opcao == 5:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
        
        if decisao == 6:
            venda = ControllerVenda()
            while True:
                opcao = int(input(
                    "========== VENDAS ==========\n"
                    "1 - Cadastrar Venda\n"
                    "2 - Mostrar Vendas\n"
                    "3 - Voltar\n"
                    "=============================\n"
                    ))
                
                if opcao == 1:
                    nome_produto = input("Digite o nome do produto:\n")
                    vendedor = input("Digite o nome do vendedor:\n")
                    comprador = input("Digite o nome do cliente:\n")
                    quantidade = input("Digite a quantidade vendida:\n")
                    venda.cadastrar_venda(nome_produto, vendedor, comprador, quantidade)
                    
                elif opcao == 2:
                    data_inicio = input("Digite data inicial:\n")
                    data_termino = input("Digite data final:\n")
                    venda.mostrar_venda(data_inicio, data_termino)
                    
                elif opcao == 3:
                    break
                
                else:
                    print("Opção invalida, tente novamente.")
                    
        if decisao == 7:
            relatorio = ControllerVenda()
            relatorio.relatorio_produtos()
            
        if decisao == 8:
            print("Encerrando o programa ...")
            break
        
        else:
            print("Opção invalida, tente novamente.")
            