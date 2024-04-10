largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = (largura * altura)
rendimento = 2

litros_necessarios = area / rendimento

print(f'Cada litro de tinta pinta 2m², sendo assim você vai necessitar de {litros_necessarios} litros para sua area total de {area} metros quadrados')
