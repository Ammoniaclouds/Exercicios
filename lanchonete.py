
codigo = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade: '))

if codigo == 100:
    valor_unitario = float (1.20)
    produto = ('Cachorro Quente')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 101:
    valor_unitario = float (1.30)
    produto = ('Bauru Simples')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 102:
    valor_unitario = float (1.50)
    produto = ('Bauru com Ovo')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 103:
    valor_unitario = float (1.20)
    produto = ('Hamburger')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 104:
    valor_unitario = float (1.70)    
    produto = ('Cheeseburger')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 105:
    valor_unitario = float (2.20)    
    produto = ('Suco')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 106:
    valor_unitario = float (1.00)
    produto = ('Refrigerante')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
else:    
    print('Código Inválido')




