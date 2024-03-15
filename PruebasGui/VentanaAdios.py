import pygame
import sys
from Boton import Boton
from Vista import Vista
from Jugador import Jugador
from pygame import Surface

class VentanaAdios:

    vista: Vista
    width : int
    height : int
    screen : Surface
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    margen : int
    # tipo_fuente : font
    bsiguiente : Boton

    def __init__(self,  width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.tamanho_botones = (90, 40)
        self.margen = 150

        self.fuente = 24

        self.colores = {"fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }

        self.tipo_fuente = pygame.font.Font(None, 36)
        self.bsiguiente = Boton(710, 520, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
                 
    def dibujar_aviso(self):
        sup_aviso = self.tipo_fuente.render(self.vista.decir_adios(), True, self.colores["negro"])
        rect_aviso = sup_aviso.get_rect()
        rect_aviso.center = (100 + 550 // 2, 100 + 100 // 2)
        pygame.draw.rect(self.screen, self.colores["azul"], (100, 100, 550, 100))
        self.screen.blit(sup_aviso, rect_aviso)

    def ejecutar(self):
        siguiente = False
        while not siguiente:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True

            self.screen.fill(self.colores["fondo"]) 

            self.dibujar_aviso()
            
            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 

            #Actualizar la pantalla
            pygame.display.flip()
 