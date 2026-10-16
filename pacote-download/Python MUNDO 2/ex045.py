from random import randint
print('-'*30)
print('JOGANDO JOKENPO')
print('-'*30)
op = ('PEDRA', 'PAPEL', 'TESOURA')  # O professor não explicou o porque de parênteses e não colchetes, mas o gpt disse que é uma TUPLA.
pc = randint(0,2)
print('''Suas opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA''')
jo = int(input('Qual é a sua jogada?'))
print('-='*30)
print('''JO
KEN
PO!!!''')
print('-='*30)
print('O computador escolheu {}.'.format(op[pc]))
print('O jogador escolheu {}.'.format(op[jo]))
if pc == 0: #computador jogou PEDRA
    if jo == 0:
        print('EMPATE!')
    elif jo == 1:
        print('Jogador venceu!')
    elif jo == 2:
        print('Computador venceu!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif pc == 1:
    if jo == 0:
        print('Computador venceu!')
    elif jo == 1:
        print('EMPATE!')
    elif jo == 2:
        print('Jogador venceu!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif pc == 2:
    if jo == 0:
        print('Jogador venceu!')
    elif jo == 1:
        print('Computador venceu!')
    elif jo == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')




