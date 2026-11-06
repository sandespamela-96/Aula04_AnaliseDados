#Atividade 04

#compra acima de 250 reais o sistema deve aplicar um desconto de 16%
#perguntar ao usuário o valor da compra, caso o valor seja maior que 250 reais: 
# aplicar um desconto de 16%; 
# exibir o valor final com o desconto aplicado; 
# caso contrário, exibir o valor original da compra (sem desconto)

#Entrada
valor_compra = float(input('Qual o valor da sua compra? '))

#Processamento
#Símbolos: > MAIOR < MENOR >= MAIOR OU IGUAL <= MENOR OU IGUAL == IGUAL
# if = primeira condição - elif = outra condição para testar - else = qualquer outro caso

#Não é o ideal colocar aqui:
#desconto = valor_compra * 0.16
#valor_final = valor_compra - desconto

#Saída

if valor_compra > 250:
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f'Desconto de R$ {desconto:.2f}, total a pagar: R$ {valor_final:.2f}')

else:
    print(f'Valor da compra: R$ {valor_compra:.2f}')