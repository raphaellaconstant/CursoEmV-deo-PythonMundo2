'''Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.'''

continuar = 'S'
contador = acumulador = media = maior = menor = 0
while continuar != 'N':
    num = int(input('Digite um número:'))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    contador += 1
    acumulador += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = acumulador / contador
print('Você digitou {} números e a média foi {}.'.format(contador, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

