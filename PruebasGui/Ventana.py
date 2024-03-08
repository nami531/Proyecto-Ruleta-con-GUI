import pygame
import sys
from Boton import Boton
from Label import Label
from EntradasTexto import EntradasTexto
from Vista import Vista

class Ventana:

    labels : list[Label]
    inputs : list[EntradasTexto]

    def __init__(self, width, height):
        self.vista = Vista()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ruleta de la suerte")

        self.bienvenida = Label(250,150, self.vista.bienvenida(), 40, (0,0,0)) 

        self.x_botones = 50
        self.tamanho_botones = 120
        self.margen = 150

        self.b2jug = Boton(self.x_botones, 525, self.tamanho_botones, 50,(100,2,25), (9,35,2), "Hola", (0,0,0), 12, 2 )
        self.b3jug = Boton(self.x_botones + self.margen, 525, self.tamanho_botones, 50,(100,2,25), (9,35,2), "Hola", (0,0,0), 12, 3 )
        self.b4jug = Boton(self.x_botones + self.margen * 2, 525, self.tamanho_botones, 50,(100,2,25), (9,35,2), "Hola", (0,0,0), 12, 4 )
        self.b5jug = Boton(self.x_botones + self.margen * 3, 525, self.tamanho_botones, 50,(100,2,25), (9,35,2), "Hola", (0,0,0), 12, 5)
        self.b6jug = Boton(self.x_botones + self.margen * 4, 525, self.tamanho_botones, 50,(100,2,25), (9,35,2), "Hola", (0,0,0), 1, 6)
        self.benviar = Boton(700, 525, self.tamanho_botones, 50 , (100,2,25), (9,35,2), "Enviar", (0,0,0), 12)
        self.benviar.eliminado = True
        
        self.botones = [self.b2jug, self.b3jug, self.b4jug, self.b5jug, self.b6jug, self.benviar]
        self.labels = []
        self.inputs = []
        self.nombres_jug = []

        # self.imagen = pygame.image.load("Multimedia\\dados.png") 
    
    def crear_label(self, num_jug):
        for i in range(num_jug): 
            self.labels.append(Label(self.x_botones + self.margen * i, 525, self.vista.pedir_nombre_jugador(i), 25, (0,0,0)))

    def crear_inputs(self, num_jug): 
        print(0,1)
        for i in range(num_jug):
            self.inputs.append(EntradasTexto(self.x_botones + self.margen * i, 550, 100, 25, (0,0,0), (0,0,0), 12))
            print(self.inputs)
        #Hay que crear aqui bootoon enviar
        self.benviar.eliminado = False
        print(10)
        

    def devolver_nombres(self)-> list[str]: 
        return self.nombres_jug

    def ejecutar(self):
        nombres = False
        while not nombres:

            # Obtener la posición del cursor
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for boton in self.botones: 
                    if boton.fue_presionado(mouse_pos, event) and not boton.eliminado:
                        num_jug = boton.valor
                        for boton in self.botones: 
                            boton.eliminar()
                        self.crear_label(num_jug)
                        self.crear_inputs(num_jug)
                if self.benviar.fue_presionado(mouse_pos, event): 
                    for entrada in self.inputs: 
                        self.nombres_jug.append(entrada.text)
                        # print(entrada.text)
                    print(self.nombres_jug)
                    nombres = True
               
                for entrada in self.inputs: 
                    entrada.update(mouse_pos, event)
                    
            for boton in self.botones:
                boton.update(mouse_pos) 

            

            self.screen.fill((0, 0, 255))  # Limpiar la pantalla con color blanco

            # Dibujar elementos en la pantalla
            for boton in self.botones:
                boton.draw(self.screen) 

            for label in self.labels: 
                label.draw(self.screen)

            for entrada in self.inputs: 
                entrada.draw(self.screen)

            self.bienvenida.draw(self.screen)
            pygame.draw.rect(self.screen, (0,0,0), (250, 200, 300,300)) #Esto será una imagen en un futuro no muy lejano
            # self.screen.blit(self.imagen, (250, 200))
           

            # Actualizar la pantalla
            pygame.display.flip()
        return self.nombres_jug

 
if __name__ == "__main__":
    pygame.init()
    ventana = Ventana(800, 600)
    print(ventana.ejecutar())