from datetime import datetime, timedelta

data_hora_atual = datetime.now()
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
data_e_hora = data_hora_atual.strftime(mascara_ptbr)
proximo_saque_disponivel_str = (datetime.now() + timedelta(days=1)).strftime(mascara_ptbr)

def menu():
    menu = f"""
{data_e_hora}
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo Usuário
[c] Nova Conta
[l] Listar Contas
[q] Sair
=> """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0: # Primeira verificação para evitar depósitos de valores negativos conforme a instrução.
        saldo += valor # Se o valor for maior que 0, eu adiciono o valor (depósito) ao meu saldo em conta. Eu faço uma atribuição com uma operação de adição.
        extrato += f"\n{data_e_hora}\nDepósito: R$ {valor:.2f}\n" # Em seguida, é concatenado a string "Depósito: R$ + {valor:.2f}" que será colocada dentro do extrato para registrar o histórico.
        print(f"\n{data_e_hora}\nDepósito realizado com sucesso!")
    else: 
        print(f"\n{data_e_hora}\nA operação falhou! O valor informado é inválido.") # Caso o valor não seja maior que 0, será mostrada essa mensagem para o usuário.

    return saldo, extrato # Retorna o extrato atualizado, não um valor
         

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo # Verificação para checar se excedeu o saldo.
    excedeu_limite = valor > limite # Verificação para checar se excedeu o limite.
    excedeu_saques = numero_saques >= limite_saques # Verificação para checar se excedeu o limite de saque.
    #proximo_saque_disponivel_str = (datetime.now() + timedelta(days=1)).strftime(mascara_ptbr)  # Atualiza a data para o próximo saque
    
    if excedeu_saldo: 
            print(f"\n{data_e_hora}\nA operação falhou! Você não tem saldo suficiente.") # Caso tenha excedido o valor do saldo, será mostrado esta mensagem.

    elif excedeu_limite:
            print(f"\n{data_e_hora}\nA operação falhou! O valor do saque excedeu o limite.") # Caso tenha excedido o valor do limite (mesmo tendo saldo), será mostrado esta mensagem.

    elif excedeu_saques:
            print(f"\n{data_e_hora}\nA operação falhou! O número máximo de saques foi excedido.\nFaça um novo saque em: {proximo_saque_disponivel_str}\n") #!!! # Caso tenha excedido o valor de saques (mesmo tendo saldo), será mostrado esta mensagem.
        
    elif valor > 0: # Verificação para evitar saques de valores negativos.
        saldo -= valor # Se o valor para saque for válido e atender a todos os requisitos, o valor será debitado do saldo.
        extrato += f"\n{data_e_hora}\nSaque: R$ {valor:.2f}\n" # Em seguida, é concatenado a string Saque: R$ + {valor:.2f} que será colocada dentro do extrato para registrar o histórico.
        numero_saques += 1 # Incremento está variável para que os próximos saques não comecem de 0. Será contabilizado 1 + 1 = 2; no próximo 1 + 2 = 3. 
                           # Isso é feito para que a verificação LIMITE_SAQUES aconteça e ela barre o usuário.
        print(f"\n{data_e_hora}\nSaque realizado com sucesso!")
                             
    else:
        print(f"\n{data_e_hora}\nA operação falhou! O valor informado é inválido.") # Caso o valor não seja maior que 0, será mostrada essa mensagem para o usuário.

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(data_e_hora)
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # If ternário verificando se o extrato está vazio. 
                                                                                 # O extrato é do tipo string e começa vazio. 
                                                                                 # Se não foi feita nenhuma operação, é exibido o extrato com a mensagem na string.
                                                                                 # Se o extrato não está vazio, é exibido o valor dentro da variável extrato.
    print(f"\nSaldo: R$ {saldo:.2f}") # É exibido o valor do saldo em qualquer circunstância. 
    print("=========================================")


def criar_usuario(usuarios):
    cpf = input(f"\n{data_e_hora}\nInforme o seu CPF (somente números): ") # A primeira entrada será o CPF, porque logo em seguida, o usuário será filtrado por ele. Por se tratar de um número único, ele é perfeito para isso.
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: # Se for retornado um usuário com o mesmo número de CPF, irá mostrar a mensagem abaixo e retornará para a função principal main exibindo o menu novamente. 
         print(f"\n{data_e_hora}\n Já existe usuário com esse CPF!")
         return
    # Se o usuário não existir, serão solicitados os dados abaixo para o cadastro de novo usuário.
    nome = input(f"\n{data_e_hora}\nInforme o seu nome completo: ")
    data_nascimento = input(f"\n{data_e_hora}\nInforme a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input(f"\n{data_e_hora}\nInforme o seu endereço (Logadouro, Nº - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) # Com todas as informações atendidas, o usuário será adicionado a um dicionário (estrutura de chave:valor).

    print(f"\n{data_e_hora}\nUsuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios): # Compreensão da lista de usuarios filtrando por CPF.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Se o usuário percorrido tiver o mesmo número de CPF da lista usuarios, ele irá retornar o usuario dentro de uma nova lista usuarios_filtrados, se não for, a lista ficará vazia.
    return usuarios_filtrados[0] if usuarios_filtrados else None # Verficando se o usuarios_filtrados não é uma lista vazia, se não for, ele irá retornar o primeiro elemento. Isso porque você só irá achar um único usuário por CPF. Se não achar, ele irá retornar "None".
     

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input(f"\n{data_e_hora}\nInforme o CPF do usuário: ") # Saber com qual usuário a nova conta será vinculada.
    usuario = filtrar_usuario(cpf, usuarios) # Usando o mesmo filtro para verificar se o CPF do usuário já existe para que uma outra conta seja vinculada a ele.

    if usuario: 
         print(f"\n{data_e_hora}\nConta Criada com sucesso!") # Se o usuário for econtrado, a nova conta é criada.
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # Como a agência e o número da conta já vem por argumento, o usuario é vinculado.
    
    print(f"\n{data_e_hora}\nUsuário não encontrado, o fluxo de criação de conta está errado!") # Se não entrar no if, significa que o usuário não foi encontrado e essa mensagem é retornada.
    

def listar_contas(contas):
     for conta in contas:
         linha = f"""\n{data_e_hora}\n
              Agência: {conta['agencia']}
              C/C: {conta['numero_conta']}
              Titular: {conta['usuario']['nome']}
         """
         print((linha))


def main():
    LIMITE_SAQUES = 10
    AGENCIA = "0001"

    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
            opcao = menu()

            if opcao == "d":
                valor = float(input(f"\n{data_e_hora}\nInforme o valor do  depósito: ")) # É perguntado ao usuário qual será o valor do depósito.
            
                saldo, extrato = depositar(saldo, valor, extrato)
    
            elif opcao == "s":
                valor = float(input(f"\n{data_e_hora}\nInforme o valor do saque: ")) # É perguntado ao usuário qual será o valor do saque.
                
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,       
            )

            elif opcao == "e":
                 exibir_extrato(saldo, extrato=extrato)
            
            elif opcao == "u":
                 criar_usuario(usuarios)
            
            elif opcao == "c":
                numero_conta = len(contas) + 1 # O len conta os itens da lista e irá somar + 1. A primeira será 0 + 1, a segunda 1 + 1 e assim sucessivamente.
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta) # Adiciona a nova conta na lista.
                
            elif opcao == "l":
                 listar_contas(contas)

            elif opcao == "q": # Opção para sair.
                break

            else:
                print(f"\n{data_e_hora}\nOperação inválida, por favor, selecione novamente a operação desejada.") # Caso o usuário digite alguma operação desconhecida, será mostrada essa mensagem.

main() 
