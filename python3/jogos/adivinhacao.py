import random

print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

# numero_secreto = round(random.random() * 100) # Por padrão a função gera um número de 0.0 e 1.0. Dessa forma podemos ter problemas com as validações do for
numero_secreto = random.randrange(1, 101) # Dessa forma utilizamos uma função do módulo random para gerar um range automático para nós.
total_de_tentativas = 0
pontos = 1000
# print(numero_secreto) # Caso você queira colar hahah

print('Existem níveis de dificuldades, escolha e se divirta!', numero_secreto)
print('(1) Fácil \n(2) Médio \n(3) Difícil')

dificuldade = int(input('Escolha a dificuldade: '))
if(dificuldade == 1):
    total_de_tentativas = 20
elif(dificuldade == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(40 * '=')
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute_str = input('Digite um número entre 1 e 100:')
    print('Você digitou: ',chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Digite um número entre 1 e 100!')
        continue # Esse comando faz com que o looping volte a acontecer
    
    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print('Você acertou e fez um total de {} pontos'.format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute) # A pontuação varia da diferença entre o numero random e o chute do jogador
        pontos = pontos - pontos_perdidos

        if(chute_maior):
            print('Você errou! O chute foi maior que o número secreto!')
            if(rodada == total_de_tentativas):
                print('O número secreto era {} e você fez {}.'.format(numero_secreto, pontos))
        if(chute_menor):
            print('Você errou! O seu chute foi menor que o número secreto!')
            if(rodada == total_de_tentativas):
                print('O número secreto era {} e você fez {}.'.format(numero_secreto, pontos))

print(15 * '=')
print('Fim do jogo!')
print(15 * '=')
