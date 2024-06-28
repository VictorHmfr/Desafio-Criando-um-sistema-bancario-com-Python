# Função para todas as operações
# O nome da função, a lógica e o retorno são de escolha o desenvolvedor
# Saque - <keyword only>(*arg1,arg2,arg3) - Susgestão: saldo, valor, extrato, limite. numero_saques, limite_saques. Sugestão de retorno: saldo e extrato
# Depósito - <Positional only>(arg1,arg2,arg3/) - Sugestão de argumentos: saldo, valor, e extrato. Sugestão de retorno: saldo e extrato.
# Extrato - <Positional only e keyword only>. Argumentos posicionais: saldo. Argumentos nomeados: extrato.
# Duas novas funções: criar usuário, criar conta corrente.
# Criar usuário - Armazenar os usuários em uma lista, com valores: nome, data de nascimento, cpf e endereço.
# O endereço é uma string com formato: logradouro, numero da casa - bairro - cidade/sigla estado.
# Somentes os números do CPF devem ser armazenados, sem o formato de xxx.xxx.xxx-xx
# Não podemos cadastras dois usuários com o mesmo CPF. (só pode existir CPF repetido).
# Criar conta corrente - Armazenar as contas em uma lista. Uma conta é composta por: agência, número da conta e usuário.
# O número da conta é sequencial, inicianto em 1(ex: usuario se registra = conta 1, outro usuario se registra = conta 2...)
# O número da agência é fixo: "0001"
# O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
# Vincular um usuário a uma conta - Filtar a lista de usuários buscando o número do CPF informado para casa usuário da lista (ex: cpf do usuario = 232.452.425-95, cpf da conta = 232.452.425-95). 

usuarios = {}
usuario_logado = {}
contas = []
idUser = 0
numero_conta = 0

def validar_data_nascimento():
    while True:
        data_nascimento = input("Digite sua data de nascimento (DDMMYYYY) --> ")
        
        # Verificar se a entrada tem 8 caracteres no formator DDMMYYYY
        if len(data_nascimento) != 8:
            print("Insira uma data válida")
            continue

        # Separar dia, mês e ano
        dia = int(data_nascimento[:2])
        mes = int(data_nascimento[2:4])
        ano = int(data_nascimento[4:])

        # Função para verificar se o ano é bissexto
        def eh_bissexto(ano):
            return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

        ano_bissexto = eh_bissexto(ano)

        # Verificar se dia, mês e ano são válidos
        if dia < 1 or dia > 31:
            print("Insira um dia válido")
            continue
        if mes < 1 or mes > 12:
            print("Insira um mês válido")
            continue
        if ano < 0 or ano > 2006:
            print("Insira um ano válido")
            continue

        # Verificar a validade dos dias em cada mês
        if mes == 2:
            if ano_bissexto and dia > 29:
                print("Fevereiro em ano bissexto tem no máximo 29 dias")
                continue
            elif not ano_bissexto and dia > 28:
                print("Fevereiro em ano não bissexto tem no máximo 28 dias")
                continue
        elif mes in [4, 6, 9, 11] and dia > 30:
            print(f"O mês {mes} tem no máximo 30 dias")
            continue
        elif dia > 31:
            print(f"O mês {mes} tem no máximo 31 dias")
            continue

        break

    data_nascimento_formatada = '{dd:02d}/{MM:02d}/{yyyy}'.format(dd=dia, MM=mes, yyyy=ano)
    return data_nascimento_formatada

def validar_cpf():
    while(True):
        cpf = input("Digite seu cpf --> ")
        if len(cpf) != 11:
            print()
            print("Insira um CPF válido")
            continue
        else:
            for i in usuarios.values():
                if i['CPF'] == cpf:
                    print("CPF indisponível")
                continue
        break
    return cpf

def criar_usuario():
    global idUser
    usuarios_aux = {}
    nome = input("Digite o seu nome --> ")
    print()
    data_nascimento = validar_data_nascimento()

    print()
    cpf = validar_cpf()

    print()
    senha = input("Insira uma senha --> ")
    
    print()
    endereco = input("Digite seu endereco --> ")
    idUser += 1
    usuarios_aux[idUser] = {'Nome': nome, 'Data de Nascimento': data_nascimento, 'CPF': cpf, 'Senha': senha, 'Endereço': endereco}
    
    usuarios.update(usuarios_aux)
    usuario_logado = usuarios_aux
    return usuario_logado

def logar_usuario():

    cpf = input("Digite seu cpf --> ")
    if len(cpf) != 11:
        print()
        print("Insira um CPF válido")

    senha = input("Digite sua senha --> ")
    while(True):
        for i in usuarios.values():
            if i['CPF'] == cpf and i['Senha'] == senha:
                usuario_logado = i
                continue
            else: 
                "Usuário inválido"
        break

    return usuario_logado

def criar_conta(usuario_logado):
    global numero_conta
    usuario = usuario_logado
    agencia = '0001'
    conta_aux = {}
    numero_conta += 1
    conta_aux = { 'NumeroConta': numero_conta, 'agencia': agencia, 'usuario': usuario}
    contas.append(conta_aux)
    print("Conta criada com sucesso!")
    
    return usuarios, contas

def menu():
    menu = """
    ############-MENU-############
      
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Sair
      
    ############-MENU-############
      """
    opcao = int(input(menu))
    return opcao

def depositar(saldo, valor, extrato, /):
    
    valor = float(input("--- Informe o valor desejado para depósito --> "))
    if valor <= 0:
        print("Insira um valor válido!")
    else:
        saldo += valor
        extrato.append(f"Operação: [Depósito] // Valor: [R$ {valor:.2f}]")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques >= limite_saques:
        print("Limite de saque diário ultrapassado. Por favor tente outra hora!") 
    else:   
        valor = float(input("--- Informe o valor desejado para saque --> "))
        if valor > limite:
            print(f"Apenas saques menores que R$ {limite} são permitidos")
        elif valor > saldo:
            print("Saldo insufisciente!")
        else:
            saldo -= valor
            numero_saques += 1
            extrato.append(f"Operação: [Saque] // Valor: [R$ {valor:.2f}]")
    return saldo, extrato

def extrair(saldo, /, *, extrato):
    
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

def sistema_usuario_menu():
    
    menu= f"""
    ############-USUÁRIO-############ 
    
        [1] Criar usuário
        [2] Criar conta
        [3] Logar usuário
        [4] Sair
      
    ############-USUÁRIO-############
    """
    opcao = int(input(menu))

    return opcao

def sistema_usuario(usuario_logado):
    usuario = []

    while True:
        
        opcao = sistema_usuario_menu()

        if opcao == 1:

            usuario = criar_usuario()
            print(usuario)
            usuario_logado = usuario
            sistema(usuario_logado)
            
        elif opcao == 2:

            criar_conta(usuario_logado)

        elif opcao == 3:
        
            usuario_logado = logar_usuario()   
            sistema(usuario_logado) 

        elif opcao == 4:          
            break

        else: 
            print("Operação inválida. insira uma operação existente")

    return usuario_logado

def sistema(usuario_logado):

    saldo = 0
    valor = 0
    extrato = []
    limite = 500
    numero_saques = 0
    limite_saques = 3
    
    while True:

        opcao = menu()

        if opcao == 1:

            saldo, extrato = depositar(saldo, valor, extrato)
            print(saldo)
        
        elif opcao == 2:

            saldo, extrato = sacar(saldo= saldo,
                                    valor= valor,
                                    extrato= extrato,
                                    limite= limite,
                                    numero_saques= numero_saques, limite_saques= limite_saques)

        elif opcao == 3:
        
            extrair(saldo, extrato= extrato)

        elif opcao == 4:      
            print(usuarios)
            sistema_usuario(usuario_logado)

        else: 
            print("Operação inválida. insira uma operação existente")

sistema_usuario(usuario_logado)

