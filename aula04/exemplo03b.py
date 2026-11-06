#Entrada
pontos = int(input('Informe sua pontuação: '))

#Processamento
#Símbolos: > MAIOR < MENOR >= MAIOR OU IGUAL <= MENOR OU IGUAL == IGUAL
# if = primeira condição - elif = outra condição para testar - else = qualquer outro caso

if pontos >= 100:
    pontos = pontos + 10
    print(f'Excelente! Você tem {pontos} pontos agora!')

if pontos >= 50:
    pontos = pontos + 5
    print(f'Legal! Você tem {pontos} pontos agora!')

else:
    print(f'Não desanime, é apenas o começo! Você tem {pontos} pontos agora!')

#