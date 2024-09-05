
palavra = input('Insira uma palavra: ')

tam = len(palavra)
palavraInvertida = []

while(tam > 0 ):
    palavraInvertida.append(palavra[tam - 1])
    tam -= 1


palavraInvertida = ''.join(palavraInvertida)
print(palavraInvertida)