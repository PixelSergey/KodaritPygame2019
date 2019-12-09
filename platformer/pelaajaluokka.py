import pygame

class Pelaaja():
    def __init__(self):
        self.x = 640
        self.y = 465
        self.nopeus = 5
        self.koko = 64
        self.laskin = 0
        self.saako_nousta = True
        self.animaation_osa = 0
        self.spritesheet_nimi = "pelaaja.png"
        self.spritesheet = None
        self.kuva = None

        self.lataa_spritesheet()
        self.lataa_kuva(0, 0)
    
    def lataa_spritesheet(self):
        self.spritesheet = pygame.image.load(self.spritesheet_nimi)

    def lataa_kuva(self, rivi, sarake):
        self.kuva = pygame.image.load("lapinakyva.png")
        aloitusY = rivi * self.koko
        aloitusX = sarake * self.koko
        lopetusY = aloitusY + self.koko
        lopetusX = aloitusX + self.koko
        #  Kopioidaan spritesheetistä koordinaattiin 0,0. Leikataan kuvasta vain lasketut koordinaatit.
        self.kuva.blit(self.spritesheet, (0, 0), (aloitusX, aloitusY, lopetusX, lopetusY))

    def animoi(self, animaation_numero):
        self.laskin += 1
        if self.laskin < 10:
            return
        
        self.laskin = 0
        self.animaation_osa += 1
        if self.animaation_osa > 3:
            self.animaation_osa = 0
        
        self.lataa_kuva(animaation_numero, self.animaation_osa)

    def piirra(self, mihin):
        mihin.blit(self.kuva, (self.x, self.y))

    def oikealle(self):
        self.x += self.nopeus

    def vasemmalle(self):
        self.x -= self.nopeus
    
    def hyppaa(self):
        self.y -= self.nopeus

    def putoa(self):
        self.y += self.nopeus
