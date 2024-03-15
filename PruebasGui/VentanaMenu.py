import pygame
import sys
from Jugador import Jugador
from Label import Label
from Vista import Vista
from Boton import Boton 
from pygame import Surface

class VentanaMenu: 
    vista: Vista
    width : int
    height : int
    screen : Surface
    x_botones : int
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    botones : list[Boton]
    turno : Label
    puntuacion : Label
    labels : list[Label]

    def __init__(self, width : int, height: int):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.x_botones = 150
        self.tamanho_botones = (200, 50)
        self.margen = 300

        self.fuente = 24

        self.colores = { "fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }
        self.botones = []
       
        for i in range(len(self.vista.OPCIONES_TURNO_JUG)): 
            if i >= 2:
                self.botones.append(Boton(self.x_botones+ self.margen * (i % 2), 300, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], self.vista.OPCIONES_TURNO_JUG[i], self.colores["negro"], self.fuente, i )) 
            else: 
                self.botones.append(Boton(self.x_botones+ self.margen * i, 200, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], self.vista.OPCIONES_TURNO_JUG[i], self.colores["negro"], self.fuente, i ))

       


    def ejecutar(self, jugador: Jugador)-> int | None:
        accion = False
        self.turno = Label(90, 100, self.vista.turno(jugador), self.fuente, self.colores["negro"])

        self.puntuacion = Label(600, 100, f"Puntuación: {jugador.comprobar_puntuacion()[0]}" , self.fuente, self.colores["negro"])
        self.labels = [self.turno, self.puntuacion]
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
                        return boton.valor +1
                                   
            for boton in self.botones:
                boton.update(mouse_pos)        

            self.screen.fill(self.colores["fondo"]) 

            # Dibujar elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 

            for label in self.labels: 
                label.draw(self.screen)           

            # Actualiza la pantalla
            pygame.display.flip()


        
