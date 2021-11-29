c = 0
vfcompra = 0.0
lista = ['Especificação', 'Cod', 'Preço']
cardapio = [['Cachorro Quente', '100', '1.20'],
            ['Bauru Simples', '101', '1.30'],
            ['Bauru com Ovo', '102', '1.50']]


def num100(preco, quant):
    print("\nProduto selecionado: \nCachorro Quente"
          "   R$", preco)
    print("Valor total do Cachorro Quente:")
    print("R$", "%.2f" % (preco*quant), "\n")


def num101(preco, quant):
    print("\nProduto selecionado: \nBauru Simples"
          "   R$", preco)
    print("Valor total do Bauru Simples:")
    print("R$", "%.2f" % (preco*quant), "\n")


def num102(preco, quant):
    print("\nProduto selecionado: \nBauru com Ovo"
          "   R$", preco)
    print("Valor total do Bauru com Ovo:")
    print("R$", "%.2f" % (preco*quant), "\n")


print("LANCHONETE TABAJARA\n")
while(True):
    while(True):
        print(lista[c], "   ", lista[c+1], "    ", lista[c+2], "\n")
        for s in cardapio:
            if(type(s) == list):
                print(*s, sep="     ")
                print("-"*35)
        cod = int(input("Digite o COD: "))
        if(cod == 100):
            preco = 1.20
            quant = int(input("Digite a Quantidade: "))
            num100(preco, quant)
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 101):
            preco = 1.30
            quant = int(input("Digite a Quantidade: "))
            num101(preco, quant)
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 102):
            preco = 1.50
            quant = int(input("Digite a Quantidade: "))
            num102(preco, quant)
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 0):
            print("-"*35)
            print("Total da compra: R$", "%.2f" % vfcompra, "\n")
            print("-"*35)
            break
        else:
            print("-"*35)
            print("\nProduto inválido! \n")
            print("-"*35)
            continue
