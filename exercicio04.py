
valor = int(input('Entre com um número inteiro e positivo --> '))
if valor < 0:
    print('O número deve ser inteiro e positivo')
else:
    fatorial = cont = 1
    while cont <= valor:
        fatorial *= cont # fatorial = fatorial * cont
        cont += 1  # cont = cont + 1
    print(f'{valor}! = {fatorial}')