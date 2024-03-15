
class Controlador: 
    def __eq__(self, otro): 
        return self == otro
    
    def es_vocal(self, letra): 
        vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü']
        if letra in vocales :
            return True
        
        