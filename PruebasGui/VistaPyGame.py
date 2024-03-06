import pygame
from pygame.locals import *
from JuegoGUI import Juego
from Jugador import Jugador
from Input import InputBox

class VistaGUI:
    def __init__(self):
        pygame.init()
        self.input = InputBox(100, 100, 140, 32)
        self.juego = Juego()
        self.screen = pygame.display.set_mode((900, 450))
        pygame.display.set_caption("Ruleta de la suerte")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.num_jug = 0
        self.inputs = []

    def bienvenida(self):
        self.screen.fill((0, 0, 255))
        texto_bienvenida = self.font.render("¡Bienvenidx a la ruleta!", True, (255, 255, 255))
        self.screen.blit(texto_bienvenida, (300, 200))
        pygame.display.flip()

    def cuantos_jugadores(self):
        self.screen.fill((0, 0, 255))
        texto1 = self.font.render("Número de jugadores:", True, (255, 255, 255))
        self.screen.blit(texto1, (300, 100))

        buttons = []
        for i in range(2, 7):
            button = pygame.Rect(200 + (i-2) * 100, 150, 50, 50)
            pygame.draw.rect(self.screen, (255, 0, 0), button)
            texto = self.font.render(str(i)+"jugadores", True, (255, 255, 255))
            self.screen.blit(texto, (215 + (i-2) * 100, 165))
            buttons.append(button)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, button in enumerate(buttons):
                        if button.collidepoint(mouse_pos):
                            self.crear_etiquetas_y_entrys(i+2)
                            return
                        
        

    def crear_etiquetas_y_entrys(self, num_elementos):
        self.num_jug = num_elementos
        self.screen.fill((0, 0, 255))
        for i in range(num_elementos):
            etiqueta = self.font.render(f"Jugador {i+1}:", True, (255, 255, 255))
            self.screen.blit(etiqueta, (200, 200 + i * 50))
            entrada = pygame.Rect(300, 200 + i * 50, 150, 30)
            pygame.draw.rect(self.screen, (255, 255, 255), entrada, 2)
            self.inputs.append(entrada)

        enviar = self.font.render("Enviar", True, (255, 255, 255))
        enviar_rect = enviar.get_rect(center=(650, 400))
        pygame.draw.rect(self.screen, (0, 255, 0), enviar_rect)
        self.screen.blit(enviar, enviar_rect.topleft)
        self.mostrar_inputs(self.num_jug)
        pygame.display.flip()
        

    def mostrar_inputs(self, num_inputs): 
        input_boxes = []
        for i in range(num_inputs): 
            input_box = InputBox(100, 100, 140, 32)
            input_boxes.append(input_box)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                for box in input_boxes:
                    box.gestionar_eventos(event)

            for box in input_boxes:
                box.actualizar()

            self.screen.fill((30, 30, 30))
            for box in input_boxes:
                box.mostrar(self.screen)
                print(self.input.lista_nombres)

            pygame.display.flip()

    # def wait_for_input(self):
    #     nombre_jugadores = []
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 exit()
    #             if event.type == MOUSEBUTTONDOWN:
    #                 mouse_pos = event.pos
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #         # Cambiar el estado activo cuando se hace clic en el cuadro de entrada
    #                 if self.rect.collidepoint(event.pos):
    #                     self.active = not self.active
    #                 else:
    #                     self.active = False
    #                 # Cambiar el color del cuadro de entrada
    #             if self.active: 
    #                 self.color = pygame.Color('dodgerblue2')  
    #             else:  
    #                 pygame.Color('lightskyblue3')
    #             if event.type == pygame.KEYDOWN:
    #                 if self.active:
    #                     if event.key == pygame.K_RETURN:
    #                         self.lista_nombres.append(self.text)
    #                         self.text = ''
    #                     elif event.key == pygame.K_BACKSPACE:
    #                         self.text = self.text[:-1]
    #                     else:
    #                         self.text += event.unicode
    #                     # Volver a renderizar el texto
    #                     self.txt_surface = self.font.render(self.text, True, self.color)
    

    def mostrar_turno(self, i):
        while True:
            self.screen.fill((0, 0, 255))
            # nombre_jugador = self.juego.lista_jugadores[i].nombre
            texto = self.font.render(f"Jugador {i}, es tu turno, ¿Qué quieres hacer?", True, (255, 255, 255))
            self.screen.blit(texto, (100, 100))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    # t = VistaGUI()
    # jueg = Juego()
    # j1 = Jugador("Nadia")
    # j2 = Jugador("Marquez")
    # jueg.anhadirJugador(j1)
    # jueg.anhadirJugador(j2)

    # t.bienvenida()
    # t.cuantos_jugadores()

    # pygame.init()
    # screen = pygame.display.set_mode((640, 480))
    # clock = pygame.time.Clock()
    # input_box = InputBox(100, 100, 140, 32)
    # input_boxes = [input_box]
    # done = False

    t = VistaGUI()
    jueg = Juego()
    j1 = Jugador("Nadia")
    j2 = Jugador("Marquez")
    jueg.anhadirJugador(j1)
    jueg.anhadirJugador(j2)

    if jueg.lista_jugadores:
        t.bienvenida()
        t.cuantos_jugadores()
        t.mostrar_turno(0)
    else:
        print("No hay jugadores en la lista")