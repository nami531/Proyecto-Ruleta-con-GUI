import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from Ruleta import Ruleta

class VentanaPremio:

    labels : list[Label]
    inputs : list[EntradasTexto]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.bienvenida = Label(250,150, self.vista.bienvenida(), 40, (0,0,0)) 

        
        self.x_botones = 50
        self.tamanho_botones = 120
        self.margen = 150

         
        self.caida = Label(100, 200, self.vista.caer_en(), 24,(0,0,0))
        
        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)
       
        
    

    def ejecutar(self, puntero, ruleta: Ruleta):
        self.puntero = puntero
        self.ruleta = ruleta
        siguiente = False
        self.premio = Label(100, 250, self.vista.mostrar_premio(self.puntero, self.ruleta), 24, (0,0,0)) 
        self.labels = [self.caida, self.premio]

        while not siguiente:
            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()
            tiempo = int(pygame.time.get_ticks() / 1000) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True
                elif tiempo > 10: 
                    siguiente = True

            # Limpiar la pantalla con color blanco
            self.screen.fill((0, 0, 255))

            # Dibujar elementos en la pantalla
            for label in self.labels: 
                label.draw(self.screen)

            self.bsiguiente.draw(self.screen)
            self.bsiguiente.update(mouse_pos) 

            # Verificar y mostrar el texto "pierde turno" si es necesario
            if self.ruleta.devuelve_premio() == -1: 
                pierdeTurno = Label(100, 400, self.vista.decir_letra_pierdeTurno(), 24, (0,0,0))
                pierdeTurno.draw(self.screen)

            # Actualizar la pantalla
            pygame.display.flip()

        
 
if __name__ == "__main__":
    r1 = Ruleta()
    print(r1.devuelve_ruleta())
    pygame.init()
    ventana = VentanaPremio(800, 600)
    print(ventana.ejecutar(1, r1)) 