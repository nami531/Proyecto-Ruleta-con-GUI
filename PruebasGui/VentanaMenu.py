import pygame
import sys
from Jugador import Jugador
from Label import Label
from Vista import Vista
from Boton import Boton 

class VentanaMenu: 
    def __init__(self, width, height, jugador: Jugador):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.x_botones = 120
        self.tamanho_botones = 120
        self.margen = 150
        negro = (0,0,0)
        blanco= (255,255,255)
        random = (34,56,78)

        self.botones = []
       
        for i in range(len(self.vista.OPCIONES_TURNO_JUG)): 
            self.botones.append(Boton(self.x_botones+ self.margen * i, 200, self.tamanho_botones, 50, random, negro, self.vista.OPCIONES_TURNO_JUG[i], negro, 24, i ))

        self.turno = Label(90, 200, self.vista.turno(jugador), 24, negro)

        self.puntuacion = Label(90, 500, f"Puntuación: + {jugador.comprobar_puntuacion()}", 24, negro)

        self.labels = [self.turno, self.puntuacion]


    def ejecutar(self):
        accion = False
        while not accion:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for boton in self.botones: 
                    if boton.fue_presionado(mouse_pos, event) and not boton.eliminado:
                        accion = True
                        return boton.valor
               
                    
            for boton in self.botones:
                boton.update(mouse_pos) 

            

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            # Dibujar elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 

            for label in self.labels: 
                label.draw(self.screen)

#Esto será una imagen en un futuro no muy lejano
            # self.screen.blit(self.imagen, (250, 200))
           

            # Actualizar la pantalla
            pygame.display.flip()

if __name__ == "__main__":
    j1 = Jugador("Nadia")
    j2 = Jugador("Pepe")
    lista_jugadores = [j1, j2]
    pygame.init()
    ventana = VentanaMenu(800, 600, j1)
    print(ventana.ejecutar())

        
