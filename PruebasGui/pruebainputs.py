import pygame
from pygame.locals import *

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Cambiar el estado activo cuando se hace clic en el cuadro de entrada
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            # Cambiar el color del cuadro de entrada
            self.color = WHITE if self.active else BLACK #Cambiar a nnoormal 
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Al presionar Enter, el campo de entrada se desactiva
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    # Al presionar retroceso, se elimina el último carácter
                    self.text = self.text[:-1]
                else:
                    # Se añade el carácter ingresado al texto
                    self.text += event.unicode
                # Volver a renderizar el texto
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        # Dibujar el cuadro de entrada
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # Dibujar el texto
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))


def main(num_inputs):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Inputs con Pygame")
    clock = pygame.time.Clock()
    input_boxes = []

    # Crear los campos de entrada
    input_height = 40
    spacing = 10
    total_height = num_inputs * (input_height + spacing) - spacing
    top_margin = (screen.get_height() - total_height) // 2
    left_margin = (screen.get_width() - 300) // 2
    for i in range(num_inputs):
        input_box = InputBox(left_margin, top_margin + i * (input_height + spacing), 300, input_height)
        input_boxes.append(input_box)

    # Crear el botón de enviar
    send_button = pygame.Rect(left_margin, top_margin + total_height + 20, 100, 40)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if send_button.collidepoint(event.pos):
                    # Cuando se hace clic en el botón de enviar, se crea una lista con los textos de los campos de entrada
                    input_texts = [box.text for box in input_boxes]
                    print("Texto recibido de los inputs:", input_texts)

        screen.fill((30, 30, 30))
        # Dibujar los campos de entrada
        for box in input_boxes:
            box.draw(screen)
        # Dibujar el botón de enviar
        pygame.draw.rect(screen, (0, 255, 0), send_button)
        font = pygame.font.Font(None, 32)
        text = font.render("Enviar", True, BLACK)
        screen.blit(text, (send_button.x + 10, send_button.y + 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main(3) 