import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from pygame import Surface
from Jugador import Jugador
import textwrap
import os

class VentanaError:

    vista: Vista
    width : int
    height : int
    screen : Surface
    tamanho_botones: tuple[int,int]
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    # tipo_fuente : font
    bintroducir : Boton
    id : Label
    puntuacion : Label
    letra : Label
    entrada : EntradasTexto
    elementos : list[Label | EntradasTexto]
    __errores : list[str | None]

    def __init__(self,  width: int = 800, height: int = 600):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.tamanho_botones = (80, 50)
  
        self.fuente = 24

        self.colores = { "fondo" : (234,234,234),
                        "negro" : (0,0,0),
                        "blanco": (255,255,255),
                        "morado": (204, 202, 234),
                        "morado_hover" : (159, 149, 175),
                        "azul" : (199, 228, 255) ,
                        "azul_hover" : (46, 155, 255)
        }
        
        self.tipo_fuente = pygame.font.Font(None, 24)
        
        self.intletra = Label(100, 100, self.vista.introducir_letra(), self.fuente, self.colores["negro"])
        
        self.entrada = EntradasTexto(275, 92, 200, 30, self.colores["negro"], self.colores["negro"], self.colores["blanco"], self.fuente) 

        self.bintroducir = Boton(700, 530, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Introducir", self.colores["negro"], self.fuente)

        self.__errores = [self.vista.comodin, self.vista.longitud_incorrecta(), self.vista.decir_letra_esta_repetida(self.entrada.text), self.vista.decir_letra_no_aparece(self.entrada.text), self.vista.vocal_sin_comprar(), self.vista.letra_en_comprar_vocal(), self.vista.saldo_insuficiente()]

    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self, enigma: str, pista: str, letras: list[str], vocales: list[str]) -> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma, pista, letras, vocales)
        
        # Calculamos el tamaño de cada rectángulo en función del tamaño de la ventana
        tamanho_rect = (self.width // 40, self.height // 15)
        
        margen_y = self.height // 6  
        margen_x = tamanho_rect[0] // 2 
        
        x = self.width // 8  
        y = self.height // 4 + 30 

        #Todas las posiciones en este caso son relativas a la ventana
        
        for i in range(len(enigma_cifrado)):
            letra = enigma_cifrado[i]
            if letra.lower() in letras:  
                self.dibujar_rect_Letra(letra, x, y, tamanho_rect)
                x += tamanho_rect[0] + margen_x  # Movemos los rectángulos con el tamaño del rectángulo y el margen
            
            elif letra == " ": 
                x += tamanho_rect[0] + margen_x  # Incrementamos con tamaño del rectángulo y el margen
            else: 
                pygame.draw.rect(self.screen, self.colores["azul"], (x, y, tamanho_rect[0], tamanho_rect[1]))
                x += tamanho_rect[0] + margen_x  
                
            #comprobamos si hemos llegado al final de la fila para saltar a la siguiente
            if x + tamanho_rect[0] > self.width - tamanho_rect[0]:
                x = self.width // 10  # Se reinicia x
                y += margen_y 
        return y

             
    def dibujar_rect_Letra(self, letra: str, x: int, y: int, tamanho: tuple[int, int])-> None: 
        rect = pygame.Rect(x, y, tamanho[0], tamanho[1])
        pygame.draw.rect(self.screen, self.colores["azul"], rect) #Primero se crean los rectángulos a los que va a pertenecer

        sup_texto = self.tipo_fuente.render(letra, True, self.colores["negro"])
        rect_texto = sup_texto.get_rect(center=rect.center)
        self.screen.blit(sup_texto, rect_texto)

    def genera_pista_adaptada(self, pista: str, rectangulo): #rectangulo: Rect       
        pista = textwrap.wrap(pista, width=75) #Esta libreria adapta el texto al width (nº caracteres) deseado
        y = rectangulo.top
        for linea in pista:
            texto_render = self.tipo_fuente.render(linea, True, self.colores["negro"])
            self.screen.blit(texto_render, (rectangulo.left + 10, y + 10))
            y += texto_render.get_height()
         
    def dibujar_pista(self, pista: str, ultimo_y: int): 
        rectangulo = pygame.draw.rect(self.screen, self.colores["morado"], (100, ultimo_y+100, 630, 100))
        self.genera_pista_adaptada(pista, rectangulo)  
    
    def genera_error_adaptada(self, error: int, rectangulo): #rectangulo: Rect            
        error = textwrap.wrap(self.errores[error], width=75) #Esta libreria adapta el texto al width (nº caracteres) deseado
        y = rectangulo.top
        fuente_error = pygame.font.Font(None, 24)
        for linea in error:

            texto_render = fuente_error.render(linea, True, self.colores["negro"])
            self.screen.blit(texto_render, (rectangulo.left + 10, y + 10))
            y += texto_render.get_height()
    
    def dibujar_error(self, error: int):
        rectangulo = pygame.draw.rect(self.screen, self.colores["morado_hover"], (100,140, 630, 30))
        self.genera_error_adaptada(error, rectangulo)  

    @property
    def errores(self): 
        return self.__errores
    
    @errores.setter
    def errores(self, valor): 
        self.__errores = self.__errores

    def ejecutar(self, enigma_juego: str, pista: str, jugador: Jugador, error: int, letras: list[str], vocales: list[str], letra: str=""):
        self.id = Label(100, 50, f"Jugador {jugador}", self.fuente, self.colores["negro"])
        self.puntuacion = Label(300, 50, f"Puntuación: {jugador.comprobar_puntuacion()[0]}", self.fuente, self.colores["negro"])
        self.elementos =  [self.id, self.puntuacion, self.intletra, self.entrada]

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
                elif error == 6 and self.bintroducir.fue_presionado(mouse_pos, event): 
                    siguiente = True 
                elif self.bintroducir.fue_presionado(mouse_pos, event) and (error != 3) : 
                    if self.entrada.text != "": 
                        return self.entrada.text
                elif self.bintroducir.fue_presionado(mouse_pos, event):
                    siguiente = True 

                self.entrada.update(mouse_pos, event)

            self.screen.fill(self.colores["fondo"]) 


            ultimo_y = self.dibujar_rect_encriptados(enigma_juego, letra, letras, vocales)
            
            self.dibujar_pista(pista, ultimo_y)

            for elemento in self.elementos: 
                elemento.draw(self.screen)

            if error != 0:
                self.dibujar_error(error) 

            if error == 3: 
                self.intletra.eliminado = True
                self.entrada.eliminado = True
            else: 
                self.intletra.eliminado = False
                self.entrada.eliminado = False


            self.bintroducir.draw(self.screen)
        
            self.bintroducir.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
        return ""
 