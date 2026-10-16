''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

'''print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
contador = contadorh = contadorm =  0
while True:
    idade = int(input('Idade:'))
    gen = str(input('Gênero: [M/F]')).strip().upper()[0]
    print('-' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if idade > 18:
        contador += 1
    if gen == 'M':
        contadorh += 1
    if gen == 'F' and idade < 20:
        contadorm += 1
    if continuar == 'N': #O break por ultimo para que ele possa verificar todos os if anteriores.
        break
print(f'Total de pessoas com mais de 18 anos: {contador}')
print(f'Ao todo temos {contadorh} homens cadastrados.')
print(f'E temos {contadorm} mulheres com menos de 20 anos.')'''

print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
contador = contadorh = contadorm =  0
while True:
    idade = int(input('Idade:'))
    gen = ' '   #PRESTAR ATENÇÃO. Aqui estava errando por não colocar o ESPAÇO entre as aspas.
    while gen not in 'MF':
        gen = str(input('Gênero: [M/F]')).strip().upper()[0]
        print('-' * 20)
    if idade > 18:
        contador += 1
    if gen == 'M':
        contadorh += 1
    if gen == 'F' and idade < 20:
        contadorm += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 20)
    if continuar == 'N':  # O break por ultimo para que ele possa verificar todos os if anteriores.
        break
print(f'Total de pessoas com mais de 18 anos: {contador}')
print(f'Ao todo temos {contadorh} homens cadastrados.')
print(f'E temos {contadorm} mulheres com menos de 20 anos.')




