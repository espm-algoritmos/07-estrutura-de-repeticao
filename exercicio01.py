
inicio = int(input('Informe o valor inicial --> '))
fim = int(input('Informe o valor final --> '))

if inicio >= fim:
    print('o valor inicial deve ser menor')
else:
    contador = inicio
    while contador <= fim:
        print(contador, end='  ')
        contador = contador + 1