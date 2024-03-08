import pygame

class Label:
    def __init__(self, x, y, text, font_size, color):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=(self.x, self.y))

    def update(self, text):
        self.text = text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect.topleft)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    label = Label(100, 100, "Hola mundo", 24, (255, 0, 0))

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        label.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
