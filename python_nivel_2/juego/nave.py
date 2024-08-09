import pygame

class Nave:
    def __init__(self, a_game):   #Segunda parte
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("juego/imagenes/naveespacial.png")
        self.rect = self.image.get_rect()   
        self.rect.midbottom = self.screen_rect.midbottom   #Segunda parte
        self.mover_derecha = False    #Tercera parte
        self.mover_izquierda = False    #Tercera parte

    def mover(self):
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.mover_izquierda and self.rect.left > self.screen_rect.left:
            self.rect.x -= 1

    def corre(self):   #Segunda  parte
        self.screen.blit(self.image, self.rect)