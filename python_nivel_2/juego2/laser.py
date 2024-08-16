import pygame  
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.rect = pygame.Rect(0,0, a_game.anchobala, a_game.altobala)
        self.rect.midtop = a_game.nave.rect.midtop
        self.juego = a_game
        self.y = float(self.rect.y)
        self.sonido = pygame.mixer.Sound("juego/musica/efecto-de-sonido-teletransportacion-de-goku.mp3")   # 26
        self.sonido.play()   # 27

    def update(self):
        self.y -= self.juego.velocidad
        self.rect.y = self.y
        self.bullets = self.juego.bullets    # 19
        self.aliens = self.juego.aliens   # 20
        choques = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)    #21  #Esta linea funciona como un diccionario, donde key es laser y el value sera el alien. Los dos True funcionan para eliminar al key o al value solo cambiando a False. Si el primer True es cambiado a False, la bala no desaparecera al colisionar y eliminara a dos o mas enemigos dependiendo de tu flota.

        #Luego de crear esta linea prueba tu juego antes de pasar a la siguiente 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)  