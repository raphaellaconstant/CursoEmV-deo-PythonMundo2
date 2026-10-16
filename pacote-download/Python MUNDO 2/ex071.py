'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 20)
print('{:^20}'.format('BANCO DA MANON'))
print('=' * 20)
valor = int(input('Que valor você quer sacar? R$'))
total = valor

while True:


