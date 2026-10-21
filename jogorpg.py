import random

while True:

    print("Bem vindo ao jogo RPG!")

    # ESCOLHA DE RODADAS
    while True:
        numrodadas = input(
            "Escolha o número de rodadas.\n"
            "1 - 5 RODADAS\n"
            "2 - 10 RODADAS\n"
        )

        if numrodadas == "1":
            rodadas = 5
            break
        elif numrodadas == "2":
            rodadas = 10
            break
        else:
            print("Selecione um número válido de rodadas.")

    print("O jogo começou!")

    # STATUS DO JOGADOR
    vida = 100
    cura = 30
    nivxp = 0

    # LOOP DE RODADAS
    for rodada in range(1, rodadas + 1):

        print("\nRodada", rodada)

        # GERAR INIMIGO
        numinimigo = random.randint(1, 100)

        if numinimigo <= 45:
            inimigo = "GOBLIN"
            inivida = 40
            danoinimigo = random.randint(15, 20)
            xp = random.randint(15, 20)

        elif numinimigo <= 90:
            inimigo = "ESQUELETO"
            inivida = 60
            danoinimigo = random.randint(20, 25)
            xp = random.randint(20, 30)

        else:
            inimigo = "DRAGÃO"
            inivida = 100
            danoinimigo = random.randint(25, 30)
            xp = random.randint(40, 60)

        print("Um", inimigo, "apareceu!")
        print("Vida do inimigo:", inivida, "\n")

        # COMBATE
        while inivida > 0 and vida > 0:

            # TURNO DO JOGADOR
            acao = input(
                f"Sua vida: {vida}\n"
                f"Sua Experiência: {nivxp}\n"
                "O que você quer fazer?\n"
                "1 - ATACAR\n"
                "2 - CURAR\n"
                "3 - FUGIR\n"
            )

            if acao == "1":

                dano = random.randint(9, 15)
                critico = random.randint(1, 100)

                if critico <= 20:
                    dano *= 2
                    print("Você acertou um ataque CRÍTICO!")

                inivida -= dano

                if inivida < 0:
                    inivida = 0

                print("\nVocê causou", dano, "de dano!\n")
                print("Vida do inimigo:", inivida)

                if inivida == 0:
                    print("Você derrotou o", inimigo)
                    print("Você ganhou", xp, "de Experiência!")
                    nivxp += xp
                    break

            elif acao == "2":

                vida += cura
                print("Você curou", cura, "de vida!")
                print("Sua vida agora é:", vida)

            elif acao == "3":

                print("Você fugiu!")
                break

            else:
                print("Escolha uma opção válida.")
                continue

            # TURNO DO INIMIGO
            vida -= danoinimigo

            if vida < 0:
                vida = 0

            print("\nO", inimigo, "atacou!")
            print("Você recebeu", danoinimigo, "de dano.")

            if vida == 0:
                print("\nVocê perdeu!\nSeu XP:", nivxp)
                break
        if vida == 0:
                break

    # JOGAR NOVAMENTE
    jogar = input("\nVocê quer jogar novamente?\n1 - SIM\n2 - NÃO\n")

    if jogar != "1":
        print("Obrigado por jogar!")
        break