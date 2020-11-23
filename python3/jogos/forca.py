def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana"
    letras_acertadas = ['_','_','_','_','_',''] 
        
    enforcou = False
    acertou = False
    
    while(not enforcou and not acertou):
        chute = input('Chute uma letra: ')
        chute = chute.lower().strip()
        
        index = 0

        for letra in palavra_secreta:
            if(letra.lower() == chute):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()