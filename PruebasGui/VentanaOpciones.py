import pygame
from Vista import Vista
from Label import Label
from Jugador import Jugador
from Boton import Boton

class VentanaOpciones:

    vista : Vista

    def __init__(self, width, height, jugadores, i):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        margen = 50
        self.labels = []
        self.inputs = []
        self.jugadores = jugadores
        self.botones = []

        Label(100, 100, self.vista.turno(jugadores[i]), 24, (0,0,0))

        for i in range(len(self.vista.OPCIONES_TURNO_JUG)): 
            self.botones.append(Boton(100 + margen * i, 200, 100, 25, (12,23,43), (27,11,5), self.vista.OPCIONES_TURNO_JUG[i], (0,0,0), 24))

    
        

 