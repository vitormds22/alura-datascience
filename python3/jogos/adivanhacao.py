print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 42
print('O tipo da variável é: ', type(numero_secreto))

chute_str = input('Digite o seu numero:')
print('O tipo do input é: ', type(chute_str))

print('Você digitou: ',chute_str)

chute = int(chute_str)
if (numero_secreto == chute):
    print('Você acertou')
else:
    print('Você errou')

print('Fim do jogo!')