# ideias: tornar os blocos de if/elif funções e só chamar quando entrar na condição
candidatos = [['1', 'Joao', 0], ['2', 'Maria', 0],
              ['3', 'Oliveira', 0], ['4', 'Pedro', 0]]
vtnulo = 0  # variavel p contar votos nulos
vtbranco = 0  # variavel p contar votos brancos
c = 0
porcnull = 0.0  # variavel p percentual votos nulos
porcbranco = 0.0  # variavel p percentual votos branco
tot = 0  # variavel p contar total de votos
while(1 > 0):  # loop infinito p votação n acabar
    vt = input("Qual o seu voto: ")
    tot = tot + 1
    for c in candidatos:
        if (vt == "1"):  # se votar 1
            esc = candidatos[0]
            esc[2] = esc[2] + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            candidatos[0] = esc  # computando voto na variavel candidatos
            print("\n\n\n\n\n\n\n")
            break
        elif (vt == "2"):
            esc = candidatos[1]
            esc[2] = esc[2] + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            candidatos[1] = esc
            print("\n\n\n\n\n\n\n")
            break
        elif (vt == "3"):
            esc = candidatos[2]
            esc[2] = esc[2] + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            candidatos[2] = esc
            print("\n\n\n\n\n\n\n")
            break
        elif (vt == "4"):
            esc = candidatos[3]
            esc[2] = esc[2] + 1
            print("--------------------")
            print("     F I M !")
            print("--------------------")
            candidatos[3] = esc
            print("\n\n\n\n\n\n\n")
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
        print("--------------------")
        print("     F I M !")
        print("--------------------")
        print("\n\n\n")
        print(" EXIBINDO RESULTADO DA ELEIÇÃO \n")
        break
print("COD  |   NOME    |   VOTOS\n")
for i in candidatos:
    print(*i, "\n", sep="    |    ")
porcnull = float((100 * (vtnulo/tot)))
porcbranco = float((100 * (vtbranco/tot)))
print("Votos branco: ", vtbranco, "/", "%.2f" % porcbranco, "%",
      "  Votos Nulos: ", vtnulo, "/", "%.2f" % porcnull, "%")
print("\n")
