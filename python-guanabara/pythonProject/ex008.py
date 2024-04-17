m = float(input('Digite um valor em metros - '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(f'A medida de {m}m corresponde a')
print(f'{km}km\n{hm}hm\n{dam}dam')
print(f'{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
