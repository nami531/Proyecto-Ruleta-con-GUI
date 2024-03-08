import random
random.seed(1)

class Tarjetas(): 
    fichero_enigma : str
    __enigmas_pistas: dict[str, str]
    __enigma: str
    pista : str
    __lista_enigmas : list[str]
    __lista_pistas : list[str]
    
    def __init__(self, fichero: int) -> None:
        self.__tematicas_disponibles = ["Normal", "San Valentín", "Carnaval", "Comida", "Python"]
        self.__enigma = "" #Hay que protegerlos
        self.__lista_enigmas = []
        self.__lista_pistas = []
        self.__enigmas_pistas = {}

        #Proceso de generar la lista de pistas y enigmas
        with open(("./Ficheros/" +  self.__tematicas_disponibles[fichero] +"/"+ self.__tematicas_disponibles[fichero]   + ".txt"), "r", encoding="utf-8") as ficheroEnigma: 
            for linea in ficheroEnigma: 
                self.lista_enigmas.append(linea.rstrip().replace(", ", " ").replace(". ", " ").replace(": ", " ")) #Elimina el \n y reemplaza cualquier coma y puntos
        
        with open(("./Ficheros/" + self.__tematicas_disponibles[fichero]  +"/"+ self.__tematicas_disponibles[fichero]  + "Pistas.txt"), "r", encoding="utf-8") as ficheroPistas:
            for linea in ficheroPistas: 
                self.lista_pistas.append(linea.rstrip())

        self.crear_dic_pistas_enigmas()

    @property
    def tematicas_disponibles(self):
        return self.__tematicas_disponibles

    @tematicas_disponibles.setter
    def tematicas_disponibles(self, tematicas):
        self.__tematicas_disponibles = self.__tematicas_disponibles

    @property
    def enigma(self):
        return self.__enigma

    @enigma.setter
    def enigma(self, value):
        self.__enigma = value

    @property
    def lista_enigmas(self):
        return self.__lista_enigmas

    @lista_enigmas.setter
    def lista_enigmas(self, value):
        self.lista_enigmas = self.lista_enigmas

    @property
    def lista_pistas(self):
        return self.__lista_pistas

    @lista_pistas.setter
    def lista_pistas(self, value):
        self.lista_pistas = self.lista_pistas

    @property
    def enigmas_pistas(self):
        return self.__enigmas_pistas

    @enigmas_pistas.setter
    def enigmas_pistas(self, value):
        self.enigmas_pistas = self.enigmas_pistas

    def crear_dic_pistas_enigmas(self): 
        for i in range(len(self.lista_enigmas)): 
            self.enigmas_pistas[self.lista_pistas[i]] = self.lista_enigmas[i] 

    def devolver_enigma_aleatorio(self):
        num = random.randint(1, len(self.enigmas_pistas)-1)
        
        self.pista = list(self.__enigmas_pistas)[num]
        self.__enigma = self.__enigmas_pistas[self.pista]
        return self.__enigma


    def devolver_enigma(self)->str: 
        return self.__enigma
    
    def devolver_pista(self)->str: 
        return self.pista
    
    
if __name__ == "__main__": 
    t1 = Tarjetas(4)  
    print(t1.devolver_enigma_aleatorio())
    # print(t1.devolver_enigma_aleatorio())
    print(t1.devolver_enigma())
    print(t1.devolver_pista())