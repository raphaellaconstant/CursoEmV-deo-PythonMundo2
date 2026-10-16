'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

contador2 = 0
contador3 = 0
for i in range(1,8):
    id = int(input('Em que ano a {}ª pessoa nasceu?'.format(i)))
    if id <= 2008:
        contador2 += 1
    elif id >2008:
        contador3 += 1
print('Ao todo, tivemos {} pessoas maiores de idade.'.format(contador2))
print('E também tivemos {} pessoas menores de idade.'.format(contador3))






