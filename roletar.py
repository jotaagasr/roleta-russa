import random
import time

def roleta_russa():
    print("roleta russa")
    balas = [0, 0, 0, 0, 0, 1]  # 1 = bala, 0 = vazio
    random.shuffle(balas)

    input("Aperte ENTER pra girar o tambor...")
    time.sleep(0.5)
    print("Girando o tambor...")
    time.sleep(0.5)

    input("Aperte ENTER pra puxar o gatilho...")
    time.sleep(0.5)

    if balas.pop() == 1:
        print("BANG!")
        print("SE FUDEU MORREU")
    else:
        print("*click*")
        print("Segue a vida, por enquanto...")

    print("\nFim da rodada.")
    input("Pressione ENTER para jogar novamente...")
    roleta_russa() 
# Executar o jogo
roleta_russa()