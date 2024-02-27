import random
random.seed(1)

class Tarjetas(): 
    fichero_enigma : str
    enigmas_pistas: dict[str, str]
    enigma: str
    
    def __init__(self) -> None:
        self.tematicas_disponibles = ["Normal", "San Valentín"]
        self.enigma = "" #Hay que protegerlos
        
    def abrir(self, fichero_enigma: str ): 
        enigmas_select = open(("./Ficheros/" + fichero_enigma + ".txt"), "r", encoding="utf-8") #Cambiarlo cuando tenga los ficheros a una carpeta
        lista_enigmas = enigmas_select.readlines()
        enigmas_select.close()
        pistas = open(("./Ficheros/" + fichero_enigma + "Pistas.txt"), "r", encoding="utf-8")
        lista_pistas = pistas.readlines()
        pistas.close()
        return lista_enigmas, lista_pistas
    
    def crear_dic_pistas_enigmas(self, fichero_enigma): 
        lista_enigmas, lista_pistas = self.abrir(fichero_enigma: str)
        for i in range(len(lista_enigmas)): 
            self.enigmas_pistas[lista_enigmas[i]] = lista_pistas[i] #Creo que es al reves, pero weno, se cambia y ya

    def devolver_enigma_aleatorio(self, tematica):
        self.abrir(self.tematicas_disponibles[tematica])
        num = random.randint(1, len(self.enigmas_pistas)-1)
        lista_claves = self.enigmas_pistas.keys()
        self.pista = lista_claves[num]
        self.enigma = self.enigmas_pistas[self.pista]
        return self.enigma
        # self.enigma_generado = self.enigma.devolver_enigma()

    def devolver_enigma(self)->str: 
        return self.enigma
    
    def devolver_pista(self)->str: 
        return self.pista
    
    
if __name__ == "__main__": 
    t1 = Tarjetas()  
    t1.abrir("Normal") 
    print(t1.devolver_enigma_aleatorio())
    # print(t1.devolver_enigma_aleatorio())
    print(t1.devolver_enigma())