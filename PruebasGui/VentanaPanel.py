import pygame
import sys
from Boton import Boton
from Vista import Vista
from pygame import Surface
from pygame import font 
import textwrap

class VentanaPanel:

    vista: Vista
    width : int
    height : int
    screen : Surface
    x_botones : int
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    # tipo_fuente : font 
    bsiguiente : Boton



    def __init__(self, width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.x_botones = 100
        self.tamanho_botones = (100, 40)
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

        self.tipo_fuente = pygame.font.Font(None, 24)
        
        self.bsiguiente = Boton(700, 530, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
        

 
    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self, enigma: str, pista: str, letras: list[str], vocales: list[str]) -> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma, pista, letras, vocales)
        
      
        tamanho_rect = (self.width // 40, self.height // 15)
        
        margen_y = self.height // 6  
        margen_x = tamanho_rect[0] // 2 
        
        x = self.width // 8  
        y = self.height // 4 + 30 
        
        for i in range(len(enigma_cifrado)):
            letra = enigma_cifrado[i]
            if letra.lower() in letras:  
                self.dibujar_rect_Letra(letra, x, y, tamanho_rect)
                x += tamanho_rect[0] + margen_x  # Movemos los rectángulos con el tamaño del rectángulo y el margen
            
            elif letra == " ": 
                x += tamanho_rect[0] + margen_x   # Incrementamos con tamaño del rectángulo y el margen
            else: 
                pygame.draw.rect(self.screen, self.colores["azul"], (x, y, tamanho_rect[0], tamanho_rect[1]))
                x += tamanho_rect[0] + margen_x 
                
            #comprobamos si hemos llegado al final de la fila para saltar a la siguiente
            if x + tamanho_rect[0] > self.width - tamanho_rect[0]:
                x = self.width // 10  # Se reinicia x
                y += margen_y  
                
        return y
    
    def dibujar_rect_Letra(self, letra: str, x: int, y: int, tamanho: tuple[int, int])-> None: 
        rect = pygame.Rect(x, y, tamanho[0], tamanho[1])
        pygame.draw.rect(self.screen, self.colores["azul"], rect)  #Primero se crean los rectángulos a los que va a pertenecer

        sup_texto = self.tipo_fuente.render(letra, True, self.colores["negro"])
        rect_texto = sup_texto.get_rect(center=rect.center)
        self.screen.blit(sup_texto, rect_texto)
    

    def genera_pista_adaptada(self, pista: str, rectangulo):   #rectangulo: Rect          
        pista = textwrap.wrap(pista, width=75)
        y = rectangulo.top
        for linea in pista:
            rendered_text = self.tipo_fuente.render(linea, True, self.colores["negro"])
            self.screen.blit(rendered_text, (rectangulo.left + 10, y + 10))
            y += rendered_text.get_height()
         
    def dibujar_pista(self, pista: str, ultimo_y: int): 
        rectangulo = pygame.draw.rect(self.screen, self.colores["morado"], (100, ultimo_y+100, 630, 100))
        self.genera_pista_adaptada(pista, rectangulo)    

    def ejecutar(self, enigma_juego: str, pista: str, letras: list[str], vocales: list[str], letra: str=""):
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
            

            self.screen.fill(self.colores["fondo"])

            ultimo_y = self.dibujar_rect_encriptados(enigma_juego, letra, letras, vocales )
            
            self.dibujar_pista(pista, ultimo_y)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualiza la pantalla
            pygame.display.flip()
 