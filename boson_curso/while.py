#num = 1
#while(num <= 10):
#    print(num)
#    num += 1
#print('Fim do loop')

nome = None

while True:
    print('Digite seu nome, ou x para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem Vindo {nome}')
print('Fim do loop')    