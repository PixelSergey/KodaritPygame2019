import pygame
import sys
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

pelaaja = pygame.image.load("pelaaja.png")

musta = (0, 0, 0)
koordinaatit = [0, 0]

while True:
    naytto.fill(musta)
    naytto.blit(pelaaja, koordinaatit)
    pygame.display.flip()
    
    # Tämä pätkä tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:  # Jos ruksia painettiin
            sys.exit()  # Sulje peli
        elif tapahtuma.type == pygame.KEYDOWN:         # Jos jotain nappia painettiin
            if tapahtuma.key == pygame.K_w:             # W = liiku ylös
                koordinaatit[1] = koordinaatit[1] - 10   # Ota koordinaatti Y:stä 10 pois
            elif tapahtuma.key == pygame.K_a:             # A = liiku vasemmalle
                koordinaatit[0] = koordinaatit[0] - 10   # Ota koordinaatti X:stä 10 pois
            elif tapahtuma.key == pygame.K_s:             # S = liiku alas
                koordinaatit[1] = koordinaatit[1] + 10   # Lisää koordinaatti Y:hyn 10
            elif tapahtuma.key == pygame.K_d:             # D = liiku oikealle
                koordinaatit[0] = koordinaatit[0] + 10   # Lisää koordinaatti X:ään 10
            
            if koordinaatit[0] < 0:  # Jos X-arvo on liian pieni
                koordinaatit[0] = 0  # Asetetaan se nollaan
            if koordinaatit[1] < 0:  # Jos Y-arvo on liian pieni
                koordinaatit[1] = 0  # Asetetaan se nollaan
            
            if koordinaatit[0] > koko[0]:  # Jos X-arvo on liian iso
                koordinaatit[0] = koko[0]  # Asetetaan se ruudun leveyteen
            if koordinaatit[1] > koko[1]:  # Jos Y-arvo on liian iso
                koordinaatit[1] = koko[1]  # Asetetaan se ruudun korkeuteen
                