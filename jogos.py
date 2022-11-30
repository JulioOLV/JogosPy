import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Iniciando jogo da Forca...")
        forca.play()
    elif jogo == 2:
        print("Iniciando jogo de Advinhacao")
        adivinhacao.play()


if __name__ == "__main__":
    escolhe_jogo()
