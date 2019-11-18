import pygame

class Pelaaja():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.nopeus = 10
        self.koko = 64
        self.spritesheet_nimi = "pelaaja.png"
        self.spritesheet = None
        self.kuva = None

        self.lataa_spritesheet()
        self.lataa_kuva()
    
    def lataa_spritesheet(self):
        self.spritesheet = pygame.image.load(self.spritesheet_nimi)

    def lataa_kuva(self):
        self.kuva = pygame.image.load("lapinakyva.png")
        #  Kopioi spritesheetistä koordinaattiin 0,0 koordinaateista 0,0 - 64,64 (eka kuva)
        self.kuva.blit(self.spritesheet, (0, 0), (0, 0, self.koko, self.koko))

    def piirra(self, mihin):
        mihin.blit(self.kuva, (self.x, self.y))

    def oikealle(self):
        self.x += self.nopeus

    def vasemmalle(self):
        self.x -= self.nopeus
