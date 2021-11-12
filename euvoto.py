idade = int(input("Qual a sua idade?"))
if(idade < 16):
    print("Não votante!")
elif(idade <= 18 or idade > 65):
    print("Seu voto é opcional!")
elif(idade >= 18 and idade <= 65):
    print("Seu voto é obrigatório!")
