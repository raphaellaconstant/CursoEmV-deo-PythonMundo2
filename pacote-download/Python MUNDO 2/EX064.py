'''Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
acumulador = 0
contador = 0
while num != 999:
    num = int(input('Digite um número. Para parar, digite 999:'))
    acumulador += num
    contador += 1
    if num == 999:
        acumulador2 = acumulador - 999
        print('Você digitou {} números e a soma entre eles foi {}.'.format(contador - 1,acumulador2))

