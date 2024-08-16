import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen

        self.image = pygame.image.load("juego/imagenes/naveenemiga3.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.juego = a_game #3

    def update(self):
        self.x += (self.juego.velocidad_Alien * self.juego.flota_direccion)   # 8
        self.rect.x = self.x

    def valida_bordes(self): #4
        screen_rect = self.screen.get_rect() #5 "Creamos el rectangulo de la ventana"
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: # 6
            return True #7  # Si nuestra parte der o izq del rectangulo del alien es >= al rectangulo der o izq de la ventana, que va a pasar?
