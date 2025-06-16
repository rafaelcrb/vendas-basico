# Documentação Técnica - Sistema de Vendas Básico

## 1. Visão Geral

Este projeto implementa um sistema de vendas básico em Python, operado via console. Ele permite o cadastro e listagem de produtos e clientes, bem como a realização de vendas, incluindo verificação de estoque e opções de pagamento.

## 2. Estrutura do Projeto

A estrutura do projeto é composta por um único arquivo Python:

```
vendas-basico/
├── SistemaVendas_Parcial.py    # Código principal do sistema de vendas
└── README.md                   # Arquivo de documentação do projeto
```

## 3. Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.

## 4. Funcionalidades Principais

O sistema é dividido em várias funções, cada uma responsável por uma parte da lógica de negócio:

### `cadastro_produto()`

*   Permite ao usuário inserir o nome, preço e quantidade em estoque de um novo produto.
*   Armazena os dados do produto em uma lista global `produtos`.
*   Inclui uma opção para cadastrar múltiplos produtos sequencialmente.

### `listarProdutos()`

*   Exibe uma lista formatada de todos os produtos cadastrados, incluindo código, nome, preço e quantidade em estoque.

### `cadastro_clientes()`

*   Permite ao usuário inserir o nome, idade e endereço de um novo cliente.
*   Armazena os dados do cliente em uma lista global `clientes`.
*   Inclui uma opção para cadastrar múltiplos clientes sequencialmente.

### `listarClientes()`

*   Exibe uma lista formatada de todos os clientes cadastrados, incluindo código, nome, idade e endereço.

### `vender()`

*   Guia o usuário através do processo de venda.
*   Primeiro, lista os produtos disponíveis para que o usuário escolha.
*   Solicita a quantidade desejada e verifica a disponibilidade em estoque.
*   Se houver estoque suficiente, chama a função `pagamento()` e exibe um resumo da venda, atualizando o estoque do produto.
*   Caso contrário, informa que a quantidade é indisponível.

### `pagamento()`

*   Apresenta opções de pagamento (Cartão de Crédito, Dinheiro, Pix).
*   Aplica acréscimos ou descontos fictícios com base na opção escolhida.

## 5. Estruturas de Dados Globais

*   **`clientes`**: Uma lista de listas, onde cada sublista representa um cliente com seus dados (nome, idade, endereço).
*   **`produtos`**: Uma lista de listas, onde cada sublista representa um produto com seus dados (nome, preço, quantidade em estoque).

## 6. Fluxo de Operação

O sistema opera através de um menu principal interativo em um loop `while`:

1.  O menu exibe as opções disponíveis: Cadastrar Produto, Listar Produtos, Cadastrar Clientes, Listar Clientes, Vender e Sair.
2.  O usuário digita um número correspondente à opção desejada.
3.  A função apropriada é chamada com base na escolha do usuário.
4.  O loop continua até que o usuário escolha a opção 'Sair'.

## 7. Configuração e Execução

Para configurar e executar o projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x

### Instalação

Não há dependências externas complexas. Basta clonar o repositório:

```bash
git clone https://github.com/rafaelcrb/vendas-basico.git
cd vendas-basico
```

### Execução

1.  Navegue até o diretório do projeto.
2.  Execute o script Python:
    ```bash
    python SistemaVendas_Parcial.py
    ```

## 8. Considerações de Desenvolvimento

*   Este é um projeto console-based, ideal para demonstrar conceitos básicos de lógica de programação e interação com o usuário.
*   Os dados (clientes e produtos) são armazenados em memória e não são persistentes; eles são perdidos ao encerrar o programa.
*   A validação de entrada do usuário é básica.
*   O uso de `os.system('cls')` e `os.system('pause')` é específico para sistemas Windows e pode não funcionar em outros sistemas operacionais sem adaptações.

