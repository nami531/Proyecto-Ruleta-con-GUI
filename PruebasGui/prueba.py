import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from os import path
import os 

class VentanaFuerza:

    labels: list[Label]
    inputs: list[EntradasTexto]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.__contador = 0 
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Concatenar la ruta del directorio actual con la ruta de la imagen
        ruta_imagen = os.path.join(directorio_actual, "Multimedia", "ruleta.png")

        # Cargar la imagen
        self.imagen = pygame.image.load(directorio_actual + "\\Multimedia\\ruleta.png")

        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)

    def girar_imagen(self, imagen, angulo):
        # Rotar la imagen
        imagen_girada = pygame.transform.rotate(imagen, angulo)
        return imagen_girada

    def ejecutar(self):
        imagen_girada = self.imagen
        siguiente = False
        angulo = 0
        velocidad_rotacion = 2  # Velocidad de rotación en grados por iteración
    
        while not siguiente:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    siguiente = True

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            # Girar la imagen
            imagen_girada = self.girar_imagen(self.imagen, angulo)

            # Obtener la superficie de la imagen girada
            sup_imagen_girada = imagen_girada.get_rect()
            sup_imagen_girada.center = (self.width // 2, self.height // 2)  # Centrar la imagen en la pantalla
            self.screen.blit(imagen_girada, sup_imagen_girada)  # Blit la imagen en la pantalla

            # Actualizar la pantalla
            pygame.display.flip()

            # Incrementar el ángulo de rotación para la próxima iteración
            angulo += velocidad_rotacion

            # Restringir el ángulo entre 0 y 360 grados
            angulo %= 360
 
if __name__ == "__main__":
    pygame.init()
    ventana = VentanaFuerza(800, 600)
    ventana.ejecutar()
