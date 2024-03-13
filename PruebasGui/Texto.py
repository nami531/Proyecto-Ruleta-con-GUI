import pygame
import sys

class TextoAdaptable:
    def __init__(self, texto, rectangulo, color=(255, 255, 255), font_name=None):
        self.texto = texto
        self.rectangulo = rectangulo
        self.color = color
        self.font_size = self.calcular_tamano_fuente()
        self.font = pygame.font.SysFont(font_name, self.font_size)
        self.renderizar_texto()

    def calcular_tamano_fuente(self):
        fuente = pygame.font.SysFont(None, 25)
        texto_ancho, texto_alto = fuente.size(self.texto)
        rectangulo_ancho, rectangulo_alto = self.rectangulo.size
        #Calcular el tamaño de fuente adecuado para que quepa dentro del rectángulo
        tamano_fuente = min(int((rectangulo_ancho / texto_ancho) * fuente.get_height()),
                            int((rectangulo_alto / texto_alto) * fuente.get_height()))
        return tamano_fuente

    def renderizar_texto(self):
        self.font = pygame.font.SysFont(None, self.font_size)
        texto_superficie = self.font.render(self.texto, True, self.color)
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = self.rectangulo.center
        self.texto_renderizado = (texto_superficie, texto_rect)

    def actualizar_texto(self, nuevo_texto):
        self.texto = nuevo_texto
        self.font_size = self.calcular_tamano_fuente()
        self.renderizar_texto()

    def dibujar(self, pantalla):
        pantalla.blit(*self.texto_renderizado)

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((400, 300))
    reloj = pygame.time.Clock()

    rectangulo = pygame.Rect(100, 100, 200, 50)
    texto_adaptable = TextoAdaptable("Texto de ejemplo", rectangulo)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        pantalla.fill((0, 0, 0))
        pygame.draw.rect(pantalla, (255, 255, 255), rectangulo, 2)
        texto_adaptable.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
