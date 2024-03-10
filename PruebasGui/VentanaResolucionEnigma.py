import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from Jugador import Jugador

class VentanaResolucion:

    labels : list[Label]
    inputs : list[EntradasTexto]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.font = pygame.font.Font(None, 36)
        self.x_botones = 50
        self.tamanho_botones = 120
        self.margen = 150

        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)
                    
    def ejecutar(self,jugador,  resuelto):

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
            
            if resuelto: 
                sup_aviso = self.font.render(self.vista.panel_resuelto(), True, (255,255,255))
                rect_aviso = sup_aviso.get_rect()
                rect_aviso.center = (100 + 500 // 2, 100 + 100 // 2)
                pygame.draw.rect(self.screen, (0,0,0), (100, 100, 500, 100))
                self.screen.blit(sup_aviso, rect_aviso)
                Label(200, 200, self.vista.has_ganado(jugador), 24,(0,0,0)).draw(self.screen)
            else: 
                sup_aviso = self.font.render(self.vista.no_resolviste_panel(), True, (255,255,255))
                rect_aviso = sup_aviso.get_rect()
                rect_aviso.center = (100 + 500 // 2, 100 + 100 // 2)
                pygame.draw.rect(self.screen, (0,0,0), (100, 100, 500, 100))
                self.screen.blit(sup_aviso, rect_aviso)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaResolucion(800, 600)
    print(ventana.ejecutar(j1, False))