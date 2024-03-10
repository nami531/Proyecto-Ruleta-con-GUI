import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista
from Jugador import Jugador

class VentanaError:

    labels : list[Label]
    inputs : list[EntradasTexto]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.font = pygame.font.Font(None, 36)
        self.x_botones = 50
        self.tamanho_botones = 120
        self.margen = 150
        
        
        self.intletra = Label(100, 100, self.vista.introducir_letra(), 24, (0,0,0))
        
        self.entrada = EntradasTexto(275, 92, 200, 30, (255,255,255), (0,0,0), 24) 
       

        self.bsiguiente = Boton(700, 500, 75, 25, (0,0,0), (23,233,65), "Introducir", (255,255,255), 24)
        
    
    def crear_rect_encriptados(self):
        enigma_cifrado = self.vista.mostrar_panel_cifrado(self.enigma,self.letra, self.letras, self.vocales)
        margen_y = 120
        x = 100
       
        tamanho = (20,50)
        for i in range(len(enigma_cifrado)):
            j = i % 9
            y = 200
            margen_x = 50
            x, y= self.filas(i,x, y , margen_y)
            letra = enigma_cifrado[i]
            if letra == "_": 
                pygame.draw.rect(self.screen, (0,0,0), (x + margen_x * j, y, tamanho[0], tamanho[1]))
            elif letra == " ": 
                margen_x += 10
            else: 
                text_surface = self.font.render(letra, True, (255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.center = (x + margen_x * j + tamanho[0] // 2, y + tamanho[1] // 2)
                pygame.draw.rect(self.screen, (0,0,0), (x + margen_x * j, y, tamanho[0], tamanho[1]))
                self.screen.blit(text_surface, text_rect)
        return y
    @staticmethod
    def filas(i,x , y, margen_y)->tuple[int,int]: 
        if i >= 9: 
            y += margen_y * (i//9) #  define la fila en la que estamos 
            x = 100
        return x, y
             

    def ejecutar(self, enigma_juego, pista,jugador, error, letras, vocales, letra=""):
        self.letras = letras
        self.vocales = vocales
       
        self.letra = letra
        self.id = Label(100, 50, f"Jugador {jugador.nombre}", 24,(0,0,0))
        self.puntuacion = Label(300, 50, f"Puntuación: + {jugador.comprobar_puntuacion()}", 24, (0,0,0))
        self.elementos =  [self.id, self.puntuacion, self.intletra, self.entrada]

        self.error = error
        self.errores = ["", self.vista.longitud_incorrecta(), self.vista.decir_letra_esta_repetida(self.entrada.text), self.vista.decir_letra_no_aparece(self.entrada.text), self.vista.vocal_sin_comprar(), self.vista.letra_en_comprar_vocal(), self.vista.saldo_insuficiente()]

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
                elif self.bsiguiente.fue_presionado(mouse_pos, event): 
                    return self.entrada.text
                
                self.entrada.update(mouse_pos, event)

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            y = self.crear_rect_encriptados()
            
            superficie_pista = self.font.render(self.pista, True, (255,255,255))
            rect_pista = superficie_pista.get_rect()
            rect_pista.center = (100 + 500 // 2, y + 100 // 2)
            pygame.draw.rect(self.screen, (0,0,0), (100, y+100, 500, 100))
            self.screen.blit(superficie_pista, rect_pista)

            for elemento in self.elementos: 
                elemento.draw(self.screen)

            sup_error = self.font.render(self.errores[self.error], True, (255,255,255))
            rect_error = sup_error.get_rect()
            rect_error.center = (100 + 500 // 2, 150 + 100 // 2)
            pygame.draw.rect(self.screen, (0,0,0), (100,150, 500, 100))
            self.screen.blit(sup_error, rect_error)

            self.bsiguiente.draw(self.screen)
        
            self.bsiguiente.update(mouse_pos) 
            # Actualizar la pantalla
            pygame.display.flip()
 
if __name__ == "__main__":
    j1 = Jugador("Nadia")
    pygame.init()
    ventana = VentanaError(800, 600)
    print(ventana.ejecutar("__l_ __ ll___ n____", "Mi nombre", j1, 1))