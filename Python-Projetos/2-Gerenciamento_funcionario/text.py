from funcionario import Funcionario, Diretor, Gerente

print("Escolha qual você deseja")
escolha = int(input("1- Funcionario | 2- Gerente | 3- Diretor | 4 - Sair "))
while escolha == 1 or escolha == 2 or escolha == 3:

    if escolha == 1:
        funcionario = Funcionario(str(input("Diga o nome do funcionario: ")),int(input("Diga a idade do funcionario: ")),float(input("Diga o salario do funcionario: ")))


    elif escolha == 2:
        gerente = Gerente(str(input("Diga o nome do gerente: ")), int(input("Diga a idade do gerente: ")),float(input("Diga o salario do gerente: ")),float(input("Diga o bonus que o gerente irá ganhar: ")))


    elif escolha == 3:
        director = Diretor(str(input("Diga o nome do diretor: ")), int(input("Diga a idade do diretor: ")), float(input("Diga o salario do diretor: ")), float(input("Diga o valor das ações que o diretor ganhou: ")))
        director.mostrar_info()

    elif escolha == 4:
        print("Retornando para o inicio")

    if escolha == 1:
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print("FUNCIONARIO")
        print("=-=-=-=-=-=-=-=-=-=-=-")
        funcionario.mostrar_info()

    elif escolha == 2:
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print("GERENTE")
        print("=-=-=-=-=-=-=-=-=-=-=-")
        gerente.mostrar_info()

    elif escolha == 3:
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print("DIRETOR")
        print("=-=-=-=-=-=-=-=-=-=-=-")
        director.mostrar_info()

    elif escolha == 4:
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print("FIM DO SERVIÇO")
        print("=-=-=-=-=-=-=-=-=-=-=-")

    print("Escolha qual você deseja")
    escolha = int(input("1- Funcionario | 2- Gerente | 3- Diretor | 4 - Sair"))