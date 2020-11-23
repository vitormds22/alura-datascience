def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana"
    letras_acertadas = ['_','_','_','_','_',''] 
        
    enforcou = False
    acertou = False
    erros = 0
    
    while (not enforcou and not acertou):
        chute = input('Chute uma letra: ')
        chute = chute.lower().strip()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(letra.lower() == chute):
                    letras_acertadas[index] = letra
                index += 1
        else:
            ##Se o chute não estiver dentro da palavra secreta, então sai adiciona mais um erro
            erros += 1
        ##Quando os erros atingirem o numero 6 a var enforcou se torna True consequentemente saindo do laço
        enforcou = erros == 6
        print(letras_acertadas)
    

    print('Fim do jogo!')
        

if(__name__ == "__main__"):
    jogar()