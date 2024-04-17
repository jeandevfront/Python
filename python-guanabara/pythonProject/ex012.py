preco_produto = float(input('Digite o preço do produto :'))
desconto = 10/100
des = int(desconto*100)
valor_desconto = preco_produto * desconto
preco_desconto = preco_produto - valor_desconto

print(f'O preço do produto é de R${preco_produto:.2f} reais.')
print(f'E com {des}% de desconto ele custa R${preco_desconto:.2f} reais.')
