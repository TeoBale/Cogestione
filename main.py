import os
import random
import time

colori = "rgby"
sequenza = ""
punteggio = 0


while True:
    os.system("clear")
    punteggio += 1
    sequenza += random.choice(colori)

    for colore in sequenza:
        print(colore)
        time.sleep(1)
        os.system("clear")
        time.sleep(0.2)

    risposta = input("Ripeti -> ")
    if not risposta == sequenza:
        print(f"Hai sbagliato, sei arrivato a {punteggio - 1} punti")
        break
    else:
        print("Risposta esatta")

    time.sleep(1)
