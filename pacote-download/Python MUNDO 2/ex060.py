'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''

fat = 1
num = int(input('Digite um número:'))
print('Calculando o {}! ='.format(num), end=' ')
for n in range(num, 0, -1):
    fat *= n
    print(('{} x' if n > 1 else '{} = {}').format(n, fat), end=' ')


