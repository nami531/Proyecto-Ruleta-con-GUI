import pygame
import sys
import os
from pygame import Surface
from Boton import Boton
from Label import Label
from Vista import Vista
from Ruleta import Ruleta


class VentanaPremio:

    vista : Vista
    width : int
    height : int
    screen : Surface
    colores : dict[str, tuple[int,int,int]]
    fuente : int
    tamanho_botones : tuple[int,int]
    caida: Label
    pierdeTurno : Label
    bsiguiente : Boton
    imgPierdeTurno : Surface
    texto_premio : Label

    def __init__(self, width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.colores = { "fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }

        self.fuente = 35
        
        self.tamanho_botones = (100, 40) 
        self.margen = 275

        self.caida = Label(self.margen, 50, self.vista.caer_en(), self.fuente,self.colores["negro"])
        self.pierdeTurno = Label(125, 100, self.vista.decir_letra_pierdeTurno(), 24, self.colores["negro"])
        
        self.bsiguiente =  Boton(700, 530, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], 24)
        
        

    def ejecutar(self, puntero, ruleta: Ruleta, premio: int):

        texto_premio = self.vista.mostrar_premio(puntero, ruleta)

        self.texto_premio = Label(self.margen+75, 100, texto_premio, self.fuente, self.colores["negro"]) 
        
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.img = pygame.image.load(directorio_actual + f"\\Multimedia\\{texto_premio.capitalize()}.jpeg")
        self.img = pygame.transform.scale(self.img, (300,300))

        siguiente = False        
        while not siguiente:

            mouse_pos = pygame.mouse.get_pos()
            tiempo = int(pygame.time.get_ticks() / 1000) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True
            
            self.screen.fill(self.colores["fondo"])

            # Dibujar elementos en la pantalla    
            self.caida.draw(self.screen)

            if tiempo > 1: 
                if premio == -1: 
                    self.pierdeTurno.draw(self.screen)
                else: 
                    self.texto_premio.draw(self.screen)
                self.bsiguiente.draw(self.screen)
                self.screen.blit(self.img, (225, 250))
                
            self.bsiguiente.update(mouse_pos) 

            # Actualizar la pantalla
            pygame.display.flip()
        
 