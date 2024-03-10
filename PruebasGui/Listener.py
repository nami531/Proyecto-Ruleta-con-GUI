from typing import Any
import pygame
class Listener: 
    __contador : int       
    fps : pygame.time.Clock 


    def __init__(self):
        self.pantalla = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("Medidor de fuerza")
        self.fps = pygame.time.Clock()
        self.__contador = 0 
        
    @property 
    def contador(self): 
        return self.__contador

    @contador.setter
    def contador(self, contador): 
        self.__contador = self.__contador 

    def medir_fuerza(self): 
        self.__contador = 0 
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
                        self.__contador +=1 
                elif event.type == pygame.KEYUP:
                    print("Se ha levantado la tecla")
                
            self.fps.tick(20)
        
            
            
            pygame.display.update()
        pygame.quit()
        return self.__contador


    
if __name__ == "__main__":
    input("Hla")
    pygame.init()
    l = Listener()
   
        