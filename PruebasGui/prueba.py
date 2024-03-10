import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectángulo con Texto")

# Definir el color del rectángulo y del texto
rect_color = (0, 0, 255)  # Azul
text_color = (255, 255, 255)  # Blanco

# Definir las coordenadas y dimensiones del rectángulo
rect_x, rect_y = 100, 100
rect_width, rect_height = 200, 150

# Definir el texto y la fuente
font = pygame.font.Font(None, 36)  # Fuente predeterminada con tamaño 36
texto = "Hola, mundo!"

# Renderizar el texto como una superficie
text_surface = font.render(texto, True, text_color)

# Obtener el rectángulo que enmarca el texto
text_rect = text_surface.get_rect()

# Centrar el rectángulo de texto en el rectángulo
text_rect.center = (rect_x + rect_width // 2, rect_y + rect_height // 2)

# Ejecución del bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpia la pantalla con un color de fondo
    screen.fill((255, 255, 255))  # Blanco

    # Dibuja el rectángulo en la pantalla
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Dibuja el texto en el rectángulo
    screen.blit(text_surface, text_rect)

    # Actualiza la pantalla
    pygame.display.flip()