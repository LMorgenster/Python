#estoque.py

produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço: '))
quantidade = int(input('Digite a quantidade: '))
compra_total = preco * quantidade

#informar produto, preço e quantidade
print("produto = ", produto)
print("preço = ", preco)
print("quantidade = ", quantidade)
print("compra total = %.2f" % compra_total)
