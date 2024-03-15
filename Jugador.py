from Ruleta import Ruleta
from Listener import Listener
from Controlador import Controlador


class Jugador: 
    controlador : Controlador
    nombre : str
    _puntuacion: list[float|int|str] 


    def __init__(self, nombre: str) -> None:
        self.controlador = Controlador()
        
        self.nombre = nombre
        self._puntuacion = [0]  

    def girar_ruleta(self, ruleta: Ruleta, fuerza : int)-> None: 
        ruleta.girar(fuerza)
        
    @property
    def puntuacion(self): 
        return self._puntuacion[0] 
    
    @puntuacion.setter
    def puntuacion(self, puntuacion): 
        if puntuacion >= 0: 
            self._puntuacion[0] = puntuacion
        else: 
            self._puntuacion[0] = 0

    def comprar_vocal(self, letra: str , precio: int) -> bool:
        if self.controlador.es_vocal(letra):
            if self.puntuacion < precio: 
                return False
            else: 
                self.puntuacion -= precio
                return True
    
    def multiplicar_puntuacion(self, premio): 
        self.puntuacion *= premio

    def comprobar_puntuacion(self):
        print(self._puntuacion)
        
    def perder_mitad(self, premio: int | float): 
        self.multiplicar_puntuacion(premio)

    def en_quiebra(self, premio: int|float): 
        self.multiplicar_puntuacion(premio)
 
    def ganar_puntuacion(self, premio: int | float, apariciones: int = 1):    
        if premio == 2: 
            self.multiplicar_puntuacion(premio)
        elif premio == 1: 
            self._puntuacion.append("Comodín")
        else: 
            self.puntuacion += (premio * apariciones)

    def tiene_comodin(self): 
        if "Comodín" in self._puntuacion: 
            self._puntuacion.remove("Comodín") 
            return True
        return False
    
    def perder_turno(self, jugador: int, lista_jugadores: list)-> tuple[int,bool]: #SI LE PONES LIST[JUGADOR SE VUELVE LOCO]
        if self.tiene_comodin():
            mismo_jugador = True
            jugador = jugador
        else: 
            mismo_jugador= False
            jugador =(jugador + 1)  % len(lista_jugadores) 
        return jugador, mismo_jugador
    
    def devuelve_nombre(self)-> str:
        return self.nombre
    
    def resolver_enigma(self, enigma : str, enigma_jugador: str)-> bool: 
        if enigma.lower() == enigma_jugador.lower():
            return True
        else: 
            return False
    
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
