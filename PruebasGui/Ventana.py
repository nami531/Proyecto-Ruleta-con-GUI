import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from os import path
import os
from pygame import Surface


class Ventana:

    vista: Vista
    width : int
    height : int
    screen : Surface
    labels : list[Label]
    inputs : list[EntradasTexto]
    x_botones : int
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    bienvenida : Label
    jugadores: Label
    b2jug: Boton
    b3jug: Boton
    b4jug: Boton
    b5jug: Boton
    benviar : Boton
    imagen : Surface

    def __init__(self, width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.x_botones = 100
        self.tamanho_botones = (100, 50)
        self.margen = 175

        self.fuente = 24

        self.colores = { "fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }

        self.bienvenida = Label(260,80, self.vista.bienvenida(), 40, (0,0,0)) 
        self.jugadores = Label(300, 450, "Nº Jugadores:", self.fuente, (0,0,0))

        self.b2jug = Boton(self.x_botones,500, self.tamanho_botones[0], self.tamanho_botones[1],self.colores["azul"], self.colores["azul_hover"], "2", self.colores["negro"], self.fuente, 2 )
        self.b3jug = Boton(self.x_botones + self.margen,500, self.tamanho_botones[0], self.tamanho_botones[1],self.colores["azul"], self.colores["azul_hover"], "3", self.colores["negro"], self.fuente, 3 )
        self.b4jug = Boton(self.x_botones + self.margen * 2,500, self.tamanho_botones[0], self.tamanho_botones[1],self.colores["azul"], self.colores["azul_hover"], "4", self.colores["negro"], self.fuente, 4 )
        self.b5jug = Boton(self.x_botones + self.margen * 3,500, self.tamanho_botones[0], self.tamanho_botones[1],self.colores["azul"], self.colores["azul_hover"], "5", self.colores["negro"], self.fuente, 5)
        self.benviar = Boton(420,430, self.tamanho_botones[0], self.tamanho_botones[1] , self.colores["azul"], self.colores["azul_hover"], "Enviar", self.colores["negro"], self.fuente)
        self.benviar.eliminado = True
        
        self.botones = [self.b2jug, self.b3jug, self.b4jug, self.b5jug, self.benviar]
        self.labels = [self.jugadores]
        self.inputs = []
        self.nombres_jug = []

        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.imagen = pygame.image.load(directorio_actual + "\\Multimedia\\dados.png")
        self.imagen = pygame.transform.scale(self.imagen, (250, 250))
    
    def crear_label(self, num_jug)->None:
        for i in range(num_jug): 
            self.labels.append(Label(self.x_botones + self.margen * i, 525, self.vista.pedir_nombre_jugador(i), self.fuente, (0,0,0)))

    def crear_inputs(self, num_jug)-> None: 
        for i in range(num_jug):
            self.inputs.append(EntradasTexto(self.x_botones + self.margen * i, 550, 100, 25, self.colores["negro"], self.colores["negro"], self.colores["blanco"] , self.fuente))
        self.benviar.eliminado = False
   
    def devolver_nombres(self)-> list[str]: 
        return self.nombres_jug

    def ejecutar(self)-> list[str]:
        nombres = False
        self.error = Label(0,0,"Todos los jugadores deben tener un nombre", self.fuente, self.colores["negro"])
        while not nombres:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for boton in self.botones: 
                    if boton.fue_presionado(mouse_pos, event) and not boton.eliminado:
                        num_jug = boton.valor
                        for boton in self.botones: 
                            boton.eliminar()
                        self.crear_label(num_jug)
                        self.crear_inputs(num_jug)
                if self.benviar.fue_presionado(mouse_pos, event): 
                    for entrada in self.inputs: 
                        if entrada.text != "": #Si no esta vacia, se añade
                            self.nombres_jug.append(entrada.text.capitalize())
                        else: 
                            self.labels.append(self.error)
                            self.nombres_jug = [] #Se tiene que reiniciar porque si no se sobreañadirían los nombres ya introducidos
                    if len(self.nombres_jug)<= 1: #Tiene que haber mín. 2 jugadores para iniciar la partida
                        self.labels.append(self.error)
                        self.nombres_jug = []
                    else: 
                        nombres = True
               
                for entrada in self.inputs: 
                    entrada.update(mouse_pos, event)

            for boton in self.botones:
                boton.update(mouse_pos) 

            self.screen.fill(self.colores["fondo"]) 

            # Dibujar los elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 

            for label in self.labels: 
                label.draw(self.screen)

            for entrada in self.inputs: 
                entrada.draw(self.screen)

            self.bienvenida.draw(self.screen)
            self.screen.blit(self.imagen, (275, 150))

            # Actualizar la pantalla
            pygame.display.flip()
        return self.nombres_jug
