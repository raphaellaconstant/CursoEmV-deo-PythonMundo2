soma = contador = menor = totmil = 0
produtom = ' '
print('-' * 20)
print('MERCEARIA DA WAN')
print('-' * 20)
while True:
    produto = str(input('Nome do produto:')).strip()
    preço = float(input('Preço: R$'))
    contador += 1 #Tem que diferenciar do totmil
    soma += preço
    if preço > 1000: #Ifs e whiles na mesma indentação.
        totmil += 1 #Estava errando aqui ao usar o mesmo contador dele para o menor preço.
    if contador == 1: #Aqui eu estava ERRANDO ao colocar preço e não contador. É sobre o contador no índice 1 e não sobre preço valer 1.
        menor = preço
        produtom = produto
    else: #O ELSE é ligado DIRETAMENTE ao if na mesma indentação anterior à ele. Aqui ele significa que só pode ser uma coisa ou outra.
        if preço < menor: #Um if dentro do else. Se não tivesse o else ele executaria os dois if e o segundo não seria válido por causa do primeiro.
            menor = preço
            produtom = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${soma}.')  #O print vem na MESMA indentação do primeiro while.
print(f'Temos {totmil} produto custando mais de R$1000.')
print(f'O produto mais barato foi {produtom} que custa R${menor:.2f}.')