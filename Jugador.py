from Ruleta import Ruleta

from Jugada import Jugada


class Jugador(): 
    nombre : str
    _puntuacion: list[float|int|str] 


    def __init__(self, nombre: str) -> None:
        self.jugada = Jugada()
        self.nombre = nombre
        self._puntuacion = [0] #Hay que cifrarlo con propertys y demás 

    def girar_ruleta(self, ruleta: Ruleta)-> None: 
        fuerza= int(input("Con cuanta fuerza quieres tirar: "))
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

    def comprar_vocal(self, letra: str , precio: int):
        if self.jugada.es_vocal(letra):
            if self.puntuacion < precio: 
                print("Lo siento, no puedes comprar la vocal porque no tienes suficiente dinero")
            else: 
                self.puntuacion -= precio
    
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
            print("Te salvaste por el comodín")
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
        if enigma.lower()[:-2] == enigma_jugador.lower(): #[:-2] es necesario ya que al leer el enigma acaba con \n y esto afecta a la comparación 
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