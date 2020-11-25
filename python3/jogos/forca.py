def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "maça".upper()
    letras_acertadas = ['_' for letra in palavra_secreta] 

    enforcou = False
    acertou = False
    erros = 6
    
    while (not enforcou and not acertou):
        chute = input('Chute uma letra: ')
        chute = chute.upper().strip()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(letra == chute):
                    letras_acertadas[index] = letra
                index += 1
        else:
            ##Se o chute não estiver dentro da palavra secreta, então sai adiciona mais um erro
            erros -= 1
            print('Ops, você errou! Faltam {} tentativas'.format(erros))

        ## Quando os erros atingirem o numero 6 a var enforcou se torna True consequentemente saindo do laço
        enforcou = erros == 0
        
        ## Quando o jogador acertou todas as letras
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        print('Você ganhou')
    else:
        print('Você perdeu')
        
    print('Fim do jogo!')
        

if(__name__ == "__main__"):
    jogar()