def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana"
    palavra_secreta_tratada = palavra_secreta.lower()
    enforcou = False
    acertou = False
    
    # for letra in palavra_secreta:
    #     print(letra)

    #enquanto(true)
    while(not enforcou and not acertou):
        chute = input('Chute uma letra: ')
        chute_tratado = chute.lower().strip()
        
        index = 0

        for letra in palavra_secreta_tratada:
            if(letra == chute_tratado):
                print('Encontrei a letra {} na posicao {}'.format(letra, index))
            index = index + 1

if(__name__ == "__main__"):
    jogar()