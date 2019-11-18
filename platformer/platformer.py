import pygame
import sys
import pelaajaluokka
pygame.init()

koko = (1280, 720)
naytto = pygame.display.set_mode(koko)

pelaaja = pelaajaluokka.Pelaaja()

while True:
    naytto.fill([0,0,0])
    pelaaja.piirra(naytto)

    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
        elif tapahtuma.type == pygame.KEYDOWN:         # Jos jotain nappia painettiin
            if tapahtuma.key == pygame.K_w:             # W = liiku ylös
                pass
            elif tapahtuma.key == pygame.K_a:             # A = liiku vasemmalle
                pelaaja.vasemmalle()
            elif tapahtuma.key == pygame.K_s:             # S = liiku alas
                pass
            elif tapahtuma.key == pygame.K_d:             # D = liiku oikealle
                pelaaja.oikealle()
    
    pygame.display.flip()