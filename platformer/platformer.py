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
    if pelaaja.y < 465:  # Jos pelaaja on ilmassa
        pelaaja.animoi(3)
        if nappaimisto[pygame.K_SPACE] == True and pelaaja.y > 425 and pelaaja.saako_nousta == True:  # Joko mene ylös...
            pelaaja.hyppaa()
        else:  # Tai putoa alas.
            pelaaja.saako_nousta = False
            pelaaja.putoa()
    else:  # Muuten, jos pelaaja on maassa, se saa...
        pelaaja.saako_nousta = True                 # ...nousta...
        if nappaimisto[pygame.K_a] == True:         # ...liikkua vasemmalle...
            if pelaaja.x < -pelaaja.koko/2:
                pelaaja.x = 1280 - pelaaja.koko/2
            pelaaja.vasemmalle()
            pelaaja.animoi(2)
        elif nappaimisto[pygame.K_d] == True:       # ...liikkua oikealle...
            if pelaaja.x > 1280 - pelaaja.koko/2:
                pelaaja.x = -pelaaja.koko/2
            pelaaja.oikealle()
            pelaaja.animoi(1)
        elif nappaimisto[pygame.K_SPACE] == True:   # ...hypätä...
            pelaaja.hyppaa()
        else:                                       # ...ja seistä paikoillaan.
            pelaaja.animoi(0)

    naytto.fill([0,0,0])
    naytto.blit(tausta, (0,0))
    pelaaja.piirra(naytto)
    pygame.display.flip()