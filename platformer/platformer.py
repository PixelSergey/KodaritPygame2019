import pygame
import sys
import pelaajaluokka
pygame.init()

koko = (1280, 720)
naytto = pygame.display.set_mode(koko)
tausta = pygame.image.load("tausta.png")
pelaaja = pelaajaluokka.Pelaaja()

while True:
    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli

    nappaimisto = pygame.key.get_pressed()  # Mitä nappeja on painettu?
    if nappaimisto[pygame.K_a] == True:
        pelaaja.vasemmalle()
        pelaaja.animoi(2)
    if nappaimisto[pygame.K_d] == True:
        pelaaja.oikealle()
        pelaaja.animoi(1)

    naytto.fill([0,0,0])
    naytto.blit(tausta, (0,0))
    pelaaja.piirra(naytto)
    pygame.display.flip()