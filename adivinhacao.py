print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    valor_informado = input("Digite o seu numero: ")

    print("Voce digitou ", valor_informado)

    number = int(valor_informado)

    acertou = number == numero_secreto
    maior   = number > numero_secreto
    menor   = number < numero_secreto

    if(acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Voce errou! O seu chute foi menor que o numero secreto.")

    rodada = rodada + 1

print("Fim do jogo")