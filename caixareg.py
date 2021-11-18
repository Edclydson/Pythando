'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro
que o cliente forneceu,
para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a
próxima compra.
A saída deve ser conforme o exemplo abaixo:
LOJAS TABAJARA
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
'''
contador = 1000
x = 1
compra = 0.0
print("LOJAS TABAJARA\n")
while(1 > 0):
    while(x < contador):

        preco = float(input("R$ "))
        print("Produto", x, ": R$ ", "%.2f" % preco)
        compra = float(compra + preco)
        if(preco == 0):
            print("Total: R$", "%.2f" % compra)
            break
        else:
            x = x+1
            continue
