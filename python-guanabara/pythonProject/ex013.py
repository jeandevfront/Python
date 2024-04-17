salario = float(input('Digite seu salário'))
aumento = 15/100
v_aumento = salario * aumento
n_salario = v_aumento + salario

print(f"Seu salário é R${salario:.2f}, com um aumento de 15% temos R${n_salario:.2f}")