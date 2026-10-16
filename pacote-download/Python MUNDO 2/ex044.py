'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

preço = float(input('Digite o valor do(s) produto(s): R$'))
formas = int(input('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção?'''))
if formas == 1:
    print('Sua compra de R${:.2f} recebeu um desconto de 10%. O novo valor é: R${:.2f}'.format(preço,preço - (preço * 10/100)))
elif formas == 2:
    print('Sua compra de R${:.2f} recebeu um desconto de 5%. O novo valor é: R${:.2f}.'.format(preço,preço - (preço * 5/100)))
elif formas == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}.'.format(preço,preço/2))
elif formas == 4:
    preço2 = preço + (preço * 20/100)
    par = int(input('Quantas parcelas?'))
    print('Na sua compra de R${:.2f} foi aplicado 20% de juros. O novo valor é: R${:.2f}. Valor das parcelas: {}x de R${:.2f}.'.format(preço,preço2,par,(preço2/par)))

