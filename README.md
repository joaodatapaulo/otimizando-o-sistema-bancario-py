🐍 **Otimizando o Sistema Bancário com Python**

Este projeto teve como objetivo modularizar o código do sistema bancário, criando funções para operações de depósito, saque e visualização de extrato, além de duas novas funções: criação de usuário e criação de conta.

Para cada função, foi definida uma regra de argumentos e retornos que cada uma deveria ter, e para as duas novas funções não foi diferente. Sendo elas:

- Saque
<br /> Argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques (keyword only).
<br /> Retorno: saldo e extrato.

- Depósito
<br /> Argumentos: saldo, valor, extrato (positional only).
<br /> Retorno: saldo e extrato.

- Extrato
<br /> Argumentos: saldo (positional only) e extrato (keyword).

Novas Funções:

- Criar Usuário
<br /> Armazenar usuários em uma lista com nome, data de nascimento, CPF (apenas números) e endereço (formato específico).
<br /> Garantir que não haja duplicidade de CPF.

- Criar Conta Corrente
<br /> Armazenar contas em uma lista com agência (fixa em "0001"), número sequencial da conta (iniciando em 1) e usuário associado.
<br /> Permitir que um usuário tenha várias contas, mas cada conta pertença a um único usuário.

Com os conhecimentos adquiridos, acrescentei o módulo datetime ao código. Para cada retorno mostrado na tela, é exibida a hora e a data. Se o cliente exceder o número de saques no dia, ele receberá uma mensagem de quando poderá realizar novos saques.
Também adicionei a listagem de contas, que foi mostrada pelo Prof. Guilherme. Achei bastante interessante e acabei implementando-a no meu código.
