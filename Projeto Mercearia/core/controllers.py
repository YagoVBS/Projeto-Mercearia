from models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastrar_categoria(self, nova_categoria):
        existe = False
        categorias = DaoCategoria.ler()
        
        for categoria in categorias:
            if categoria.categoria == nova_categoria:
                existe = True
                break
        
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print(f'Categoria {nova_categoria} cadastrada !')
        else:
            print('Essa Categoria já existe !')
            
    def remover_categoria(self, categoria_remover):
        categorias = DaoCategoria.ler()
        categorias_restantes = list(filter(lambda x: x.categoria == categoria_remover, categorias))
        
        if len(categorias_restantes) <= 0:
            print('Essa Categoria não existe !')
        else:
            for i in range(len(categorias)):
                if categorias[i].categoria == categoria_remover:
                    del categorias[i]
                    break
            print('Categoria removida !')
            with open('categorias.txt', 'w') as arq:
                
                for i in categorias:
                    arq.writelines(f'{i.categoria}\n')
                    
        estoque = DaoEstoque.ler()
        estoque2 = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade)
                        if (x.produto.categoria == categoria_remover) else (x), estoque)) 
        
        with open('estoque.txt', 'w') as arq:
            for i in estoque2:
                arq.writelines(f'{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n')
                                       
    def alterar_categoria(self, categoria_alterar, categoria_alterada):
        categorias = DaoCategoria.ler()
        categoria_filter = list(filter(lambda x: x.categoria == categoria_alterar, categorias))
        
        if len(categoria_filter) > 0:
            categoria_existente = list(filter(lambda x: x.categoria == categoria_alterada, categorias))
            
            if len(categoria_existente) == 0:
                for i in range(len(categorias)):
                    if categorias[i].categoria == categoria_alterar:
                        categorias[i].categoria = categoria_alterada
                print('Categoria alterada com sucesso.')
                
                estoque = DaoEstoque.ler()
                estoque2 = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoria_alterada), x.quantidade)
                        if (x.produto.categoria == categoria_alterar) else (x), estoque)) 
        
                with open('estoque.txt', 'w') as arq:
                    for i in estoque2:
                        arq.writelines(f'{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n')
            else:
                print("A Categoria para qual deseja alterar já existe")
                
        else:
            print('Essa Categoria não existe !')
        
        with open('categorias.txt', 'w') as arq:
            for i in categorias:
                arq.writelines(f'{i.categoria}\n')
                                                    
    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma categoria cadastrada !')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
                              
class ControllerEstoque:
    
    def cadastrar_produto(self, nome, preco, categoria, quantidade ):
        estoque = DaoEstoque.ler()
        categoria_exist = DaoCategoria.ler()
        
        categorias = list(filter(lambda x: x.categoria == categoria, categoria_exist))
        est = list(filter(lambda x: x.produto.nome == nome, estoque))
        
        if len(categorias) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto {nome} cadastrado com sucesso !')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria não existe')
            
    def remover_produto(self, nome):
        estoque = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, estoque))
        
        if len(est) > 0:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == nome:
                    print(f'Produto {nome} removido com sucesso !')
                    del estoque[i]
                    break
        else:
            print('O produto não existe !')
            
        with open('estoque.txt', 'w') as arq:
            
            for i in estoque:
                arq.writelines(f'{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n')
                       
    def alterar_produto(self, nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        estoque = DaoEstoque.ler()
        categorias = DaoCategoria.ler()
        
        cat = list(filter(lambda x: x.categoria == nova_categoria, categorias))
        if len(cat) > 0:
            est = list(filter(lambda x: x.produto.nome == nome_alterar, estoque))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novo_nome, estoque))
                if len(est) == 0:
                    estoque = list(map(lambda x: Estoque(Produto(novo_nome, novo_preco, nova_categoria), nova_quantidade) if(x.produto.nome == nome_alterar) else(estoque), estoque))
                    print(f'Produto {nome_alterar} alterado para {novo_nome} com sucesso !')
                else:
                    print('O produto já existe !')
            else:
                print('O produto não existe !')
                
            with open('estoque.txt', 'w') as arq:
                for i in estoque:
                    arq.writelines(f'{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n')

        else:
            print('Categoria não existe')
    
    def mostrar_estoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque Vazio')
        else:
            print('=========     PRODUTO     =========')
            for i in estoque:
                
                print(f"Produto: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}"
                )    
                print("====================================")
                
class ControllerVenda:
    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        estoque = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in estoque:
            if existe == False:
                if i.produto.nome == nome_produto:
                    existe = True
                    if int(i.quantidade) >= int(quantidade_vendida):
                        quantidade = True
                        i.quantidade = i.quantidade - int(quantidade_vendida)
                        
                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade_vendida)
                        
                        valor_compra = int(quantidade_vendida) * int(i.produto.preco)
                        
                        DaoVenda.salvar(vendido)
                
            temp.append(Estoque(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        
        with open('estoque.txt', 'w') as arq:
            arq.write('')
        
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n")
                
        if existe == False:
            print('O Produto não existe')
            return None
        elif not quantidade:
            print('Quantidade insuficiente no estoque')
            return None
        else:
            print('Venda realizada com sucesso.')
            return valor_compra
            
    def relatorio_produtos(self):
        vendas = DaoVenda.ler()
        produtos = []
        
        for i in vendas:
            nome = i.itens_vendidos.nome
            quantidade = i.qtd_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if x['produto'] == nome else x, produtos))
                
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
                
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
            
        a = 1
        print('====== PRODUTOS MAIS VENDIDOS ======\n')
        for i in ordenado:
            print(f'============  PRODUTO {a} ============\n')
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            print("====================================\n")
            a += 1

    def mostrar_venda(self, data_inicio, data_termino):
        vendas = DaoVenda.ler()
        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
        data_termino = datetime.strptime(data_termino, '%d/%m/%Y')
        
        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= data_inicio
                                and datetime.strptime(x.data, '%d/%m/%Y') <= data_termino, vendas))
        
        cont = 1
        total = 0
        
        for i in vendas_selecionadas:
            print(f'=============  VENDA {cont}  ============\n')
            print(f"Nome: {i.itens_vendidos.nome}\n"
                  f"Categoria: {i.itens_vendidos.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.qtd_vendida}\n"
                  f"Cliente {i.comprador}\n"
                  f"Vendedor {i.vendedor}\n")    
            print("====================================\n")
            total += int(i.itens_vendidos.preco) * int(i.qtd_vendida)
            cont += 1
        
        print(f"Total vendido = R$ {float(total)}")
        
class ControllerFornecedor:
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        fornecedores = DaoFornecedor.ler()
        lista_cnpj = list(filter(lambda x: x.cnpj == cnpj, fornecedores))
        lista_telefone = list(filter(lambda x: x.telefone == telefone, fornecedores))
        
        if len (lista_cnpj) > 0:
            print("CNPJ já existe")
            
        elif len(lista_telefone) > 0:
            print("O telefone já existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print("Fornecedor cadastrado com sucesso")
            else:
                print("CNPJ ou telefone inválido")
    
    def remover_fornecedor(self, nome):
        fornecedores = DaoFornecedor.ler()
        lista_nomes = list(filter(lambda x: x.nome == nome, fornecedores))
        
        if len(lista_nomes) <= 0:
            print("Fornecedor não encontrado")
        else:
            for i in range(len(fornecedores)):
                if fornecedores[i].nome == nome:
                    del fornecedores[i]
                    break
                 
            with open('fornecedores.txt', 'w') as arq:
                
                for i in fornecedores:
                    arq.writelines(f'{i.nome}|{i.cnpj}|{i.telefone}|{str(i.categoria)}\n')
                print('Fornecedor deletado com sucesso.')
                
    def alterar_fornecedor(self, nome_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        
        fornecedores = DaoFornecedor.ler()
        lista_nome = list(filter(lambda x: x.nome == nome_alterar, fornecedores))
        
        if len(lista_nome) > 0:
            lista_cnpj = list(filter(lambda x: x.cnpj == novo_cnpj, fornecedores))
            
            if len(lista_cnpj) == 0:
                fornecedores = list(map(lambda x: Fornecedor(novo_nome, novo_cnpj, novo_telefone, nova_categoria)
                                    if x.nome == nome_alterar else x, fornecedores))
                print('Fornecedor alterado com sucesso !')
            else:
                print("CNPJ já existe")
        else:
            print("Fornecedor para alterar não encontrado")
            
        with open('fornecedores.txt', 'w') as arq:
            
            for i in fornecedores:
                arq.writelines(f"{i.nome}|{i.cnpj}|{i.telefone}|{str(i.categoria)}\n")
                
    def mostrar_fornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("Nenhum fornecedor cadastrado")
        
        else:
            for i in fornecedores:
                print(f'===========  FORNECEDORES ==========\n')
                print(f"Nome: {i.nome}\n"
                      f"CNPJ: {i.cnpj}\n"
                      f"Telefone: {i.telefone}\n"
                      f"Categoria: {i.categoria}\n")
                print("====================================\n")
    
class ControllerCliente:
    def cadastrar_cliente(self, nome, cpf, telefone, email, endereco):
        clientes = DaoPessoa.ler()
        lista_cpf = list(filter(lambda x: x.cpf == cpf, clientes))
        lista_telefone = list(filter(lambda x: x.telefone == telefone, clientes))
        
        if len(lista_cpf) > 0:
            print("CPF já existe")
            
        elif len(lista_telefone) > 0:
            print("Telefone já existe")
            
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoPessoa.salvar(Pessoa(nome, cpf, telefone, email, endereco))
                print('Cliente cadastrado com sucesso !')
            else:
                print("CPF ou telefone inválido")
                
    def remover_cliente(self, cpf):
        clientes = DaoPessoa.ler()
        lista_cpf = list(filter(lambda x: x.cpf == cpf, clientes))
        
        if len(lista_cpf) <= 0:
            print("CPF não encontrado")
        
        else:
            for i in range(len(clientes)):
                if clientes[i].cpf == cpf:
                    del clientes[i]
                    break
                
            with open('clientes.txt', 'w') as arq:
                for i in clientes:
                    arq.writelines(f'{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}\n')
                print('Cliente excluido com sucesso !')

    def alterar_cliente(self, cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco):
        clientes = DaoPessoa.ler()
        lista_cpf = list(filter(lambda x: x.cpf == cpf_alterar, clientes))
        
        if len(lista_cpf) > 0:
            lista_cpf2 = list(filter(lambda x: x.cpf == novo_cpf, clientes))
            
            if len(lista_cpf2) == 0:
                clientes = list(map(lambda x: Pessoa(novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco)
                                if x.cpf == cpf_alterar else x, clientes))
                print('Cliente alterado com sucesso !')
            else:
                print("CPF já existe")
               
        else:
            print("CPF do cliente não encontrado !")
        
        with open('clientes.txt', 'w') as arq:
            for i in clientes:
                arq.writelines(f'{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}\n')
            
    def mostrar_cliente(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print("Nenhum cliente encontrado !")
        else:
            for i in clientes:
                print(f'===========  CLIENTES ==========\n')
                print(f"Nome: {i.nome}\n"
                      f"CPF: {i.cpf}\n"
                      f"Telefone: {i.telefone}\n"
                      f"Email: {i.email}\n"
                      f"Endereço: {i.endereco}\n")
                print("====================================\n")
                 
class ControllerFuncionario:
    def cadastrar_funcionario(self, clt, nome, cpf, telefone, email, endereco, salario):
        funcionarios = DaoFuncionario.ler()
        lista_cpf = list(filter(lambda x: x.cpf == cpf, funcionarios))
        lista_clt = list(filter(lambda x: x.clt == clt, funcionarios))
        
        if len(lista_cpf) > 0:
            print("CPF do funcionário já existe !")
        elif len(lista_clt) > 0:
            print("Contrato CLT já existe !")
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFuncionario.salvar(Funcionario(clt, nome, cpf, telefone, email, endereco, salario))
                print('Funcionário cadastrado com sucesso !')
            else:
                print("CPF ou telefone inválido !")
                
    def remover_funcionario(self, cpf):
        funcionarios = DaoFuncionario.ler()
        lista_cpf = list(filter(lambda x: x.cpf == cpf, funcionarios))
        
        if len(lista_cpf) <= 0:
            print("CPF não encontrado !")
        else:
            for i in range(len(funcionarios)):
                if funcionarios[i].cpf == cpf:
                    del funcionarios[i]
                    break
                
            with open('funcionarios.txt', 'w') as arq:
                for i in funcionarios:
                    arq.writelines(f'{i.clt}|{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}|{i.salario}\n')
                print('Funcionário excluído com sucesso !')
 
    def alterar_funcionario(self, cpf_alterar, novo_clt, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco, novo_salario):
        funcionarios = DaoFuncionario.ler()
        lista_cpf = (list(filter(lambda x: x.cpf == cpf_alterar, funcionarios)))
        
        if len(lista_cpf) > 0:
            lista_cpf_validado = list(filter(lambda x: x.cpf == novo_cpf, funcionarios))
            if len(lista_cpf_validado) == 0:
                funcionarios = list(map(lambda x: Funcionario(novo_clt, novo_nome, novo_cpf, novo_telefone, novo_email,
                                                              novo_endereco, novo_salario)
                                        if x.cpf == cpf_alterar else x, funcionarios))
                print('Funcionario alterado com sucesso !')
            else:
                print('CPF já existe !')
        else:
            print("CPF não encontrado !")
            
        with open('funcionarios.txt', 'w') as arq:
            for i in funcionarios:
                arq.writelines(f'{i.clt}|{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}|{i.salario}\n')
            
    def mostrar_funcionario(self):
            funcionarios = DaoFuncionario.ler()
            if len(funcionarios) == 0:
                print("Nenhum funcionário cadastrado !")
            else:
                for i in funcionarios:
                    print(f'===========  FUNCIONARIOS ==========\n')
                    print(f"CLT: {i.clt}\n"
                          f"Nome: {i.nome}\n"
                          f"CPF: {i.cpf}\n"
                          f"Telefone: {i.telefone}\n"
                          f"Email: {i.email}\n"
                          f"Endereço: {i.endereco}\n"
                          f"Salario: {i.salario}")
                    print("====================================\n")
                