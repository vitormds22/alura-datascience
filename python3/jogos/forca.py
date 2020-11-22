def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    
    # for letra in palavra_secreta:
    #     print(letra)

    #enquanto(true)
    while(not enforcou and not acertou):
        chute = input('Chute uma letra: ')
        chute = chute.lower().strip()
        
        index = 0

        for letra in palavra_secreta:
            if(letra.lower() == chute):
                print('Encontrei a letra {} na posicao {}'.format(letra, index))
            index = index + 1

if(__name__ == "__main__"):
    jogar()