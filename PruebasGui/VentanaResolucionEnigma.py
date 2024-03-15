import pygame
import sys
from Boton import Boton
from Label import Label
from Vista import Vista
from Jugador import Jugador
from pygame import Surface
import os 

class VentanaResolucion:

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

    def __init__(self, width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.tamanho_imgs = (300, 300)
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
        self.__directorio = os.path.dirname(os.path.abspath(__file__))

        self.tipo_fuente = pygame.font.Font(None, 36)

        self.bsiguiente = Boton(710, 520, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
        
    @property
    def directorio(self): 
        return self.__directorio
    
    @directorio.setter
    def directorio(self, valor): 
        self.__directorio = self.__directorio

    def dibujar_aviso_ganador(self,jugador: Jugador): 
        sup_aviso = self.tipo_fuente.render(self.vista.panel_resuelto(), True, self.colores["negro"])
        rect_aviso = sup_aviso.get_rect(center = (125 + 500 // 2, 100 + 100 // 2))
        pygame.draw.rect(self.screen, self.colores["morado"], (125, 100, 500, 100))
        self.screen.blit(sup_aviso, rect_aviso)
        Label(250, 225, self.vista.has_ganado(jugador), self.fuente,self.colores["negro"]).draw(self.screen)
    
    def carga_img_trofeo(self): 
        self.imagen = pygame.image.load(self.directorio + "\\Multimedia\\trofeo.webp")
        self.imagen = pygame.transform.scale(self.imagen, (self.tamanho_imgs[0], self.tamanho_imgs[1]))


    def dibujar_aviso_perdedor(self): 
        sup_aviso = self.tipo_fuente.render(self.vista.no_resolviste_panel(), True, self.colores["negro"])
        rect_aviso = sup_aviso.get_rect(center = (100 + 500 // 2, 100 + 100 // 2))
        pygame.draw.rect(self.screen, self.colores["azul"], (100, 100, 500, 100))
        self.screen.blit(sup_aviso, rect_aviso)

    def carga_img_triste(self): 
        self.imagen = pygame.image.load(self.directorio + "\\Multimedia\\triste.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.tamanho_imgs[0], self.tamanho_imgs[1]))
    

    def ejecutar(self,jugador: Jugador,  resuelto: bool)-> None:

        siguiente = False
        while not siguiente:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True

            self.screen.fill(self.colores["fondo"])  # Limpiar la pantalla con color blanco
            
            if resuelto: 
                self.dibujar_aviso_ganador(jugador)
                self.carga_img_trofeo()
            else: 
                self.dibujar_aviso_perdedor()
                self.carga_img_triste()
            self.screen.blit(self.imagen, (225, 250))

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()