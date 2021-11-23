'''
Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados.
'''
jogadores = []
vtnulo = 0  # variavel p contar votos nulos
vtbranco = 0  # variavel p contar votos brancos
c = 0
porcnull = 0.0  # variavel p percentual votos nulos
porcbranco = 0.0  # variavel p percentual votos branco
tot = 0  # variavel p contar total de votos

#adicionando os 23 jogadores na lista
for i in range(1,24):
    jogadores.append([str(i),0])
print (jogadores)

def voto(p=0):  # função voto
    esc = jogadores[p]
    esc[1] = esc[1] + 1
    print("-" * 20)
    print("     F I M !")
    print("-" * 20)
    jogadores[p] = esc  # computando voto na variavel candidatos
    print("\n\n\n\n\n\n\n")


def fim():  # função encerra votação
    print("-" * 20)
    print("     F I M !")
    print("-" * 20)
    print("\n\n\n")
    print(" EXIBINDO RESULTADO DA ELEIÇÃO \n")
    print("Nº JOGADOR  |   VOTOS    |   % VOTOS\n")
    for i in jogadores:  # percorre mostrando candidatos e votos
        print(*i, "\n", sep="    |    ")
        #FALTA EXIBIR % DE VOTOS DO JOGADOR
    porcnull = float((100 * (vtnulo/tot)))  # % de votos nulos
    porcbranco = float((100 * (vtbranco/tot)))  # % de votos brancos
    print("Votos branco: ", vtbranco, "/", "%.2f" % porcbranco, "%",
          "  Votos Nulos: ", vtnulo, "/", "%.2f" % porcnull, "%")
    print("\n")


while(1 > 0):  # loop infinito p votação n acabar
    vt = input("Qual o seu voto: ")
    tot = tot + 1
    for c in jogadores:
        if (vt == "1"):
            voto(p=0)
            break
        elif (vt == "2"):
            voto(p=1)
            break
        elif (vt == "3"):
            voto(p=2)
            break
        elif (vt == "4"):
            voto(p=3)
            break
        elif (vt == "5"):
            voto(p=4)
            break
        elif (vt == "6"):
            voto(p=5)
            break
        elif (vt == "7"):
            voto(p=6)
            break
        elif (vt == "8"):
            voto(p=7)
            break
        elif (vt == "9"):
            voto(p=8)
            break
        elif (vt == "10"):
            voto(p=9)
            break
        elif (vt == "11"):
            voto(p=10)
            break
        elif (vt == "12"):
            voto(p=11)
            break
        elif (vt == "13"):
            voto(p=12)
            break
        elif (vt == "14"):
            voto(p=13)
            break
        elif (vt == "15"):
            voto(p=14)
            break
        elif (vt == "16"):
            voto(p=15)
            break
        elif (vt == "17"):
            voto(p=16)
            break
        elif (vt == "18"):
            voto(p=17)
            break
        elif (vt == "19"):
            voto(p=18)
            break
        elif (vt == "20"):
            voto(p=19)
            break
        elif (vt == "21"):
            voto(p=20)
            break
        elif (vt == "22"):
            voto(p=21)
            break
        elif (vt == "23"):
            voto(p=22)
            break
        elif (vt == "0"):
            fim()
            break
        else:
            print("Voto inválido!")
            print("\n\n\n\n\n\n\n")
            continue
    