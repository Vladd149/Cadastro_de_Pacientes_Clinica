from funcoes import cadastrar_paciente, listar_pacientes, buscar_pacientes, exibir_estatisticas
from paciente import Paciente 

Pacientes = [] #lista de pacientes

def menu_principal():
    print("=================")
    print("\nSistema Clínica Vida+")
    print("\n=================")

    while True:
        print("\n--- OPÇÕES ---")
        print("1. Cadastrar Novo Paciente")
        print("2. Listar Todos os Pacientes")
        print("3. Buscar Paciente por Nome")
        print("4. Exibir Estatísticas")
        print("5. Sair do Programa")
        
        escolha = input("\n Escolha uma opção (1-5): ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas o número da opção.")
            continue # Volta para o topo do loop

        if escolha == 1:
            cadastrar_paciente(Pacientes)
            
        elif escolha == 2:
            listar_pacientes(Pacientes)
            
        elif escolha == 3:
            buscar_pacientes(Pacientes)
            
        elif escolha == 4:
            exibir_estatisticas(Pacientes)
            
        elif escolha == 5:
            print("\n Encerrando o sistema de gerenciamento. Até logo!")
            break
            
        else:
            print(f" Opção '{escolha}' não reconhecida. Tente um número de 1 a 5.")

# Ponto de entrada do programa: 
if __name__ == "__main__":
    menu_principal()

