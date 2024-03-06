import random
random.seed(1)

class Tarjetas(): 
    fichero_enigma : str
    lista_enigmas: list[str]
    enigma: str
    
    def __init__(self) -> None:
        self.lista_enigmas = []
        self.tematicas_disponibles = ["Normal", "San Valentín"]
        self.enigma = "" #Hay que protegerlos
        
    def abrir(self, fichero_enigma: str ): 
        enigmas_select = open(("./Ficheros/" + fichero_enigma + ".txt"), "r", encoding="utf-8")
        self.lista_enigmas = enigmas_select.readlines()
        enigmas_select.close()
    
    def devolver_random(self): 
        num = random.randint(1, len(self.lista_enigmas)-1)
        return num

    def devolver_enigma_aleatorio(self, tematica):
        self.abrir(self.tematicas_disponibles[tematica])
        num = self.devolver_random()
        self.enigma = self.lista_enigmas[num]
        return self.enigma
        # self.enigma_generado = self.enigma.devolver_enigma()

    def devolver_enigma(self)->str: 
        return self.enigma
    
if __name__ == "__main__": 
    t1 = Tarjetas()  
    t1.abrir("Normal") 
    print(t1.devolver_enigma_aleatorio())
    # print(t1.devolver_enigma_aleatorio())
    print(t1.devolver_enigma())