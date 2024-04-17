n = int(input('Digite um número para ver sua tabuada: '))
c = 1

print('-'*12)
while c <= 10:
    res = n * c
    print(f'{n} x {c:>2} = {res}')
    c +=1
print('-'*12)