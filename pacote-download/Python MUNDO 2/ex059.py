'''Crie um programa que leia dois valores e mostre um menu na
tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

escolha = 0
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
while escolha != 5:
    print('    [1] Somar')
    print('    [2] Multiplicar')
    print('    [3] Maior')
    print('    [4] Novos números')
    print('    [5] Sair do programa')
    escolha = int(input('>>>> Qual é a sua escolha?'))
    if escolha == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}.'.format(valor1, valor2, soma))
        print('-' * 20)
    elif escolha == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} e {} é {}.'.format(valor1, valor2,multiplicar))
        print('-' * 20)
    elif escolha == 3:
        if valor1 > valor2:
            print('Entre {} e {} o maior é {}.'.format(valor1,valor2,valor1))
            print('-' * 20)
        else:
            print('Entre {} e {} o maior número é {}.'.format(valor1, valor2, valor2))
            print('-' * 20)
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro valor:'))
        valor2 = int(input('Digite o segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    elif escolha == 0 or escolha > 5:
        print('Erro! Digite uma opção válida!')
print('Fim do programa!')
