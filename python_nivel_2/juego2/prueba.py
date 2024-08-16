import pygame 
import sys 
from nave import Nave  
from laser import Bullet  
from alien import Alien
from estadisticas import Estadisticas
from time import sleep # Pausar el juego

#Se marcaran los pasos nuevos con numeros, asi que si no consigues alguno busca en los demas archivos! 
#Del 1 al 18 programamos el movimiento de los enemigos
#Del 19 al 23 programamos las colisiones
#Del 24 al 27 programamos Musica y sonidos en este link pueden descargar https://y2mate.nu/Pio1/ y en este link lo convierten a WAV https://convertio.co/es/mp3-wav/
#Del 28 al programamos el Fin
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
        self.naves_restantes = 3   #30
        self.estadisticas = Estadisticas(self)    # 38
        self.nave = Nave(self) 
        self.bullets = pygame.sprite.Group() 
        self.aliens = pygame.sprite.Group()
        self.velocidad_Alien = 1.0
        self.flota_velocidad = 10   # 1
        self.flota_direccion = 1   #2
        self.juego_activado = True   # 49

        pygame.mixer.music.load("juego/musica/DBZ-Saga-de-Freezer-Soundtrack-14.wav")   # 24
        pygame.mixer.music.play(-1)   # 25
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
            if self.juego_activado:   # 51 hacer TAB para colocar las variables dentro
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
        self.valida_bordesFlota()   # 18
        self.aliens.update()    
        if not self.aliens:   # 21
            self.bullets.empty()   #22
            self._create_fleet()   # 23
        if pygame.sprite.spritecollideany(self.nave, self.aliens):   # 28
            self.nave_colisionada()   # 49  #print("Fin")   # 29 cambiar antes de terminar
    
    def nave_colisionada(self):   # 39
        if self.naves_restantes > 0:   # 50
            self.naves_restantes -= 1   # 40

            self.aliens.empty()   # 41
            self.bullets.empty()   # 42

            self._create_fleet()   # 43
            self.nave.centrar_nave()   # 44

            sleep(0.5)   # 45
        
        else:
            self.juego_activado = False   # 51

    def valida_bordesFlota(self):   # 9
        for alien in self.aliens.sprites():   # 10
            if alien.valida_bordes():   # 11
                self.cambia_direccion()   # 12
                break #13 # Break rompe el ciclo
    
    def cambia_direccion(self):   #14
        for alien in self.aliens.sprites():   #15
            alien.rect.y += self. flota_velocidad   #16
        self.flota_direccion *= -1   #17

                

if __name__ == "__main__":  
    a = GalaxiWar()
    a.corre_juego() 
