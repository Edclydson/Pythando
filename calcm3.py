# calculadora de metro cubico e capacidade
def caixa_retangular(altura, largura, comprimento):
    m3 = altura * largura * comprimento
    print("A capacidade é de:", "%.2f" %
          m3, "m³. Com capacidade para:", "%.0f" % (m3*1000), "L")


def caixa_cilindrica(altura, raio):
    m3 = altura * raio
    print("A capacidade é de:", "%.2f" %
          m3, "m³. Com capacidade para:", "%.0f" % (m3*1000), "L")


tpcaixa = input("Qual o tipo de caixa?\n 1-CILINDRICA ou 2-RETANGULAR\n")
if(tpcaixa == '1'):
    caixa_cilindrica(float(input("Digite a altura: ")),
                     float(input("Digite o valor do raio: ")))
elif(tpcaixa == '2'):
    caixa_retangular(float(input("Digite a altura: ")),
                     float(input("Digite a largura: ")),
                     float(input("Digite o comprimento: ")))
else:
    print("escolha uma opção válida! Tente novamente!")
