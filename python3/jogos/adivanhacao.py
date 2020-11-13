print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 42
# print('O tipo da variável é: ', type(numero_secreto))

chute_str = input('Digite o seu numero:')
# print('O tipo do input é: ', type(chute_str))

print('Você digitou: ',chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if (acertou):
    print('Você acertou')
else:
    if(chute_maior):
        print('Você errou! O seu chute foi maior que o número secreto!')
    if(chute_menor):
        print('Você errou! O seu chute foi menor que o número secreto!')

print('Fim do jogo!')