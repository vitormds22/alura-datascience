print('*********************************')
print('*******Escolha seu jogo !********')
print('*********************************')

print('(1) Forca  (2) Adivinhação')

jogo = int(input('Qual jogo você escolhe?: '))

if(jogo == 1):
    print('Jogando forca')
elif(jogo == 2):
    print('Jogando adivinhação')
else:
    print('Selecione um valor válido')