real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 3.27
euro = real / 5.59
iene = real / 0.0342095
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} dólar, €{euro:.2f} euros, ¥{iene:.2f} iene japonês.')
