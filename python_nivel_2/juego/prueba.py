import pygame   #Primera parte
import sys   #Primera parte
from nave import Nave   #Segunda parte
from laser import Bullet   #Cuarta parte

# pygame setup

class GalaxiWar:   #Primera parte
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Galaxi War")
        self.color = (230, 230, 230)   #Primera parte
        self.velocidad = 1   #Cuarta parte
        self.anchobala = 3
        self.altobala = 15
        self.colorbala = (255, 0 , 0)    #Cuarta parte
        self.nave = Nave(self)   #Segunda parte
        self.bullets = pygame.sprite.Group()   #Cuarta parte
     

    def corre_juego(self):   #Primera parte
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:   #Tercera parte
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = True
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = True
                    if event.key == pygame.K_SPACE:   #Cuarta parte
                        self._fire_bullet()   #Cuarta parte
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False   #Tercera parte
            self.nave.mover()
            self.screen.fill(self.color)   #Primera parte
            self.nave.corre()   #Segunda parte
            self.bullets.update()   #Cuarta parte
            for bullet in self.bullets.sprites():   #Cuarta parte
                bullet.draw_bullet()   #Cuarta parte
            pygame.display.flip()   #Primera parte

    def _fire_bullet(self):   #Cuarta parte
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)   #Cuarta parte


if __name__ == "__main__":   #Primera parte
    a = GalaxiWar()
    a.corre_juego()   #Primera parte
