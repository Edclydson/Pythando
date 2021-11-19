contador = 1000
x = 1
c = 0
vfcompra = 0.0
lista = ['Especificação', 'Cod', 'Preço']
cardapio = [['Cachorro Quente', '100', '1.20'],
            ['Bauru Simples', '101', '1.30'],
            ['Bauru com Ovo', '102', '1.50']]

print("LANCHONETE TABAJARA\n")

while(1 > 0):
    while(0 < 1):
        print(lista[c], "   ", lista[c+1], "    ", lista[c+2], "\n")
        for s in cardapio:
            if(type(s) == list):
                print(*s, sep="     ")
        cod = int(input("Digite o COD: "))
        if(cod == 100):
            preco = 1.20
            print("Produto selecionado: \nCachorro Quente"
                  "   R$:", preco)
            quant = int(input("Digite a Quantidade: "))
            print("Valor total do Cachorro Quente:")
            print("R$", "%.2f" % (preco*quant), "\n")
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 101):
            preco = 1.30
            print("Produto selecionado: \nBauru Simples"
                  "   R$:", preco)
            quant = int(input("Digite a Quantidade: "))
            print("Valor total do Bauru Simples:")
            print("R$", "%.2f" % (preco*quant), "\n")
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 102):
            preco = 1.50
            print("Produto selecionado: \nBauru com Ovo"
                  "   R$:", preco)
            quant = int(input("Digite a Quantidade: "))
            print("Valor total do Bauru com Ovo:")
            print("R$", "%.2f" % (preco*quant), "\n")
            vfcompra = float(vfcompra + preco * quant)
        elif(cod == 0):
            print("Total da compra: R$", "%.2f" % vfcompra, "\n")
            print("-----------------------------------")
            break
        else:
            print("-----------------------------------")
            print("\nProduto inválido! \n")
            print("-----------------------------------")
            continue
