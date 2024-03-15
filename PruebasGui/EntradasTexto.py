import pygame
import sys

class EntradasTexto:

    x : int
    y : int
    __width_old: int
    __width: int
    __height: int
    color: tuple[int, int, int]
    text_color: tuple[int, int, int]
    background_color: tuple[int, int, int]
    font_size: int
    rect: pygame.Rect
    font: pygame.font.Font
    text: str
    activo: bool
    hovered: bool
    eliminado: bool

    def __init__(self, x, y, width, height, color, text_color, background_color, font_size):
        self.x = x
        self.y = y
        self.__width_old = width
        self.__width = width
        self.__height = height
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
    
    @property
    def width_old(self) -> int:
        return self.__width_old

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        if value >= 0:
            self.__width_old = self.__width
            self.__width = value
        else:
            self.__width_old = self.__width
            self.__width = 0

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int):
        if value >= 0:
            self.__height = value
        else:
            self.__height = 0

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
                        text_width = self.font.size(self.text)[0]
                        self.width = max(self.width_old, text_width - 1)  # Ajustar el ancho mínimo
                        self.rect.width = self.width

                    else:
                        self.text += event.unicode  # Agregar el carácter ingresado al texto
                        text_width = self.font.size(self.text)[0]
                        self.width = max(self.width_old, text_width + 10)  # Ajustar el ancho mínimo
                        self.rect.width = self.width

