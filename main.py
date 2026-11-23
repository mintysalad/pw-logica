while True:
    print("____ Calculadora ____\n" # \n pula linha para baixo
    "1- Somar\n"      
    "2- Subtrair\n"     
    "3- Multiplicar\n"
    "4- Sair\n")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Encerrando calculadora...")
        break
    if opcao == 1:
        print("Você escolheu somar.")
        break
    if opcao == 2:
        print("Você escolheu subtrair.")
        break
    elif opcao == 3:
        print("Você escolheu multiplicar.")
        break
    else:
        print("Opção inválida.")