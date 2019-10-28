import pygame
import sys
import random
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

esine = pygame.image.load("sieni.png")
esine = pygame.transform.scale(esine, [64, 64])
koordinaatit = [0, 0]

pisteet = 0

musta = (0, 0, 0)
punainen = (255, 0 , 0)
keltainen = (255, 255, 0)
while True:
    naytto.fill(musta)
    naytto.blit(esine, koordinaatit)

    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            paikka = tapahtuma.pos
            # JOS klikkauksen x on suurempi kuin kuvan x JA klikkauksen x on pienempi kuin kuvan x plus leveys (sen oikea laita) JA ...
            if paikka[0] >= koordinaatit[0] and paikka[0] <= koordinaatit[0] + 64 and paikka[1] >= koordinaatit[1] and paikka[1] <= koordinaatit[1] + 64:
                koordinaatit[0] = random.randint(0, koko[0])
                koordinaatit[1] = random.randint(0, koko[1])
                pisteet += 1
                print(pisteet)

    pygame.display.flip()