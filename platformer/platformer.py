import pygame
import sys
pygame.init()

koko = (1280, 720)
naytto = pygame.display.set_mode(koko)

while True:
    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
    
    pygame.display.flip()