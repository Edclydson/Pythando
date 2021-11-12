dia = int(input("Qual o dia do seu aniversário? "))
mes = int(input("Qual o mês do seu aniversário? "))

#CAPRICORNIO / AQUARIO
if(mes == 1):
    if(dia <= 20):
        print("Seu signo é Capricornio")
    else:
        print("Seu signo é Aquário")
#AQUARIO / PEIXES
elif(mes == 2):
    if(dia <= 19):
        print("Seu signo é Aquário")
    else:
        print("Seu signo é Peixes")
#PEIXES / ARIES
elif(mes == 3):
    if(dia <= 20):
        print("Seu signo é Peixes")
    else:
        print("Seu signo é Áries")
#ARIES / TOURO
elif(mes == 4):
    if(dia <= 20):
        print("Seu signo é Áries")
    else:
        print("Seu signo é Touro")
#TOURO / GEMEOS
elif(mes == 5):
    if(dia <= 20):
        print("Seu signo é Touro")
    else:
        print("Seu signo é Gemeos")
#GEMEOS / CANCER
elif(mes == 6):
    if(dia <= 20):
        print("Seu signo é Gemeos")
    else:
        print("Seu signo é Cancer")
