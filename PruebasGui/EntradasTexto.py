import pygame
import sys

class EntradasTexto:
    def __init__(self, x, y, width, height, color, text_color, background_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.background_color = background_color
        self.font_size = font_size
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, self.font_size)
        self.text = ""
        self.activo = False
        self.hovered = False
        self.eliminado = False

    def draw(self, screen):
        if not self.eliminado: 
            if self.hovered:
                self.activo = True
            else: 
                self.activo = False
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)  # Dibujar el borde del cuadro de texto
            pygame.draw.rect(screen, self.background_color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))  # Dibujar el fondo del cuadro de texto
            text_surface = self.font.render(self.text, True, self.text_color)
            screen.blit(text_surface, (self.x + 5, self.y + 5))  # Ajustar el texto para que no esté justo en el borde del cuadro de texto

    def update(self, mouse_pos, event):
        if not self.eliminado: 
            self.hovered = self.rect.collidepoint(mouse_pos)
            if self.activo: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]  # Eliminar el último carácter
                    else:
                        self.text += event.unicode  # Agregar el carácter ingresado al texto

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    cuadro_texto = EntradasTexto(150, 100, 200, 50, (255, 255, 255), (0,0,0),(255,255,255), 24)
    cuadro_texto2 = EntradasTexto(200, 200, 200, 50, (255, 255, 255), (255, 255, 255), (255,255,255), 24)
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            cuadro_texto.update(mouse_pos, event)
            cuadro_texto2.update(mouse_pos, event)

        cuadro_texto.draw(screen)
        cuadro_texto2.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

