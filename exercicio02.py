
contador = 1
maior = float('-inf')
while contador <= 5:
    valor = int(input('valor --> '))
    if valor > maior:
        maior = valor
    contador = contador + 1

print(f'maior valor: {maior}')