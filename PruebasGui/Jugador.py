from Ruleta import Ruleta

from Controlador import Controlador


class Jugador: 
    nombre : str
    _puntuacion: list[float|int|str] 


    def __init__(self, nombre: str) -> None:
        self.controlador = Controlador()
        
        self.nombre = nombre
        self._puntuacion = [0] #Hay que cifrarlo con propertys y demás 

    def girar_ruleta(self, ruleta: Ruleta, fuerza : int)-> None: 
        print(fuerza)
        ruleta.girar(fuerza)
        
    # def introducir_letra_no_vocal(self): #Podemos comprobar que no sea vocal al introducir la letra def es_vocal e iria en jugada
        
        # return letra
    @property
    def puntuacion(self): 
        return self._puntuacion[0] 
    
    @puntuacion.setter
    def puntuacion(self, puntuacion): 
        if puntuacion >= 0: 
            self._puntuacion[0] = puntuacion
        else: 
            self._puntuacion[0] = 0

    def comprar_vocal(self, letra: str , precio: int) -> bool | tuple[bool, int]:
        if self.controlador.es_vocal(letra):
            if self.puntuacion < precio: 
                return False
            else: 
                self.puntuacion -= precio
                return True
    
    def multiplicar_puntuacion(self, premio): 
        int(self.puntuacion *= premio)

    def comprobar_puntuacion(self)-> list:
        return self._puntuacion
        
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
            return True
        return False
    
    def perder_turno(self, jugador: int, lista_jugadores: list)-> tuple[int,bool]: #SI LE PONES LIST[JUGADOR SE VUELVE LOCO]
        if self.tiene_comodin():
            self._puntuacion.remove("Comodín") 
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
    
    # def ganar(self, vista: Vista):
    #     Vista.has_ganado(vista, self)
        
    # def perder()
    def __str__(self) -> str:
        return f"{self.nombre}"
    
if __name__ == "__main__": 
    r = Ruleta()
    j1 = Jugador("Nadia")
    print(j1.puntuacion)
    j1.ganar_puntuacion(50, 5)
    print(j1.puntuacion)
    j1.ganar_puntuacion(1, 5)
    print(j1._puntuacion)
    j1.perder_mitad(0.5)
    print(j1._puntuacion)
    j1.en_quiebra(0)
    print(j1._puntuacion)