import random


def play():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input("Defina o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        valor_informado = input("Digite um número entre 1 e 100: ")

        print("Voce digitou ", valor_informado)

        numero = int(valor_informado)

        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Voce errou! O seu chute foi maior que o numero secreto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif menor:
                print("Voce errou! O seu chute foi menor que o numero secreto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if __name__ == "__main__":
    play()
