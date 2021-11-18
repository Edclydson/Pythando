'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

# CRIAR DUAS VARIAVEIS SIM E NAO// PARA ARMAZENAR QUANTAS VEZES FORAM RESPONDIDAS COM SIM E NAO
# CRIAR UMA SEQUENCIA DE IF/ELSIF
# CRIAR ESTRUTURA DE DECISAO PARA ANALISAR RESPOSTAS E EMITIR UM RESULTADO// INOCENTE, SUSPEITO, CUMPLICE OU ASSASINO

sim = 0
nao = 0
print("Olá, sou o investigador Py. Gostaria de lhe fazer algumas perguntas...\n")
print("Peço para que seja objetivo nas suas respostas e responda somente sim ou não.")
print("Houve um crime na Rua *C*O*N*F*I*D*E*N*C*I*A*L")
# MORA PROX DO LOCAL
while(0 < 1):
    q1 = input("Você mora próximo desse local? 1 - SIM  2 - NÃO\n")
    if(q1 == "1"):
        sim = sim + 1
        break
    elif(q1 == "2"):
        nao = nao + 1
        break
    else:
        print("Por favor, se atenha a responder somente sim ou não!")
        continue
# PASSOU PERTO DO ENDEREÇO
while(0 < 1):
    q2 = input(
        "Você passou próximo a esse endereço recentemente?  1 - SIM  2 - NÃO\n")
    if(q2 == "1"):
        sim = sim + 1
        break
    elif(q2 == "2"):
        nao = nao + 1
        break
    else:
        print("Por favor, se atenha a responder somente sim ou não!")
        continue
# TRABALHOU COM A PESSOA
while(0 < 1):
    q3 = input("Você já trabalhou com essa pessoa? 1 - SIM  2 - NÃO\n")
    if(q3 == "1"):
        sim = sim + 1
        break
    elif(q3 == "2"):
        nao = nao + 1
        break
    else:
        print("Por favor, se atenha a responder somente sim ou não!")
        continue
# LIGOU PARA A PESSOA
while(0 < 1):
    q4 = input(
        "Você já recebeu alguma ligação ou ligou para essa pessoa? 1 - SIM  2 - NÃO\n")
    if(q4 == "1"):
        sim = sim + 1
        break
    elif(q4 == "2"):
        nao = nao + 1
        break
    else:
        print("\nPor favor, se atenha a responder sim ou não!")
        continue
# DEVIA PARA ALGUEM
while(0 < 1):
    q5 = input(
        "Você sabe dizer se essa pessoa devia para alguem ou ela tinha alguma pendência com você? 1 - SIM  2 - NÃO\n")
    if(q5 == "1"):
        sim = sim + 1
        break
    elif(q5 == "2"):
        nao = nao + 1
        break
    else:
        print("\nPor favor, se atenha a responder sim ou não!")
        continue
# FIM INTERROGATORIO

print("Muito obrigado pelas respostas e pelo seu tempo!\n")
print("RELATÓRIO FINAL\n \n")
print("INVESTIGAÇÃO DO CRIME *C*O*N*F*I*D*E*N*C*I*A*L \n")

if(sim < 2):
    print("O interrogado foi considerado inocente, por não apresentar ligações com a vítima!\n")
elif(sim == 2):
    print("O interrogado foi considerado suspeito e será convidado a prestar mais esclarecimentos!\n")
elif(sim < 4):
    print("O interrogado foi considerado cumplíce, será preso e ficará a disposição da justiça!\n")
elif(sim >= 5):
    print("O interrogado foi considerado o autor do crime e deve se julgado pelo crime cometido!\n")
