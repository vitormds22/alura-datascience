print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 42
print('O tipo da variável é: ', type(numero_secreto))

chute = input('Digite o seu numero:')
print('O tipo do input é: ', type(chute))

print('Você digitou: ',chute)

if (numero_secreto == chute):
    print('Você acertou')
else:
    print('Você errou')