from Juego import Juego

class Controlador: 
    
    def __init__(self, juego : Juego): 
        self.juego = juego

    def comprobaciones(self, letra): 
        if not self.juego.comprobaciones_al_introducir(letra): 
            if len(letra) > 

    