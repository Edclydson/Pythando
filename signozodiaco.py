dia = int(input("Qual o dia do seu aniversário? "))
mes = int(input("Qual o mês do seu aniversário? "))

if(mes == 1):
    if(dia <= 20):
        print("Seu signo é Capricornio")
    else:
        print("Seu signo é Aquário")
elif(mes == 2):
    if(dia <= 19):
        print("Seu signo é Aquário")
    else:
        print("Seu signo é Peixes")
elif(mes == 3):
    if(dia <= 20):
        print("Seu signo é Peixes")
    else:
        print("Seu signo é Áries")
elif(mes == 4):
    if(dia <= 20):
        print("Seu signo é Áries")
    else:
        print("Seu signo é Touro")
