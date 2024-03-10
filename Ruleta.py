import random
random.seed(1)
class Ruleta: 
    premios: dict[str,list[float]]
    ruleta: list[str]
    __puntero : int

    def __init__(self) -> None: 
        self.premios = {"comodin": [1, 1], 
                        "quiebra": [1, 0], 
                        "pierdeTurno": [1, -1],
                        "porDos": [1, 2],
                        "mitad":[1, 0.5],
                        "200": [2, 200],
                        "150": [5, 150],
                        "100": [7,100], 
                        "50": [6, 50]} #Clave: nombre premio Valores: cantidad existente del premio y su valor
        
        self.__puntero = 0 #El puntero siempre va a comenzar en la posición 0 

        self.ruleta = []
        premios = list(self.premios.keys())        #convierte en una lista todos las claves del diccinario self.premios
        for i in range(25,0,-1): 
            posicion_añadida = False

            while not posicion_añadida:
                tipo_premio = random.randint(0,8)
                posicion = random.randint(0,i)
                if self.premios[premios[tipo_premio]][0] > 0:
                    self.ruleta.insert(posicion ,premios[tipo_premio] )
                    self.premios[premios[tipo_premio]][0] -=1 
                    posicion_añadida = True
        # crea la ruleta

    @property 
    def puntero(self)-> int: 
        return self.__puntero
    
    @puntero.setter
    def puntero(self, puntero): 
        self.__puntero = self.__puntero 


    def ver(self, puntero:int= 0): 
        for i in range(len(self.ruleta)):
            if i == puntero: 
                print("->", end="")
            print(self.ruleta[i], end=", ")
        print()
    
    def devuelve_ruleta(self)-> list[str]: 
        return self.ruleta
    
    def devuelve_premio(self) -> int | float : 
        premio = self.ruleta[self.__puntero]
        return self.premios[premio][1] #Esta vez nos interesa el valor del premio 
    
    def girar(self, fuerza: int)-> int: 
        self.__puntero =(self.__puntero + fuerza) % 25
        return self.__puntero 
    
    def devuelve_posicion_puntero(self)-> int:
        return self.__puntero 
    
if __name__ == "__main__": 
    ruleta = Ruleta()
    ruleta.ver()
    puntero = ruleta.girar(25)
    print(ruleta.devuelve_premio())
    ruleta.ver(puntero)
    

