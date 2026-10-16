'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''

from random import randint
contador = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
pc = randint(0,10)
print(pc)
jogador = int(input('Qual é o seu palpite?'))
while jogador != pc:
    if jogador > pc:
        jogador = int(input('''Mais... Tente mais uma vez.
Qual é o seu palpite?'''))
        contador += 1
    elif jogador < pc:
        jogador = int(input('''Menos... Tente mais uma vez.
Qual é o seu palpite?'''))
        contador += 1
print('Acertou com {} tentativas. Parabéns!'.format(contador))
