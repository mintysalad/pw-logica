opcao = 0

while opcao != 4:
    print("\n==== Menu de Operações ====")
    print("1 - Mensagem")
    print("2 - Tabuada de um número")
    print("3 - Par ou Impar")
    print("4 - Sair")
    opcao = int(input("Escolher uma opção: "))

    if opcao == 1:
        print("\nSeja bem-vindo ao programa!")
    elif opcao == 3:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par!")
        else:
            print(f"O número {numero} é impar!")
    elif opcao == 2:
        numero = int(input("Digite um número: "))

        for i in range(1, 11):
            print(f"{numero} X {i} = {numero * i}")  
            
    elif opcao == 4:
        print("\nEncerrando programa... Até mais!")
    else:
        print("Opção inválida!")
    