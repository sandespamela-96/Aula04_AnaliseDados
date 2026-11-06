#Bonus por desempenho de vendas
#Símbolos: > MAIOR < MENOR >= MAIOR OU IGUAL <= MENOR OU IGUAL == IGUAL
# if = primeira condição - elif = outra condição para testar - else = qualquer outro caso

venda = float(input('Qual o valor total da venda? '))
salario = float(input('Qual o valor do seu salário? '))

if venda >= 1000:
    bonus = salario + 150
    print(f'Vendas iguais ou superiores a R$ 1000,00: Valor total com bônus R$ {bonus:.2f}')

elif venda >= 500:
    bonus = salario + 75
    print(f'Vendas iguais ou superiores a R$ 500,00: Valor total com bônus R$ {bonus:.2f}')

else:
    print(f'Vendas inferiores a R$ 500,00: Salário sem bônus R$ {salario:.2f}')
