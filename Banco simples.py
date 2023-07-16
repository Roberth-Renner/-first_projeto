
menu = """
------------menu------------
 [a] sacar
 [b] depositar
 [c] extrato
 [d] sair
----------------------------
"""
saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
quant_SAQUES = 0
usuario = ""

while usuario != "d":
    
    usuario = input("\n Se quiser realizar uma interação, escolha no menu." + menu)

    if usuario == "a" : 

        valorSaque = float(input("\nDigite o valor de saque: "))

        if valorSaque <= limite and quant_SAQUES < LIMITE_SAQUES and saldo > 0 and valorSaque > 0:

            saldo = saldo - valorSaque
            quant_SAQUES += 1
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            print(f"\nSaque realizado com sucesso !")
            
        
        else:
           
            print("\nDesculpe interação nao permitida, fique atento ao limite de saques diarios, limite de valor de saque e ao seu saldo.")

    elif usuario == "b" :

        valorDeposito = float(input("Digite a o valor do depósito: "))

        if valorDeposito > 0:

            saldo = saldo + valorDeposito
            extrato += f"Deposito: R$ {valorDeposito:.2f}\n"
            print("\nDepósito realizado com sucesso !")
           

        else:

            print("\nHá algo errado, verifique se o valor que deseja depositar nao é negativo.")
            
    elif usuario == "c" :

        print("----------------EXTRATO----------------")
        print("Ainda não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------")

    elif usuario == "d" :

        print("\nTcahu, até a próxima!\n")    

    else:

        print("\nERRO 9747. Qualquer outro caractere que não esteja no menu causará este erro.")    
        
