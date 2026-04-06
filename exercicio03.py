
resposta = 's'

while resposta == 's' or resposta == 'S':
    valor = int(input('Informe um valor inteiro --> '))
    cont = 0
    while cont <= 10:
        resultado = valor * cont
        print(f'{valor} * {cont} = {resultado}')
        cont = cont + 1
    resposta = input('Deseja outra tabuada (s ou n)? ')