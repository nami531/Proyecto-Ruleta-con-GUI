import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from pygame import Surface
from pygame import font 

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
    tipo_fuente : font
    bsiguiente : Boton



    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

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

        self.tipo_fuente = pygame.font.Font(None, 36)
        
        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)
        

 
    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self,enigma : str ,letra : str,letras : list[str],vocales : list[str])-> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma,letra, letras, vocales)
        margen_y = 120
        x = 100
       
        tamanho = (25,50)
        for i in range(len(enigma_cifrado)):
            j = i % 14 #Reinicia la fila en la que nos encontramos, de tal forma que i= columna, j= fila
            y = 200
            margen_x = 50
            x, y= self.filas(i,x, y , margen_y)
            letra = enigma_cifrado[i]
            if letra == "_": 
                pygame.draw.rect(self.screen, self.colores["azul"], (x + margen_x * j, y, tamanho[0], tamanho[1]))
            elif letra == " ": 
                margen_x += 10
            else: 
                sup_texto = self.tipo_fuente.render(letra, True, self.colores["negro"])
                rect_texto = sup_texto.get_rect()
                rect_texto.center = (x + margen_x * j + tamanho[0] // 2, y + tamanho[1] // 2)
                pygame.draw.rect(self.screen, self.colores["azul"], (x + margen_x * j, y, tamanho[0], tamanho[1]))
                self.screen.blit(sup_texto, rect_texto)
        return y

    @staticmethod
    def filas(i: int, x: int , y: int, margen_y: int)->tuple[int,int]: 
        if i >= 14: 
            y += margen_y * (i//14) #  define la fila en la que estamos 
            x = 100
        return x, y
             

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
            

            self.screen.fill(self.colores["fondo"])  # Limpiar la pantalla con color blanco

            y = self.dibujar_rect_encriptados(enigma_juego, letras, vocales, letra)
            
            superficie_pista = self.tipo_fuente.render(pista, True, self.colores["negro"])
            rect_pista = superficie_pista.get_rect()
            rect_pista.center = (100 + 500 // 2, y + 300 // 2)
            pygame.draw.rect(self.screen, self.colores["morado"], (100, y+100, 500, 100))
            self.screen.blit(superficie_pista, rect_pista)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualiza la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    pygame.init()
    letras = ["a", "h"]
    vocales = []
    ventana = VentanaPanel(800, 600)
    print(ventana.ejecutar("Hola me llamo nadia", "Mi nombre", ["t", "h", "n", "i"],[]))