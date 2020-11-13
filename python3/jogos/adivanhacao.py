print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print(40 * '=')
    print('Tentativa ', rodada, 'de', total_de_tentativas)

    chute_str = input('Digite o seu numero:')
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
    
    rodada = rodada + 1

print(15 * '=')
print('Fim do jogo!')
print(15 * '=')
