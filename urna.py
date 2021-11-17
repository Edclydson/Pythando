#### AINDA EM DESENVOLVIMENTO ####
user_admin_login = 'root'
user_admin_password = 'toor'
print("B E M  V I N D O !\n")
print("O que gostaria de fazer? ")
while(0 < 1):
    op = input("\n1-Configuração 2-Iniciar uma votação  :\n")  # MENU INICIAL

    if(op == '1'):
        # LOGIN PARA ACESSAR CONFIG DA URNA
        while(0 < 1):

            login = input("Login: ")
            senha = input("Senha: ")
            if(login != user_admin_login and senha != user_admin_password):  # CASO LOGIN E SENHA ERRADOS
                print("Ops! Verifique o Login ou a senha e tente novamente!")
            elif(login == None and senha == None):  # CASO LOGIN E SENHA VAZIOS
                print("Ops! Verifique o Login ou a senha e tente novamente!")
            else:  # CASO TUDO TIVER OK
                print("Login efetuado com sucesso!")
                break
    # INICIAR UMA VOTAÇÃO
    elif(op == '2'):
        print("Informe quantos candidatos a eleição terá: \n")
        numcandidato = int(input(""))
    else:  # CASO ESCOLHA UMA OPÇÃO QUE NÃO EXISTA
        print("Por favor, escolha uma das opções apresentadas!")
        continue
