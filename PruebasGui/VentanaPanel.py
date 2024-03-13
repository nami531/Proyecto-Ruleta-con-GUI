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
    # tipo_fuente : font 
    bsiguiente : Boton



    def __init__(self, width, height):
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

        self.tipo_fuente = pygame.font.Font(None, 36)
        
        self.bsiguiente = Boton(700, 530, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
        

 
    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self, enigma: str, pista: str, letras: list[str], vocales: list[str]) -> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma, pista, letras, vocales)
        
        # Calculamos el tamaño de cada rectángulo en función del tamaño de la ventana
        tamanho_rect = (self.width // 40, self.height // 15)
        
        margen_y = self.height // 6  # Margen entre filas
        margen_x = tamanho_rect[0] // 2  # Margen entre rectángulos dentro de una fila
        
        x = self.width // 10  # Posición inicial x
        y = self.height // 4  # Posición inicial y
        
        for i in range(len(enigma_cifrado)):
            letra = enigma_cifrado[i]
            if letra.lower() in letras:  # Calculamos j como el resto de la división de i por el número máximo de columnas
                self.dibujar_rect_Letra(letra, x, y, tamanho_rect)
                x += tamanho_rect[0] + margen_x  # Incrementamos la posición x con el tamaño del rectángulo y el margen
            
            elif letra == " ": 
                x += tamanho_rect[0] + margen_x  # Incrementamos la posición x con el tamaño del rectángulo y el margen
            else: 
                pygame.draw.rect(self.screen, self.colores["azul"], (x, y, tamanho_rect[0], tamanho_rect[1]))
                x += tamanho_rect[0] + margen_x  # Incrementamos la posición x con el tamaño del rectángulo y el margen
                
            # Verificamos si hemos llegado al final de la fila para saltar a la siguiente
            if x + tamanho_rect[0] > self.width - tamanho_rect[0]:
                x = self.width // 10  # Reiniciamos la posición x
                y += margen_y  # Incrementamos la posición y para la siguiente fila
                
        return y

    @staticmethod
    def filas(i: int, x: int , y: int, margen_y: int)->tuple[int,int]: 
        if i >= 14: 
            y += margen_y * (i//14) #  define la fila en la que estamos 
            x = 100
        return x, y
    
    def dibujar_rect_Letra(self, letra: str, x: int, y: int, tamanho: tuple[int, int])-> None: 
        rect = pygame.Rect(x, y, tamanho[0], tamanho[1])
        pygame.draw.rect(self.screen, self.colores["azul"], rect)

        sup_texto = self.tipo_fuente.render(letra, True, self.colores["negro"])
        rect_texto = sup_texto.get_rect(center=rect.center)
        self.screen.blit(sup_texto, rect_texto)
    

    def dibujar_pista(self, pista: str, y: int)->None: 
        superficie_pista = self.tipo_fuente.render(pista, True, self.colores["negro"])
        rect_pista = superficie_pista.get_rect()
        rect_pista.center = (100 + 630 // 2, y + 300 // 2)
        pygame.draw.rect(self.screen, self.colores["morado"], (100, y+100, 630, 100))
        self.screen.blit(superficie_pista, rect_pista)       

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

            ultimo_y = self.dibujar_rect_encriptados(enigma_juego, letra, letras, vocales )
            
            self.dibujar_pista(pista, ultimo_y)

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