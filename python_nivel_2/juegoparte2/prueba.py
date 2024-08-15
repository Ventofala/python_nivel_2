import pygame 
import sys 
from nave import Nave  
from laser import Bullet  
from alien import Alien

# pygame setup

class GalaxiWar:  
    def __init__(self):
        pygame.init()
        self.ancho = 900
        self.alto = 500
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Galaxi War")
        self.color = (230, 230, 230)  
        self.velocidad = 1 
        self.anchobala = 3
        self.altobala = 15
        self.colorbala = (255, 0 , 0) 
        self.nave = Nave(self) 
        self.bullets = pygame.sprite.Group() 
        self.aliens = pygame.sprite.Group()
        self.velocidad_Alien = 1.0
        self._create_fleet()

     

    def corre_juego(self): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = True
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = True
                    if event.key == pygame.K_SPACE: 
                        self._fire_bullet() 
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False 
            self.nave.mover()
            self.screen.fill(self.color)
            self.nave.corre() 
            self.bullets.update() 
            self.update_alien()


            for bullet in self.bullets.sprites(): 
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

            pygame.display.flip() 
            

    def _fire_bullet(self): 
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet) 

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availableSpace = self.ancho - (2 * alien_width)
        numerodeAliens = availableSpace // (2 * alien_width)
        nave_height = self.nave.rect.height
        availableSpacey = self.alto - (3 * alien_height) - nave_height
        numerodeFilas = availableSpacey // (2 * alien_height)

        for fila in range(numerodeFilas):
            for numeroAlien in range(numerodeAliens):
                self. _create_alien(numeroAlien, fila)

    def _create_alien(self, numeroAlien, fila):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * numeroAlien
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * fila
        self.aliens.add(alien)     

    def update_alien(self):
        self.aliens.update()    
        

                

if __name__ == "__main__":  
    a = GalaxiWar()
    a.corre_juego() 
