SAQUE_DIARIO = 3
numero_saque = 0
limite = 500.0
saldo = 2000.0
extrato = []

menu = """
    ############-MENU-############
      
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
      
    ############-MENU-############
      """

while True:

    opcao = int(input(menu))

    if opcao == 1:
        
        print()
        deposito = float(input("--- Informe o valor desejado para depósito --> "))
        if deposito < 0:
            print("Insira um valor válido!")
        else:
            saldo += deposito
            extrato.append(f"Operação: [Depósito] // Valor: [R$ {deposito:.2f}]")
        
    elif opcao == 2:
        
        print()
        if numero_saque >= 3:
            print("Limite de saque diário ultrapassado. Por favor tente outra hora!") 
        else:   
            saque = float(input("--- Informe o valor desejado para saque --> "))
            if saque > limite:
                print(f"Apenas saques menores que R$ {limite} são permitidos")
            elif saque > saldo:
                print("Saldo insufisciente!")
            else:
                saldo -= saque
                numero_saque += 1
                extrato.append(f"Operação: [Saque] // Valor: [R$ {saque:.2f}]")

    elif opcao == 3:
        
        print()
        if not extrato:
            print("Não foram realizadas movimentações")
            print(f"-- Saldo atual da conta -> R$ {saldo:.2f}")

        else:
            print("""
    ############-EXTRATO-############

                """)
            
            for lista in extrato:
                print("    " + lista)

            print(f"""
              
    -- Saldo atual da conta -> R$ {saldo:.2f}
                  
    ##########-EXTRATO-############
              """)

    elif opcao == 4:      
        break

    else: 
        print("Operação inválida. insira uma operação existente")

