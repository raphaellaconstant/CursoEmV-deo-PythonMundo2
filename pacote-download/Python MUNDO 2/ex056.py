'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.'''

homem = ''
idadeh = 0
cont = 0
maior = 0
menor = 0
soma = 0
for n in range(1,5):
    print('{} {}ª PESSOA {}'.format('-' *4, n, '-' *4))
    nome = str(input('Nome:'))
    idade = float(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    soma += idade
    media = soma/4
    if n == 1:
        maior == idade
        menor == idade
    else:
        if idade > maior:
            maior = idade
            if sexo == 'M':
                homem = nome
                idadeh = idade
        if idade < menor:
            menor = idade
        if idade < 20:
            if sexo == 'F':
                cont += 1
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeh, homem))
print('A média de idade do grupo é de {} anos.'.format(media))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))



