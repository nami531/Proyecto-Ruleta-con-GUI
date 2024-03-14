import pygame
import sys
import textwrap

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectángulo con texto envuelto en Pygame")

# Función para renderizar texto con envoltura en un rectángulo
def render_text_in_rect(text, font, color, rect, max_width):
    lines = textwrap.wrap(text, width=max_width)
    y = rect.top
    for line in lines:
        rendered_text = font.render(line, True, color)
        screen.blit(rendered_text, (rect.left, y))
        y += rendered_text.get_height()

# Main loop
def main():
    font = pygame.font.Font(None, 24)  # Fuente y tamaño del texto
    text = "Este es un ejemplo de texto que se envolverá automáticamente dentro de un rectángulo en Pygame. La envoltura del texto se maneja con la función textwrap.wrap(). Espero que esto te ayude a comprender cómo puedes hacerlo tú mismo."
    max_width = 40  # Máximo de caracteres por línea
    rect_width = 400
    rect_height = 300
    rect_x = (WIDTH - rect_width) // 2
    rect_y = (HEIGHT - rect_height) // 2
    rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, rect)  # Dibujar el rectángulo
        render_text_in_rect(text, font, BLACK, rect.inflate(-20, -20), max_width)  # Renderizar texto dentro del rectángulo
        pygame.display.flip()

if __name__ == "__main__":
    main()
