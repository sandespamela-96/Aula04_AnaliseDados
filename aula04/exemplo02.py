#Entrada
ano_nascimento = int(input('Informe o ano de nascimento: '))

#Processamento
idade = 2026 - ano_nascimento

#Saída
print(f'Você tem {idade} anos!')
if idade >= 18:
    print('Você é maior de idade')

else:
    print('você é menor de idade')