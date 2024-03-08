import random
random.seed(1)

class Tarjetas(): 
    fichero_enigma : str
    enigmas_pistas: dict[str, str]
    enigma: str
    pista : str
    lista_enigmas : list[str]
    lista_pistas : list[str]
    
    def __init__(self, fichero: int) -> None:
        self.tematicas_disponibles = ["Normal", "San Valentín", "Carnaval", "Comida", "Python"]
        self.enigma = "" #Hay que protegerlos
        self.lista_enigmas = []
        self.lista_pistas = []
        self.enigmas_pistas = {}

        #Proceso de generar la lista de pistas y enigmas
        with open(("./Ficheros/" +  self.tematicas_disponibles[fichero] +"/"+ self.tematicas_disponibles[fichero]   + ".txt"), "r", encoding="utf-8") as ficheroEnigma: 
            for linea in ficheroEnigma: 
                self.lista_enigmas.append(linea.rstrip().replace(", ", " ").replace(". ", " ").replace(": ", " ")) #Elimina el \n y reemplaza cualquier coma y puntos
        
        with open(("./Ficheros/" + self.tematicas_disponibles[fichero]  +"/"+ self.tematicas_disponibles[fichero]  + "Pistas.txt"), "r", encoding="utf-8") as ficheroPistas:
            for linea in ficheroPistas: 
                self.lista_pistas.append(linea.rstrip())

        self.crear_dic_pistas_enigmas()

    def crear_dic_pistas_enigmas(self): 
        for i in range(len(self.lista_enigmas)): 
            self.enigmas_pistas[self.lista_pistas[i]] = self.lista_enigmas[i] #Creo que es al reves, pero weno, se cambia y ya

    def devolver_enigma_aleatorio(self):
        num = random.randint(1, len(self.enigmas_pistas)-1)
        
        self.pista = list(self.enigmas_pistas)[num]
        self.enigma = self.enigmas_pistas[self.pista]
        return self.enigma
        # self.enigma_generado = self.enigma.devolver_enigma()

    def devolver_enigma(self)->str: 
        return self.enigma
    
    def devolver_pista(self)->str: 
        return self.pista
    
    
if __name__ == "__main__": 
    t1 = Tarjetas(4)  
    print(t1.devolver_enigma_aleatorio())
    # print(t1.devolver_enigma_aleatorio())
    print(t1.devolver_enigma())
    print(t1.devolver_pista())