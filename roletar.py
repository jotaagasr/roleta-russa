import random
from time import sleep

def roleta_russa():
    while True:
        try:
            print("\n🎯 Roleta Russa")

            balas = [0, 0, 0, 0, 0, 1]  # 1 = bala, 0 = vazio
            random.shuffle(balas)

            input("Aperte ENTER pra girar o tambor...")
            
            sleep(1)
            print("Girando o tambor...")
            sleep(1)

            input("Aperte ENTER pra puxar o gatilho...")
            sleep(1)

            if balas.pop() == 1:
                print("💥 BANG!")
                print("Você perdeu.")
            else:
                print("*click*")
                print("Segue a vida, por enquanto...")

            print("\nFim da rodada.")
            finalizando = input(
                "Pressione P para jogar novamente ou S para sair: "
            ).strip().upper()

            if finalizando == "S":
                print("Encerrando o jogo...")
                break

        except Exception as erro:
            print("Ocorreu um erro:", erro)

# Inicia o jogo
roleta_russa()
# Executar o jogo

roleta_russa()
