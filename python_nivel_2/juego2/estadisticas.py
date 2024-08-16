import pygame   # 31

class Estadisticas:   # 32
    def __init__(self, a_game):   # 33
        self.juego = a_game   # 34
        self.reinicia()   # 35

    def reinicia(self):   # 36
        self.naves_restantes = self.juego.naves_restantes   # 37