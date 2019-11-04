import pygame
import sys
import random
import time
pygame.init()
pygame.font.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

esine = pygame.image.load("sieni.png")
esine = pygame.transform.scale(esine, [64, 64])
koordinaatit = [0, 0]

fontti = pygame.font.SysFont("Cambria Math", 30)
isofontti = pygame.font.SysFont("Cambria Math", 64)

pisteet = 0

alku = time.time()

musta = (0, 0, 0)
punainen = (255, 0 , 0)
keltainen = (255, 255, 0)

while True:
    naytto.fill(musta)
    naytto.blit(esine, koordinaatit)
    tekstikuva = fontti.render("Pisteet: " + str(pisteet), True, keltainen)
    naytto.blit(tekstikuva, (10,10))

    nykyhetki = time.time()
    peliaika = int(nykyhetki - alku)

    aikakuva = fontti.render("Peliaika: " + str(peliaika), True, keltainen)
    naytto.blit(aikakuva, (450, 10))

    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            if peliaika > 10:
                continue
            paikka = tapahtuma.pos
            # JOS klikkauksen x on suurempi kuin kuvan x JA klikkauksen x on pienempi kuin kuvan x plus leveys (sen oikea laita) JA ...
            if paikka[0] >= koordinaatit[0] and paikka[0] <= koordinaatit[0] + 64 and paikka[1] >= koordinaatit[1] and paikka[1] <= koordinaatit[1] + 64:
                koordinaatit[0] = random.randint(0, koko[0]-64)
                koordinaatit[1] = random.randint(0, koko[1]-64)
                pisteet += 1

    if peliaika > 10:
        naytto.fill(musta)
        peliloppukuva = isofontti.render("Peli loppui!", True, keltainen)
        klikkausnopeus = fontti.render("Nopeus: " + str(pisteet/10) + " klikkausta per sekunti", True, keltainen)
        naytto.blit(peliloppukuva, (175,200))
        naytto.blit(klikkausnopeus, (150,300))
        
    
    pygame.display.flip()