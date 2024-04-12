def depositar(saldo, limite, extrato, numero_saques):
    print("Depósito")
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += "\nDepósito de R${:.2f}".format(valor)
        print("Depósito realizado. Seu saldo em conta é: {}".format(saldo))
    else:
        print("Falha na operação! Valor informado é inválido")

    return saldo, limite, extrato, numero_saques

def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUE):
    print("Saque")
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Falha na operação! Saldo insuficiente.")
    elif valor > limite:
        print("Falha na operação! Valor excede o limite de saque. LIMITE: {}".format(limite))
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\nSaque de R${valor:.2f}"
        print("Saque realizado no valor de R${:.2f}. Novo saldo em conta: R${:.2f}".format(valor, saldo))
        print("Número de saque no dia {}".format(numero_saques))
        if numero_saques > LIMITE_SAQUE:
            print("Falha na operação! Número de saques excedido. LIMITE DE SAQUES: {}".format(LIMITE_SAQUE))

    return saldo, extrato, numero_saques

def ver_extrato(saldo, extrato):
    print("Extrato")
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\nSaldo: R$ {:.2f}".format(saldo))
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = int(input("Informe o CPF (somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, Nº - Bairro - Cidade/ Sigla Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def cadastrar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta['agencia']}
            Conta:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Contas
[0] Sair

=>"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, limite, extrato, numero_saques = depositar(saldo, limite, extrato, numero_saques)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUE)
    elif opcao == "3":
        ver_extrato(saldo, extrato)
    elif opcao == "4":
        cadastrar_usuario(usuarios)
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == "6":
        listar_contas(contas) 
    elif opcao == "0":
        print("Obrigado por usar nossos serviços!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
