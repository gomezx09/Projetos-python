print('{:=^40}'.format('  Loja do gomezx  '))

preco = float(input('Preços das Compras R$ '))

print('''Forma de pagamento:
[1] Dinheiro (10% de desconto)
[2] Cartão
[3] Boleto (sem desconto)''')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:  # Pagamento à vista (dinheiro)
    total = preco - (preco * 10 / 100)
    print(f'Sua compra deu R${preco:.2f} e você terá 10% de desconto, que vai ficar R${total:.2f}.')

elif opcao == 2:  # Pagamento no cartão
    print('''Pagamento no cartão:
    [1] Débito (5% de desconto)
    [2] Crédito (sem descontos)
    [3] Parcelado no crédito''')

    op1 = int(input('Escolha uma opção: '))

    if op1 == 1:  # Débito (5% de desconto)
        total = preco - (preco * 5 / 100)
        print(f'Sua compra foi de R${preco:.2f} e você terá desconto de 5%, ficando por R${total:.2f}.')

    elif op1 == 2:  # Crédito à vista (sem desconto)
        total = preco
        print(f'Sua compra ficou R${total:.2f}.')

    elif op1 == 3:  # Parcelamento no crédito
        print('''Parcelamento disponível:
        [1] 2x sem juros
        [2] 3x ou mais com juros (20%)''')

        op2 = int(input('Escolha uma opção de parcelamento: '))

        if op2 == 1:  # Parcelado em 2x sem juros
            parcela = preco / 2
            total = preco
            print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')

        elif op2 == 2:  # Parcelado em 3x ou mais com juros
            totparc = int(input('Quantas parcelas? '))
            total = preco + (preco * 20 / 100)  # Aplicando 20% de juros
            parcela = total / totparc
            print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS, totalizando R${total:.2f}.')

        else:
            print('Opção inválida de parcelamento.')

elif opcao == 3:  # Pagamento no boleto
    total = preco
    print(f'Sua compra deu R${preco:.2f} e será paga no boleto sem desconto.')

else:
    total = preco
    print('Opção inválida! Escolha entre [1], [2] ou [3].')

# Exibição final do valor da compra
print(f'Sua compra de R${preco:.2f} vai custar R$ {total:.2f} no final.')
