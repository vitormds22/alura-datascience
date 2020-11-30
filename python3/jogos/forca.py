import random

def jogar():

    imprime_abertura()
    palavra_secreta = carrega_arquivo_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    while (not enforcou and not acertou):
        chute = chute_jogador()
        
        if(chute in palavra_secreta):
           marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            ##Se o chute não estiver dentro da palavra secreta, então sai adiciona mais um erro
            erros += 1
            desenha_forca(erros)

        ## Quando os erros atingirem o numero 6 a var enforcou se torna True consequentemente saindo do laço
        enforcou = erros == 7
        
        ## Quando o jogador acertou todas as letras
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)   

    print('Fim do jogo!')

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

def carrega_arquivo_palavras():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    num_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num_palavra].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def chute_jogador():
    chute = input('Chute uma letra: ')
    chute = chute.upper().strip()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(letra == chute):
            letras_acertadas[index] = letra
        index += 1
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()
