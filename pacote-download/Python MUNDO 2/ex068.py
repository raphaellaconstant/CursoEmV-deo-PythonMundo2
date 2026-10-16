''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=' * 20)
while True:
    num = int(input('Diga um valor:'))
    choice = str(input('PAR ou ÍMPAR? [P/I]')).strip().upper()[0]
    pc = randint(1,10)
    if (num + pc) % 2 == 0 and choice == 'P':
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {num + pc} deu PAR!')
        print('Você VENCEU! Vamos jogar novamente...')
    if (num + pc) % 2 != 0 and choice == 'I':
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {num + pc} deu ÍMPAR!')
        print('Você VENCEU! Vamos jogar novamente...')
    if (num + pc) % 2 == 0 and choice == 'I':
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {num + pc} deu PAR!')
        print('VOCÊ PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    if (num + pc) % 2 != 0 and choice == 'P':
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {num + pc} deu ÍMPAR!')
        print('VOCÊ PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    cont += 1









