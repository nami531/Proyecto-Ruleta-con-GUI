import pygame

class Boton:
    def __init__(self, x, y, width, height, color_normal, color_hover, text, text_color, font_size, valor=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False
        self.eliminado = False
        self.presionado = False
        self.valor = valor

    def draw(self, screen):
        if not self.eliminado: 
            if self.hovered: 
                color= self.color_hover
            else: 
                color = self.color_normal
            pygame.draw.rect(screen, color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        if not self.eliminado: 
            self.hovered = self.rect.collidepoint(mouse_pos)

    def fue_presionado(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Verificar si se hizo clic con el botón izquierdo del ratón
            if self.rect.collidepoint(mouse_pos):  # Verificar si las coordenadas del clic están dentro del área del botón
                self.presionado = True
                return True
        return False

    def eliminar(self): 
        self.eliminado = True

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    button = Boton(150, 100, 100, 50, (0, 128, 0), (0, 255, 0), "Botón", (255, 255, 255), 24)

    running = True
    while running:
        screen.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button.update(mouse_pos)
        button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()