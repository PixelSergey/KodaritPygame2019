import pygame
import sys
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)
punainen = (255, 0 , 0)
keltainen = (255, 255, 0)
while True:
    # Tämä pätkä piirtää "hymynaaman"
    naytto.fill(musta)
    pygame.draw.circle(naytto, keltainen, (112, 112), 50)
    pygame.draw.line(naytto, punainen, (100, 100), (100, 125), 10)
    pygame.draw.line(naytto, punainen, (125, 100), (125, 125), 10)
    pygame.draw.line(naytto, punainen, (90, 140), (130, 140), 10)
    pygame.display.flip()

    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
