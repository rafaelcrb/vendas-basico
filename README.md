Descrição: Desenvolvi um sistema de vendas em Python com o objetivo de gerenciar produtos, clientes e realizar transações de vendas de maneira eficiente. Este projeto inclui funcionalidades essenciais para qualquer sistema de vendas, como o cadastro e listagem de produtos e clientes, além de um processo simplificado de vendas com opções de pagamento variadas.
Principais Funcionalidades:
•	Cadastro de Produtos: Permite o registro de novos produtos no sistema com nome, preço e quantidade em estoque.
•	Listagem de Produtos: Exibe todos os produtos cadastrados com seus respectivos códigos, nomes, preços e quantidades disponíveis.
•	Cadastro de Clientes: Registra informações dos clientes, como nome, idade e endereço.
•	Listagem de Clientes: Exibe todos os clientes cadastrados com seus respectivos códigos, nomes, idades e endereços.
•	Processo de Venda: Permite a realização de vendas, escolhendo produtos disponíveis em estoque, especificando a quantidade desejada e selecionando a forma de pagamento.
•	Opções de Pagamento: Oferece três formas de pagamento (cartão de crédito, dinheiro e Pix) com descontos ou acréscimos aplicáveis.
Desenvolvimento:
1.	Cadastro de Produtos:
o	Utilizei a função cadastro_produto() para receber os dados do produto via input, armazenar em uma lista temporária e adicionar à lista principal produtos.
o	Implementação de um loop para permitir múltiplos cadastros de produtos em sequência.
2.	Listagem de Produtos:
o	A função listarProdutos() percorre a lista produtos e exibe as informações formatadas de cada produto cadastrado.
3.	Cadastro de Clientes:
o	Similar ao cadastro de produtos, a função cadastro_clientes() recebe os dados do cliente e armazena em uma lista temporária que é adicionada à lista principal clientes.
4.	Listagem de Clientes:
o	A função listarClientes() exibe as informações de cada cliente cadastrado de maneira formatada.
5.	Processo de Venda:
o	A função vender() integra as funções de listagem de produtos, escolha de produto, verificação de estoque e seleção de quantidade.
o	Inclui também a chamada da função pagamento() para definir o método de pagamento e aplicar os descontos ou acréscimos necessários.
6.	Opções de Pagamento:
o	A função pagamento() apresenta as opções de pagamento e aplica os descontos ou acréscimos com base na escolha do cliente.
Conclusão: Este projeto em Python demonstrou a aplicação prática de estruturas de dados como listas bidimensionais, além do uso de funções para modularizar e organizar o código. O sistema de vendas criado serve como uma base sólida para futuros desenvolvimentos, podendo ser expandido para incluir funcionalidades adicionais, como relatórios de vendas e gestão de inventário.

Repositório GitHub:
O código-fonte do projeto está disponível no https://github.com/rafaelcrb/vendas-basico.git
