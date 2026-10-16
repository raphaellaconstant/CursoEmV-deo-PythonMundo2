'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Tirando {} e {}, a sua média é {:.1f}. Você está reprovado(a).'.format(nota1,nota2,media))
elif media >= 5.0 and media <= 6.9:
    print('Tirando {} e {}, a sua média é {:.1f}. Você está em recuperação.'.format(nota1,nota2,media))
else:
    print('Tirando {} e {}, a sua média é {:.1f}. Você foi aprovado(a).'.format(nota1,nota2,media))
