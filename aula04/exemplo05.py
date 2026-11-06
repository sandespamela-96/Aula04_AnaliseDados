# Programa de fidelidade - brinde

#CONDIÇÕES: Compra maior que R$100 ou ser cliente frequente
#or = basta uma das condições ser verdadeira
#.lower() = se digitarem MAIUSCULO passa para minusculo
# [0] = Vai pegar só o primeiro caractere da palavra

valor_compra = float(input('Qual o valor total da compra? '))
frequencia_compra = input('Tem cadastro no programa de fidelidade? [S/N] ').lower()

#Símbolos: > MAIOR < MENOR >= MAIOR OU IGUAL <= MENOR OU IGUAL == IGUAL
# if = primeira condição - elif = outra condição para testar - else = qualquer outro caso

if valor_compra > 100 or frequencia_compra == 's':
    print(f'Parabéns! Você ganhou 100 reais de desconto!')

else:
    print('Não foi dessa vez :( cadastre-se no programa de fidelidade e garanta a próxima promoção!')

