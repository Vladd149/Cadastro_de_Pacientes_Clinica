from paciente import Paciente

def cadastrar_paciente(Pacientes):#funcionalidade de cadastro
    print("\nComeçando o cadastro de paciente, siga as instruções a seguir...\n")
    while True:
        nome = input("Digite o nome do paciente:")
        while True: # Loop interno para garantir a idade
            try:
                idade = int(input("Digite a idade do paciente: "))
                break  # SUCESSO: Define 'idade' e sai do loop interno
            except ValueError:
                print("Idade inválida. ...") # volta para o início do loop sem cadastrar

        telefone = input("Digite o telefone do paciente:")

        novo_paciente = Paciente (nome, idade, telefone)#cria novo objeto da classe
        Pacientes.append(novo_paciente)#coloca na lista 
        print(f"\nO paciente {nome} foi cadastrado!")

        while True:
            continuar_cadastro = input("Deseja cadastrar mais algum paciente? (SIM ou NÃO): ").lower()
            if continuar_cadastro == "não" or continuar_cadastro == "nao":
                print("\nCadastro de pacientes encerrado.")
                return

            elif continuar_cadastro == "sim":
                print("Continuando o cadastro...")
                break
            else:
                print("Resposta inválida. Por favor, responda 'SIM' ou 'NÃO'.")
                continue
            

def listar_pacientes(Pacientes):#funcionalidade de listar
    print("\n ---- TODOS OS PACIENTES CADASTRADOS: ----")
    if not Pacientes:#caso não tenha nenhum cadastro
        print("\nNenhum paciente cadastrado ainda!")
        return
    
    for paciente in Pacientes:#exibe todos os pacientes
        print(f"\n\nPaciente:{paciente.nome} \nIdade:{paciente.idade} \nTelefone:{paciente.telefone}")

def buscar_pacientes(Pacientes):#funcionalidade de buscar
    if not Pacientes:
        print ("\nNenhum paciente cadastrado!")
        return 

    while True:
        paciente_busca = input("\nDigite o nome do paciente que deseja buscar (ou digite SAIR para encerrar): ")
        if paciente_busca.lower() == "sair":
            print("\n Busca de pacientes encerrada.")
            break
        paciente_encontrado = None 

        for paciente in Pacientes:
            if paciente.nome.lower() == paciente_busca.lower(): #deixa a entrada do usuario em minusculo
                paciente_encontrado = paciente
                break

        if paciente_encontrado:
            print("\n--- Paciente Encontrado---")
            print(f"Paciente: {paciente_encontrado.nome}")
            print(f'Idade:{paciente_encontrado.idade}')
            print(f'Telefone:{paciente_encontrado.telefone}')
        else: 
            print(f'\nPaciente não encontrado!')

def exibir_estatisticas(Pacientes):#funcionalidade de estatísticas
    if not Pacientes:
        print("Nenhum paciente encontrado!")
        return
    
    print("\n----ESTATÍSTICAS----")

    total_pacientes = len(Pacientes)
    print(f"\nNúmero total de pacientes cadastrados:{total_pacientes}")
    #######

    idades = [paciente.idade for paciente in Pacientes]
    soma_idades = sum(idades)
    media_idades = soma_idades / total_pacientes
    print(f"Média de idade dos pacientes: {media_idades:.2f} anos.")
    ########

    paciente_mais_novo = min(Pacientes, key=lambda p: p.idade)
    paciente_mais_velho = max(Pacientes, key=lambda p: p.idade)

    print(f"Paciente mais novo :{paciente_mais_novo.nome} {paciente_mais_novo.idade} com anos.")
    print(f"Paciente mais velho:{paciente_mais_velho.nome} {paciente_mais_velho.idade} com anos. ")
    print("--------------------")