import random

def play():
    print("*********************************")
    print("***Bem vindo no jogo da Forca!***")
    print("*********************************")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")


if __name__ == "__main__":
    play()
