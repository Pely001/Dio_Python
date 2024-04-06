menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""
# Declarando as variáveis e Constantes
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

# Criando o laço de repetição para as operações
while True:
    
    opcao = input(menu)
    
    if opcao == "1":
       print("Deposito")
       valor = float(input("Informe o valor do deposito: "))
       
       if valor > 0:
           saldo += valor
           print("Deposito realizado. Seu saldo em conta é: {}".format(saldo))
       else:
           print("Falha na operação! Valor informado é inválido")
            
    elif opcao == "2":
       print("Saque")
       valor = float(input("Informe o valor do saque: "))
       
       if valor > saldo:
           print("Falha na operação! Saldo insuficiente.")
           
       elif valor > limite:
           print("Falha na operação! Valor excede o limite de saque. LIMITE: {}".format(limite))
           
       elif valor > 0:
           saldo -= valor
           numero_saques += 1
           print("Saque realizado no valor de R${:.2f}. Novo saldo em conta: R${:.2f}".format(valor, saldo))
           print("Número de saque no dia {}".format(numero_saques))
           if numero_saques > LIMITE_SAQUE:
               print("Falha na operação! Número de saques excedido. LIMITE DE SAQUES: {}".format(LIMITE_SAQUE))
           
            
    elif opcao == "3":
       print("Extrato")
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("==========================================")
        
    elif opcao == "4": 
        print("Obrigado por usar nossos serviços!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")