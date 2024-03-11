import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista

class VentanaPanel:

    labels : list[Label]
    inputs : list[EntradasTexto]

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

        self.font = pygame.font.Font(None, 36)
        
        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)
        

 
    
    def crear_rect_encriptados(self):
        enigma_cifrado = self.vista.mostrar_panel_cifrado(self.enigma,self.letra, self.letras, self.vocales)
        margen_y = 120
        x = 100
       
        tamanho = (20,50)
        for i in range(len(enigma_cifrado)):
            j = i % 9
            y = 200
            margen_x = 50
            x, y= self.filas(i,x, y , margen_y)
            letra = enigma_cifrado[i]
            if letra == "_": 
                pygame.draw.rect(self.screen, (0,0,0), (x + margen_x * j, y, tamanho[0], tamanho[1]))
            elif letra == " ": 
                margen_x += 10
            else: 
                text_surface = self.font.render(letra, True, (255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.center = (x + margen_x * j + tamanho[0] // 2, y + tamanho[1] // 2)
                pygame.draw.rect(self.screen, (0,0,0), (x + margen_x * j, y, tamanho[0], tamanho[1]))
                self.screen.blit(text_surface, text_rect)
        return y

    @staticmethod
    def filas(i,x , y, margen_y)->tuple[int,int]: 
        if i >= 9: 
            y += margen_y * (i//9) #  define la fila en la que estamos 
            x = 100
        return x, y
             

    def ejecutar(self, enigma_juego, pista, letras, vocales, letra=""):
        self.letras = letras
        self.vocales = vocales
       
        self.letra = letra
        self.enigma= enigma_juego
        self.pista = pista
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
            

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            y = self.crear_rect_encriptados()
            
            superficie_pista = self.font.render(self.pista, True, (255,255,255))
            rect_pista = superficie_pista.get_rect()
            rect_pista.center = (100 + 500 // 2, y + 100 // 2)
            pygame.draw.rect(self.screen, (0,0,0), (100, y+100, 500, 100))
            self.screen.blit(superficie_pista, rect_pista)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    pygame.init()
    letras = ["a", "h"]
    vocales = []
    ventana = VentanaPanel(800, 600,letras, vocales )
    print(ventana.ejecutar("Hola me llamo nadia", "Mi nombre"))