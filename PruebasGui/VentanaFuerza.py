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
    imagen_ruleta : Surface
    bempezar: Boton
    bsiguiente : Boton
    texto_fuerza: Label
    texto_turno: Label
    labels: list[Label]


    def __init__(self,  width: int = 800, height: int = 600):
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
        
        self.cargar_ajustar_img()
            
        self.bempezar = Boton(350, 480, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Empezar", self.colores["negro"], self.fuente)
        self.texto_fuerza = Label(70, 100, self.vista.aviso_medicion_fuerza(), self.fuente, self.colores["negro"]) 
        
        self.bsiguiente = Boton(710, 520, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Siguiente", self.colores["negro"], self.fuente)
                 
    def cargar_ajustar_img(self): 
        tamanho = (350,350)
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.imagen_ruleta = pygame.image.load(directorio_actual + "\\Multimedia\\ruleta.png")
        self.imagen_ruleta = pygame.transform.scale(self.imagen_ruleta, tamanho )

        self.imagen_puntero = pygame.image.load(directorio_actual + "\\Multimedia\\puntero.png")
        self.imagen_puntero = pygame.transform.scale(self.imagen_puntero, tamanho   )

        self.imagen_baseruleta = pygame.image.load(directorio_actual + "\\Multimedia\\base_ruleta.png")
        self.imagen_baseruleta = pygame.transform.scale(self.imagen_baseruleta, tamanho )

    def girar_imagen(self, imagen: Surface, angulo: int):
        imagen_girada = pygame.transform.rotate(imagen, angulo)
        return imagen_girada

    def ejecutar(self, jugador: Jugador)->int:
        
        self.texto_turno = Label(260, 50, self.vista.turno(jugador), self.fuente, self.colores["negro"])
        self.labels = [self.texto_fuerza, self.texto_turno]
        imagen_girada = self.imagen_ruleta
        velocidad_rotacion = 1
        angulo = 0 
        siguiente = False
        self.__contador = 0 
        tiempo_inicio =  None  

        while not siguiente:
            
            mouse_pos = pygame.mouse.get_pos()
            tiempo_actual = int(pygame.time.get_ticks() / 1000)  #Lo devuelve en milisegundos, por eso se divide entre 1000

            self.screen.fill(self.colores["fondo"]) 

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bempezar.fue_presionado(mouse_pos, event): 
                    self.bempezar.eliminado = True
                    self.__contador = 0
                    tiempo_inicio = tiempo_actual
                elif event.type == pygame.KEYDOWN and tiempo_inicio is not None :
                    tiempo_transcurrido = (tiempo_actual - tiempo_inicio) 
                    if tiempo_transcurrido <= 5:  # Solo contar las pulsaciones de teclas dentro de los primeros 5 segundos
                        self.__contador += 1 
                elif event.type == pygame.KEYUP:
                    print("Se ha levantado la tecla")
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    siguiente = True

            sup_imagen_girada = imagen_girada.get_rect(center=(self.width // 2, self.height // 2) ) #Obtenemos la superficie de la imagen
            sup_puntero_base = self.imagen_puntero.get_rect(center= (self.width // 2, self.height // 2) )

            self.screen.blit(self.imagen_baseruleta, sup_puntero_base ) # Puntero y base tienen la misma superficie ya que queremos que estén en capas superpuestas e independientes a la superficie de la ruleta
            self.screen.blit(imagen_girada, sup_imagen_girada)
            self.screen.blit(self.imagen_puntero, sup_puntero_base) 
            #IMPORTANTE EL ORDEN

            angulo %= 360 # Se ajusta el giro para que no sea mayor de 360º

            self.fuerza = Label(100, 500 , f"¡Guau! Has presionado {self.__contador} veces, ¡increíble!", self.fuente, self.colores["negro"])
            
            if tiempo_inicio is not None: 
                tiempo_transcurrido = (tiempo_actual - tiempo_inicio)
                if tiempo_transcurrido > 4: #> 4 para que el usuario pueda ver la renderización del texto 
                    self.fuerza.draw(self.screen)
                    self.bsiguiente.draw(self.screen)
                if 6 <= tiempo_transcurrido < 10:  
                    angulo += velocidad_rotacion
                    imagen_girada = self.girar_imagen(self.imagen_ruleta, angulo)

            self.texto_turno.draw(self.screen)  
            self.texto_fuerza.draw(self.screen)
            self.bempezar.draw(self.screen)  
            
            self.bsiguiente.update(mouse_pos) 

            # Actualizar la pantalla
            pygame.display.flip()
    
        return self.__contador
