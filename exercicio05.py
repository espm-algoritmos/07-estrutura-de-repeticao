n = int(input('Informe o valor de n positivo --> '))
y = 0
cont = 1
while cont <= n:
    y = y + 1/cont # y += 1/cont
    cont = cont + 1 # cont += 1
print(f'y = {y:.4f}')