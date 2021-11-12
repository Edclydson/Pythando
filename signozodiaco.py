while(0 < 1):
    dia = int(input("Qual o dia do seu aniversário? "))
    mes = int(input("Qual o mês do seu aniversário? "))
# CAPRICORNIO / AQUARIO
    if(mes == 1):
        if(dia <= 20):
            print("Seu signo é Capricornio")
        else:
            print("Seu signo é Aquário")
# AQUARIO / PEIXES
    elif(mes == 2):
        if(dia <= 19):
            print("Seu signo é Aquário")
        else:
            print("Seu signo é Peixes")
# PEIXES / ARIES
    elif(mes == 3):
        if(dia <= 20):
            print("Seu signo é Peixes")
        else:
            print("Seu signo é Áries")
# ARIES / TOURO
    elif(mes == 4):
        if(dia <= 20):
            print("Seu signo é Áries")
        else:
            print("Seu signo é Touro")
# TOURO / GEMEOS
    elif(mes == 5):
        if(dia <= 20):
            print("Seu signo é Touro")
        else:
            print("Seu signo é Gemeos")
# GEMEOS / CANCER
    elif(mes == 6):
        if(dia <= 20):
            print("Seu signo é Gemeos")
        else:
            print("Seu signo é Cancer")
# CANCER / LEAO
    elif(mes == 7):
        if(dia <= 21):
            print("Seu signo é Cancer")
        else:
            print("Seu signo é Leão")
# LEAO / VIRGEM
    elif(mes == 8):
        if(dia <= 22):
            print("Seu signo é Leão")
        else:
            print("Seu signo é Virgem")
# VIRGEM / LIBRA
    elif(mes == 9):
        if(dia <= 22):
            print("Seu signo é Virgem")
        else:
            print("Seu signo é Libra")
# LIBRA / ESCORPIÃO
    elif(mes == 10):
        if(dia <= 22):
            print("Seu signo é Libra")
        else:
            print("Seu signo é Escorpião")
# ESCORPIÃO / SARGITÁRIO
    elif(mes == 11):
        if(dia <= 21):
            print("Seu signo é Escorpião")
        else:
            print("Seu signo é Sargitário")
# SARGITÁRIO / CAPRICÓRNIO
    elif(mes == 12):
        if(dia <= 21):
            print("Seu signo é Sargitário")
        else:
            print("Seu signo é Capricórnio")
# SAIR DO LOOP?
    q = int(input("\n Deseja saber mais algum signo? 1 - SIM ou 2 - NÃO:"))
    if(q == 1):
        continue
    else:
        break
