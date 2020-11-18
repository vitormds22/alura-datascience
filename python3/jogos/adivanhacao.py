import random

print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

# numero_secreto = round(random.random() * 100) # Por padrão a função gera um número de 0.0 e 1.0. Dessa forma podemos ter problemas com as validações do for
numero_secreto = random.randrange(1, 101) # Dessa forma utilizamos uma função do módulo random para gerar um range automático para nós.
total_de_tentativas = 3

print(numero_secreto)

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
        print('Você acertou')
        break
    else:
        if(chute_maior):
            print('Você errou! O seu chute foi maior que o número secreto!')
        if(chute_menor):
            print('Você errou! O seu chute foi menor que o número secreto!')
    

print(15 * '=')
print('Fim do jogo!')
print(15 * '=')
