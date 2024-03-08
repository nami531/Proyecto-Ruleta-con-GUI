from typing import Any
import pygame
# # from pynput import keyboard as kb

# # def pulsa(tecla):
# # 	print('Se ha pulsado la tecla ' + str(tecla))

# # def suelta(tecla):
# # 	print('Se ha soltado la tecla ' + str(tecla))
# # 	if tecla == kb.KeyCode.from_char('q'):
# # 		return False




# # class Cursor(pygame.Rect): 
# #     def __init__(self): 
# #         pygame.Rect.__init__(self,0,0,1,1)

# #     def update(self): 
# #         self.left, self.top = pygame.mouse.get_pos()

# # class Boton(pygame.sprite.Sprite):
# #     def __init__(self, pantalla):
# #         self.pantalla = pantalla
# #         self.rect = (50,50,100,50)

# #     def update(self, cursor):
# #         if cursor.colliderect(self.rect): 
# #             pygame.draw.rect(self.pantalla, (0,0,0), self.rect )
# #         else: 
# #             pygame.draw.rect(self.pantalla, (0,0,0), (5,20,100,50))

# def main(): 
#     contador = 0   
#     pygame.init()

#     pantalla= pygame.display.set_mode((1, 1))
#     pygame.display.set_caption("Medidor de fuerza")
#     fps = pygame.time.Clock()
    
#     # c1= Cursor()
#     # b1 = Boton(pantalla)
    

#     # color = (255,255,255)
#     # escuchador = kb.Listener()
#     # escuchador.start() and escuchador.is_alive()   
 

# print(main())

class Listener: 
    contador : int       
    fps : pygame.time.Clock 


    def __init__(self):
        self.pantalla = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("Medidor de fuerza")
        self.fps = pygame.time.Clock()
        self.contador = 0 

    def medir_fuerza(self): 
        self.contador = 0 
        salir = False
        tiempo = int(pygame.time.get_ticks() / 1000)
    
        while not salir :
             #Lo devuelve en milisegundos
            tiempo2 = int(pygame.time.get_ticks() / 1000)    
            
            if tiempo2 - tiempo > 5: 
                salir = True

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    salir = True
                elif event.type == pygame.KEYDOWN  : 
                        self.contador +=1 
                elif event.type == pygame.KEYUP:
                    print("Se ha levantado la tecla")
                
            self.fps.tick(20)
        
            
            
            pygame.display.update()
        pygame.quit()
        return self.contador


    
if __name__ == "__main__":
    input("Hla")
    pygame.init()
    l = Listener()
   
        