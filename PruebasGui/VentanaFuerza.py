import pygame
import sys
from Boton import Boton
from Label import Label
from Vista import Vista
import os 
from Jugador import Jugador
from pygame import Surface

class VentanaFuerza:
    vista: Vista
    width : int
    height : int
    screen : Surface
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    contador : int
    imagen : Surface
    bempezar: Boton
    bsiguiente : Boton
    texto_fuerza: Label
    texto_turno: Label
    labels: list[Label]


    def __init__(self, width : int, height: int):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.tamanho_botones = (90, 40)
        self.margen = 150

        self.fuente = 24

        self.colores = {"fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }

        self.__contador = 0 
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        self.imagen = pygame.image.load(directorio_actual + "\\Multimedia\\ruleta.png")
        self.imagen = pygame.transform.scale(self.imagen, (300, 300))
        
        self.bempezar = Boton(350, 470, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Empezar", self.colores["negro"], self.fuente)
        self.texto_fuerza = Label(70, 100, self.vista.aviso_medicion_fuerza(), self.fuente, self.colores["negro"]) 
        
        self.bsiguiente = Boton(710, 520, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
                 
    def girar_imagen(self, imagen: Surface, angulo: int):
        imagen_girada = pygame.transform.rotate(imagen, angulo)
        return imagen_girada

    def ejecutar(self, jugador: Jugador)->int:
        
        self.texto_turno = Label(260, 50, self.vista.turno(jugador), self.fuente, self.colores["negro"])
        self.labels = [self.texto_fuerza, self.texto_turno]
        imagen_girada = self.imagen
        velocidad_rotacion = 1
        angulo = 0 
        siguiente = False
        self.__contador = 0 
        tiempo =  int(pygame.time.get_ticks() / 1000)   #Lo devuelve en milisegundos, por eso se divide entre 1000
    
        while not siguiente:
            
            mouse_pos = pygame.mouse.get_pos()
            tiempo2 = int(pygame.time.get_ticks() / 1000) 

            self.screen.fill(self.colores["fondo"]) 

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
                self.bsiguiente.draw(self.screen)
                
                
            self.texto_turno.draw(self.screen)  
            self.texto_fuerza.draw(self.screen)
            self.bempezar.draw(self.screen)  
            
            self.bsiguiente.update(mouse_pos) 

            # Actualizar la pantalla
            pygame.display.flip()
       
        return self.__contador
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaFuerza(800, 600, j1)
    print(ventana.ejecutar())