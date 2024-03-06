import pygame
from pygame.locals import *

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.lista_nombres = []

    def gestionar_eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Cambiar el estado activo cuando se hace clic en el cuadro de entrada
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Cambiar el color del cuadro de entrada
        if self.active: 
            self.color = pygame.Color('dodgerblue2')  
        else:  
            pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.lista_nombres.append(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Volver a renderizar el texto
                self.txt_surface = self.font.render(self.text, True, self.color)
    
    def devolver_nombre_jugador(self): 
        return self.text

    def actualizar(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def mostrar(self, screen): 
        # Dibujar el cuadro de entrada
            pygame.draw.rect(screen, self.color, self.rect, 2)
            # Dibujar el texto
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5 ))
    
    def devolver_lista_nombres(self): 
        return self.lista_nombres


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    input_box = InputBox(100, 100, 140, 32)
    input_boxes = [input_box]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.gestionar_eventos(event)

        for box in input_boxes:
            box.actualizar()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.mostrar(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()