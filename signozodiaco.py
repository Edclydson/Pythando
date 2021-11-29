while(True):
    dia = int(input("Qual o dia do seu aniversário? "))
    mes = int(input("Qual o mês do seu aniversário? "))
# CAPRICORNIO / AQUARIO
    if(mes == 1):
        if(dia > 0 and dia <= 20):
            print("Seu signo é Capricornio")
        elif(dia >= 21 and dia <= 31):
            print("Seu signo é Aquário")
        else:
            print("Houve um problema com a data informada.")
# AQUARIO / PEIXES
    elif(mes == 2):
        if(dia > 0 and dia <= 19):
            print("Seu signo é Aquário")
        elif(dia > 19 and dia <= 29):
            print("Seu signo é Peixes")
        elif(dia >= 30):
            print("O mês de Fevereiro tem no máximo 29 dias."
                  " Boa tentativa! kkkk")
            continue
        else:
            print("Houve um problema com a data informada.")
# PEIXES / ARIES
    elif(mes == 3):
        if(dia > 0 and dia <= 20):
            print("Seu signo é Peixes")
        elif(dia <= 31):
            print("Seu signo é Áries")
        else:
            print("Houve um problema com a data informada.")
# ARIES / TOURO
    elif(mes == 4):
        if(dia > 0 and dia <= 20):
            print("Seu signo é Áries")
        elif(dia <= 30):
            print("Seu signo é Touro")
        else:
            print("Houve um problema com a data informada.")

# TOURO / GEMEOS
    elif(mes == 5):
        if(dia > 0 and dia <= 20):
            print("Seu signo é Touro")
        elif(dia <= 31):
            print("Seu signo é Gemeos")
        else:
            print("Houve um problema com a data informada.")

# GEMEOS / CANCER
    elif(mes == 6):
        if(dia > 0 and dia <= 20):
            print("Seu signo é Gemeos")
        elif(dia <= 30):
            print("Seu signo é Cancer")
        else:
            print("Houve um problema com a data informada.")

# CANCER / LEAO
    elif(mes == 7):
        if(dia > 0 and dia <= 21):
            print("Seu signo é Cancer")
        elif(dia <= 31):
            print("Seu signo é Leão")
        else:
            print("Houve um problema com a data informada.")

# LEAO / VIRGEM
    elif(mes == 8):
        if(dia > 0 and dia <= 22):
            print("Seu signo é Leão")
        elif(dia <= 31):
            print("Seu signo é Virgem")
        else:
            print("Houve um problema com a data informada.")

# VIRGEM / LIBRA
    elif(mes == 9):
        if(dia > 0 and dia <= 22):
            print("Seu signo é Virgem")
        elif(dia <= 30):
            print("Seu signo é Libra")
        else:
            print("Houve um problema com a data informada.")

# LIBRA / ESCORPIÃO
    elif(mes == 10):
        if(dia > 0 and dia <= 22):
            print("Seu signo é Libra")
        elif(dia <= 31):
            print("Seu signo é Escorpião")
        else:
            print("Houve um problema com a data informada.")

# ESCORPIÃO / SARGITÁRIO
    elif(mes == 11):
        if(dia > 0 and dia <= 21):
            print("Seu signo é Escorpião")
        elif(dia <= 30):
            print("Seu signo é Sargitário")
        else:
            print("Houve um problema com a data informada.")

# SARGITÁRIO / CAPRICÓRNIO
    elif(mes == 12):
        if(dia > 0 and dia <= 21):
            print("Seu signo é Sargitário")
        elif(dia <= 31):
            print("Seu signo é Capricórnio")
        else:
            print("Houve um problema com a data informada.")

    else:
        print("Digite um mês válido!")
        continue
# SAIR DO LOOP?
    q = int(input("\n Deseja saber mais algum signo? 1 - SIM ou 2 - NÃO:"))
    if(q == 1):
        continue
    else:
        break
