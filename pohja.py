import pygame
import sys
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)
punainen = (255, 0 , 0)
keltainen = (255, 255, 0)
while True:
    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
    
    pygame.display.flip()