# Simulação de login e senha em um sistema

# and = verificar se duas ou mais condições correspondem

nome = input('Nome do Usuário: ')
senha = input('Digite a senha: ')

if nome == 'admin' and senha == '1234':
    print(f'Login realizado com sucesso')

else:
    print(f'Usuário ou senha incorreto')