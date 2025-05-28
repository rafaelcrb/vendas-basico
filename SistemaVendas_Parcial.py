#SISTEMA DE VENDAS

def cadastro_produto():
    nome = input('Qual o Nome do Produto? ')
    preco = float(input('Qual o o Preço do Produto? '))
    quantidade = int(input('Qual a Quantidade em Estoque? '))
    print('--'*20)
    print('PRODUTO CADASTRADO COM SUCESSO! ')
    print('--'*20)
    print('Deseja Realizar outro Cadastro ? ')
   
    resp = str(input('Sim ou Não? '))
    if resp == 's':
        cadastro_produto()

    os.system('cls')

    produto = []                               #para colocar os dados na lista usamos o apppend

    produto.append(nome)
    produto.append(preco)
    produto.append(quantidade)

    produtos.append (produto)                #para adicionar essa lista a lista principal 'Produtos', se torna rede bidimencional

def listarProdutos():                                    
    for i in range(0, len(produtos)):                     
         print('--'*20)
         print('PRODUTO CADASTRADO. ')
         print('Código: {} - Produto: {} - Preço: R${:.2f} - Estoque: {}'.format(i, produtos[i][0], produtos[i][1], produtos[i][2]))       
                                                                  
def cadastro_clientes():
    nome = str(input('Digite seu Nome: '))
    idade = int(input('Digite sua Idade: '))
    endereco = str(input('Digite seu Endereço: '))
    print('--'*20)
    print('CLIENTE CADASTRADO COM SUCESSO! ')
    print('--'*20)
    print('Deseja Realizar outro Cadastro ? ')
   
    resp = str(input('Sim ou Não? '))
    if resp == 's':
        cadastro_clientes()

    os.system('cls')

    cliente = []

    cliente.append(nome)
    cliente.append(idade)
    cliente.append(endereco)

    clientes.append(cliente)

def listarClientes():
    for i in range(0, len(clientes)):
        print('--'*20)
        print('CLIENTE CADASTRADO.')
        print('Código: {} - Nome: {} - Idade: {} - Endereço: {}'.format(i, clientes [i][0], clientes [i][1], clientes [i][2]))
        print('--'*20)
               
def vender():
    print('Escolha um Produto Abaixo: ')
    listarProdutos()
    numero = int(input('Digite o Código do Produto: '))
    quantidade = int(input('Quantidade: '))                
    
    if produtos [numero][2] >= quantidade:                                  #Verificar se a quantidade está disponivel em estoque
        print ('Escolha a opção de Pagamento: ')
        pagamento()
        print('--'*20)
        print('Produto Vendido Com Sucesso!')
        print('--'*20)
        print('---------Informações da Venda:---------\nProduto: ..................... {}\nQuantidade: .................. {}\nValor Total: ................. R${:.2f}'.format(produtos[numero][0], quantidade, quantidade * produtos[numero][1]))
        produtos [numero][2] -= quantidade                                  #na linha numero na coluna 2 ... esse -= significa retirando da variavel o valor espercifico
        
    else:
        print('Quantidade Indisponivel em Estoque.')

def pagamento():
    print('--'*20)
    print('Opções de Pagamento: ')
    print('[1] - Cartão de Crédito.')
    print('[2] - Dinheiro. ')
    print('[3] - Pix. ')
    print('--'*20)
    opc_pagamento = int(input('Digite a Opção de pagamento: '))

    if opc_pagamento == 1:
        print('--'*20)
        print('Acrescimo de 5% no Cartão')
        print('Obrigado, Volte Sempre')
        #print('--'*20)

    elif opc_pagamento == 2:
        print('--'*20)
        print('Desconto de 3% Avista ')
        print('Obrigado, Volte Sempre')
        #print('--'*20)

    elif opc_pagamento == 3:
        print('--'*20)
        print('Desconto de 5% no Pix')
        print('Obrigado, Volte Sempre')
       # print('--'*20)
    else:
        print('--'*20)
        print('Opção de Pagamento Não Existe. \nTente Novamente! ')
        print('                  ')
        os.system('pause')
        os.system('cls')

import os
clientes = []
produtos = []
opcao = 0

while (opcao != 6):
    print(' REALIZE SEU PEDIDO. . . ')
    print('================================')
    print('     MENU:                      ')
    print('================================')
    print('     [1] - Cadastrar Produto    ')
    print('     [2] - Listar Produtos      ')
    print('     [3] - Cadastrar Clientes   ')
    print('     [4] - Listar Clientes      ') 
    print('     [5] - Vender               ')
    print('     [6] - Sair                 ')
    print('================================')
    opcao = int(input('Digite Uma Opção: '))

    if (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao !=6 ):
        print('Opção Inválida.')
        os.system('pause')
        os.system('cls')
        continue
        
    if opcao == 1:
        cadastro_produto()            

    if opcao == 2:
        listarProdutos()
        os.system('pause')
        
    if opcao == 3:
        cadastro_clientes()

    if opcao == 4:
        listarClientes()  
        os.system('pause')
        
    if opcao == 5:
        vender()
        print('                      ')
        os.system('pause')     
            
    
    if opcao == 6:
        print('Obrigado Pela Preferência, Volte Sempre! ')
        break
                                            

