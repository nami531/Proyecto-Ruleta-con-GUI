import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from Jugador import Jugador
from pygame import Surface
from pygame import font

class VentanaPanelEntrada:

    vista: Vista
    width : int
    height : int
    screen : Surface
    x_botones : int
    tamanho_botones: tuple[int,int]
    margen :int
    fuente : int
    colores : dict[str, tuple[int,int,int]]
    tipo_fuente : font
    bsiguiente : Boton
    id : Label
    puntuacion : Label
    letra : Label
    entrada : EntradasTexto
    elementos : list[Label | EntradasTexto]

    def __init__(self, width, height, jugador: Jugador):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.tipo_fuente = pygame.font.Font(None, 36)
        self.x_botones = 50
        self.tamanho_botones = 120
        self.margen = 150
        
        self.id = Label(100, 50, f"Jugador {jugador.nombre}", self.fuente ,self.colores["negro"])
        self.puntuacion = Label(300, 50, f"Puntuación: + {jugador.comprobar_puntuacion()}", self.fuente, self.colores["negro"])
        self.letra = Label(100, 100, self.vista.introducir_letra(), self.fuente, self.colores["negro"])
        
        self.entrada = EntradasTexto(275, 92, 200, 30, self.colores["blanco"], self.colores["negro"], self.fuente) 
        self.elementos =  [self.id, self.puntuacion, self.letra, self.entrada]

        self.bsiguiente = Boton(700, 500, 75, 25, self.colores["azul"], self.colores["azul_hover"], "Introducir", self.colores["negro"], self.fuente)

    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self,enigma : str, pista: str ,letra : str,letras : list[str],vocales : list[str])-> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma, pista, letras, vocales, letra)
        margen_y = 120
        x = 100
       
        tamanho = (25,50)
        for i in range(len(enigma_cifrado)):
            j = i % 14 #Reinicia la fila en la que nos encontramos, de tal forma que i= columna, j= fila
            y = 200
            margen_x = 50
            x, y= self.filas(i,x, y , margen_y)
            letra = enigma_cifrado[i]
            if letra == "_": 
                pygame.draw.rect(self.screen, self.colores["azul"], (x + margen_x * j, y, tamanho[0], tamanho[1]))
            elif letra == " ": 
                margen_x += 10
            else: 
                self.dibujar_rect_Letra(letra, x, y, margen_x, tamanho, j)
        return y

    @staticmethod
    def filas(i: int,x:int , y: int, margen_y: int)->tuple[int,int]: 
        if i >= 14: 
            y += margen_y * (i//14) #  define la fila en la que estamos 
            x = 100
        return x, y
             
    def dibujar_rect_Letra(self, letra: str, x: int, y: int, margen_x: int, tamanho: tuple[int, int], j: int)-> None: 
        sup_texto = self.tipo_fuente.render(letra, True, self.colores["negro"])
        rect_texto = sup_texto.get_rect()
        rect_texto.center = (x + margen_x * j + tamanho[0] // 2, y + tamanho[1] // 2)
        pygame.draw.rect(self.screen, self.colores["azul"], (x + margen_x * j, y, tamanho[0], tamanho[1]))
        self.screen.blit(sup_texto, rect_texto)

    def dibujar_pista(self, pista: str, y: int)->None: 
        superficie_pista = self.fuente.render(pista, True, self.colores["blanco"])
        rect_pista = superficie_pista.get_rect()
        rect_pista.center = (100 + 500 // 2, y + 100 // 2)
        pygame.draw.rect(self.screen, self.colores["morado"], (100, y+100, 500, 100))
        self.screen.blit(superficie_pista, rect_pista)

    def ejecutar(self, enigma_juego:str, pista: str,  letras: list[str], vocales: list[str],letra: str =""):
        siguiente = False
        while not siguiente:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    return self.entrada.text.lower()
                
                self.entrada.update(mouse_pos, event)

            self.screen.fill(self.colores["fondo"])  

            ultimo_y = self.crear_rect_encriptados(enigma_juego, letras, vocales, letra)
            
            self.dibujar_pista(pista, ultimo_y)

            for elemento in self.elementos: 
                elemento.draw(self.screen)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaPanelEntrada(800, 600, j1)
    print(ventana.ejecutar("__l_ __ ll___ n____", "Mi nombre"))