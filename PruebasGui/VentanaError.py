import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from pygame import Surface
from Jugador import Jugador

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

    def __init__(self, width: int, height: int):
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
        
        self.entrada = EntradasTexto(275, 92, 200, 30, self.colores["negro"], self.colores["negro"], self.colores["blanco"], 24) 

        self.bintroducir = Boton(700, 530, self.tamanho_botones[0], self.tamanho_botones[1], self.colores["azul"], self.colores["azul_hover"], "Introducir", self.colores["negro"], self.fuente)


        self.__errores = ["", self.vista.longitud_incorrecta(), self.vista.decir_letra_esta_repetida(self.entrada.text), self.vista.decir_letra_no_aparece(self.entrada.text), self.vista.vocal_sin_comprar(), self.vista.letra_en_comprar_vocal(), self.vista.saldo_insuficiente()]

        
    
    #Función que dibuja los rectangulos, del panel
    def dibujar_rect_encriptados(self,enigma : str, pista: str ,letra : str,letras : list[str],vocales : list[str])-> int:
        enigma_cifrado = self.vista.mostrar_panel_cifrado(enigma, pista, letras, vocales)
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
        superficie_pista = self.tipo_fuente.render(pista, True, self.colores["negro"])
        rect_pista = superficie_pista.get_rect()
        rect_pista.center = (100 + 630 // 2, y + 300 // 2)
        pygame.draw.rect(self.screen, self.colores["morado"], (100, y+100, 630, 100))
        self.screen.blit(superficie_pista, rect_pista)    
    
    def dibujar_error(self, error: int): 
        sup_error = self.tipo_fuente.render(self.errores[error], True, self.colores["negro"])
        rect_error = sup_error.get_rect()
        rect_error.center = (100 + 630 // 2, 130 + 25 // 2)
        pygame.draw.rect(self.screen, self.colores["morado_hover"], (100,130, 630, 25))
        self.screen.blit(sup_error, rect_error)

    @property
    def errores(self): 
        return self.__errores
    
    @errores.setter
    def errores(self, valor): 
        self.__errores = self.__errores


    def ejecutar(self, enigma_juego: str, pista: str,jugador: Jugador, error: int, letras: list[str], vocales: list[str], letra: str=""):
        self.id = Label(100, 50, f"Jugador {jugador.nombre}", 24,(0,0,0))
        self.puntuacion = Label(300, 50, f"Puntuación: {jugador.comprobar_puntuacion()[0]}", 24, (0,0,0))
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
                elif self.bintroducir.fue_presionado(mouse_pos, event) and error != 3: 
                    if self.entrada.text != "": 
                        return self.entrada.text
                elif self.bintroducir.fue_presionado(mouse_pos, event):
                    siguiente = True 
                     
                
                self.entrada.update(mouse_pos, event)

            self.screen.fill(self.colores["fondo"])  # Limpiar la pantalla con color blanco

            ultimo_y = self.dibujar_rect_encriptados(enigma_juego, pista, letra, letras, vocales)
            
            self.dibujar_pista(pista, ultimo_y)

            for elemento in self.elementos: 
                elemento.draw(self.screen)

            if error != 0:
                self.dibujar_error(error) 
            if error == 3: 
                self.intletra.eliminado = True
                self.entrada.eliminado = True

            self.bintroducir.draw(self.screen)
        
            self.bintroducir.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaError(800, 600)
    print(ventana.ejecutar("Hola me llamo nadia", "Mi nombre", j1, 2, ["h", "l", "y", "p"], ["i"]))