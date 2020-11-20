import forca
import adivinhacao

print('*********************************')
print('*******Escolha seu jogo !********')
print('*********************************')

print('(1) Forca  (2) Adivinhação')

jogo = int(input('Qual jogo você escolhe?: '))

if(jogo == 1):
    print('Jogando forca')
    forca.jogar()
elif(jogo == 2):
    print('===================')
    print('Jogando adivinhação')
    print('===================')

    adivinhacao.jogar()
else:
    print('Selecione um valor válido')