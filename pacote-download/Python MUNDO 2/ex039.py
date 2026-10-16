'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano = int(input('Ano de nascimento:'))
hoje = 2026 - ano
if hoje > 18:
    print('Quem nasceu em {}, tem {} anos em 2026.'.format(ano,hoje))
    print('Você já deveria ter se alistado há {} anos.'.format(hoje - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
elif hoje < 18:
    print('Quem nasceu em {}, tem {} anos em 2026.'.format(ano,hoje))
    print('Ainda faltam {} anos para o alistamento.'.format(18 - hoje))
    print('Seu alistamento será em {}.'.format(ano + 18))
else:
    print('Quem nasceu em {}, tem {} anos em 2026.'.format(ano,hoje))
    print('Você tem que se alistar imediatamente!')


