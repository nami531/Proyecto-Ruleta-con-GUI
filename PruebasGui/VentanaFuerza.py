import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from os import path
import os 
from Jugador import Jugador
import time
class VentanaFuerza:

    labels : list[Label]
    inputs : list[EntradasTexto]

    def __init__(self, width, height,jugador):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.__contador = 0 
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Concatenar la ruta del directorio actual con la ruta de la imagen

        # Cargar la imagen
        self.imagen = pygame.image.load(directorio_actual + "\\Multimedia\\ruleta.png")
        self.imagen = pygame.transform.scale(self.imagen, (300, 300))
        
        self.bempezar = Boton(0, 0, 100, 100, (0,0,0), (255,255,255), "Empezar", (233,243,1), 24)
        self.texto_fuerza = Label(100, 100, self.vista.aviso_medicion_fuerza(), 24,(0,0,0)) 
        self.texto_turno = Label(100, 50, self.vista.turno(jugador), 24, (0,0,0))
        self.labels = [self.texto_fuerza, self.texto_turno]
        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Siguiente", (255,255,255), 24)
        
        
        

    
    def girar_imagen(self, imagen, angulo):
        # Rotar la imagen
        imagen_girada = pygame.transform.rotate(imagen, angulo)
        return imagen_girada

    def ejecutar(self)->int:
        
       
        imagen_girada = self.imagen
        velocidad_rotacion = 1
        angulo = 0 
        siguiente = False
        self.__contador = 0 
        tiempo =  int(pygame.time.get_ticks() / 1000)   #Lo devuelve en milisegundos, por eso se divide entre 1000
    
        while not siguiente :
            
            mouse_pos = pygame.mouse.get_pos()
            tiempo2 = int(pygame.time.get_ticks() / 1000) 

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bempezar.fue_presionado(mouse_pos, event): 
                    self.bempezar.eliminado = True
                    self.__contador = 0
                    
                elif event.type == pygame.KEYDOWN and tiempo2 - tiempo <= 5 : 
                    self.__contador +=1 
                elif event.type == pygame.KEYUP:
                    print("Se ha levantado la tecla")
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            sup_imagen_girada = imagen_girada.get_rect()
            sup_imagen_girada.center = (self.width // 2, self.height // 2)  #Obtenemos la superficie de la imagen
            self.screen.blit(imagen_girada, sup_imagen_girada)

            angulo %= 360 

            self.fuerza = Label(100, 500 , f"¡Guau! Has presionado {self.__contador} veces, ¡increíble!", 24, (0,0,0))

            if tiempo2 - tiempo > 6 and tiempo2 - tiempo< 12: 
                angulo += velocidad_rotacion
                imagen_girada = self.girar_imagen(self.imagen, angulo)
                
            if tiempo2 - tiempo >= 5: 
                self.fuerza.draw(self.screen)
                
                
            self.texto_turno.draw(self.screen)  
            self.texto_fuerza.draw(self.screen)
            self.bempezar.draw(self.screen)  
            self.bsiguiente.draw(self.screen)
            self.bsiguiente.update(mouse_pos) 

            # Actualizar la pantalla
            pygame.display.flip()
       
        return self.__contador
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaFuerza(800, 600, j1)
    print(ventana.ejecutar())