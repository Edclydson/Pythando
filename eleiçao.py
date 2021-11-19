candidatos = [['1', 'Joao', 0], ['2', 'Maria', 0],
              ['3', 'Oliveira', 0], ['4', 'Pedro', 0]]
vtnulo = 0  # variavel p contar votos nulos
vtbranco = 0  # variavel p contar votos brancos
c = 0
porcnull = 0.0  # variavel p percentual votos nulos
porcbranco = 0.0  # variavel p percentual votos branco
tot = 0  # variavel p contar total de votos


def voto(p=0):  # função voto
    esc = candidatos[p]
    esc[2] = esc[2] + 1
    print("--------------------")
    print("     F I M !")
    print("--------------------")
    candidatos[p] = esc  # computando voto na variavel candidatos
    print("\n\n\n\n\n\n\n")


def fim():  # função encerra votação
    print("--------------------")
    print("     F I M !")
    print("--------------------")
    print("\n\n\n")
    print(" EXIBINDO RESULTADO DA ELEIÇÃO \n")
    print("COD  |   NOME    |   VOTOS\n")
    for i in candidatos:  # percorre mostrando candidatos e votos
        print(*i, "\n", sep="    |    ")
    porcnull = float((100 * (vtnulo/tot)))  # % de votos nulos
    porcbranco = float((100 * (vtbranco/tot)))  # % de votos brancos
    print("Votos branco: ", vtbranco, "/", "%.2f" % porcbranco, "%",
          "  Votos Nulos: ", vtnulo, "/", "%.2f" % porcnull, "%")
    print("\n")


while(1 > 0):  # loop infinito p votação n acabar
    vt = input("Qual o seu voto: ")
    tot = tot + 1
    for c in candidatos:
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
        elif (vt == "0"):
            vtbranco = vtbranco + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            print("\n\n\n\n\n\n\n")
            break
        else:
            vtnulo = vtnulo + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            print("\n\n\n\n\n\n\n")
            break
    if (vt == "fim"):
        vtnulo = vtnulo - 1
        fim()
        break
