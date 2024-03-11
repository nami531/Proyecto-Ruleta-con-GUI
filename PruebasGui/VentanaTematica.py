import pygame
from Vista import Vista
from Jugador import Jugador
from Boton import Boton
import sys
from pygame import Surface

class VentanaTematica:

    vista: Vista
    width : int
    height : int
    screen : Surface
    x_botones : int
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        margen = 150
        self.botones = []

        self.x_botones = 100
        self.tamanho_botones = (120, 50)
        self.margen = 150

        self.fuente = 24

        self.colores = { "fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }

        for i in range(len(self.vista.tematicas_disponibles)): 
            if i >= len(self.vista.tematicas_disponibles) //2: 
                self.botones.append(Boton(100 + margen * (i-2), 300, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["morado"], self.colores["morado_hover"], self.vista.tematicas_disponibles[i], self.colores["negro"], self.fuente, i))
            else: 
                self.botones.append(Boton(100 + margen * i, 100, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["morado"], self.colores["morado_hover"], self.vista.tematicas_disponibles[i], self.colores["negro"], self.fuente, i))

    def ejecutar(self)-> int | None:
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
                        eleccion = True
                        return boton.valor
                    
            for boton in self.botones:
                boton.update(mouse_pos) 

            

            self.screen.fill(self.colores["fondo"])  # Limpiar la pantalla con color blanco

            # Dibujar elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 
           

            # Actualizar la pantalla
            pygame.display.flip()

if __name__ == "__main__":
    j1 = Jugador("Nadia")
    j2 = Jugador("Jorge")
    jugadores = [j1, j2]
    pygame.init()
    ventana = VentanaTematica(800, 600)
    print(ventana.ejecutar())
        

 