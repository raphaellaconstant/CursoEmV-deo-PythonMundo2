'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:'''

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
if num1 > num2:
    print('O primeiro valor é maior que o segundo.')
elif num2 > num1:
        print('O segundo valor é maior que o primeiro.')
else:
    print('Os dois valores são iguais.')