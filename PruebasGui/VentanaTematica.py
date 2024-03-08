import pygame
from Vista import Vista
from Label import Label
from Jugador import Jugador
from Boton import Boton
import sys

class VentanaTematica:

    vista : Vista

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        margen = 150
        self.labels = []
        self.inputs = []
        # self.jugadores = jugadores
        self.botones = []

        # Label(100, 100, self.vista.turno(jugadores[i]), 24, (0,0,0))
        # self.i = i 

        for i in range(len(self.vista.tematicas_disponibles)): 
            if i >= len(self.vista.tematicas_disponibles) //2: 
                self.botones.append(Boton(100 + margen * (i-2), 400, 100, 25, (12,23,43), (27,11,5), self.vista.tematicas_disponibles[i], (0,0,0), 24, i))
            else: 
                self.botones.append(Boton(100 + margen * i, 200, 100, 25, (12,23,43), (27,11,5), self.vista.tematicas_disponibles[i], (0,0,0), 24, i))

    def ejecutar(self)-> int:
        eleccion = False
        while not eleccion:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for boton in self.botones: 
                    if boton.fue_presionado(mouse_pos, event) and not boton.eliminado:
                        return boton.valor

                for entrada in self.inputs: 
                    entrada.update(mouse_pos, event)
                    
            for boton in self.botones:
                boton.update(mouse_pos) 

            

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            # Dibujar elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 

            for label in self.labels: 
                label.draw(self.screen)

            for entrada in self.inputs: 
                entrada.draw(self.screen)

           

            # Actualizar la pantalla
            pygame.display.flip()

if __name__ == "__main__":
    j1 = Jugador("Nadia")
    j2 = Jugador("Jorge")
    jugadores = [j1, j2]
    pygame.init()
    ventana = VentanaOpciones(800, 600)
    print(ventana.ejecutar())
        

 