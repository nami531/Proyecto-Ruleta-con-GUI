import time
# from TarjetasAntiguoSinPistas import Tarjetas
from Jugador import Jugador
from Ruleta import Ruleta
import os

class Vista: 
    SALIR: int = 4
    OPCIONES_TURNO_JUG: list[str] = ["1.Letra", "2.Comprar vocal", "3.Resolver enigma", "4.Salir"]
    tematicas_disponibles : list[str]
    enigma_generado : str

    def __init__(self):
        self.enigma_generado = ""
        self.tematicas_disponibles = ["Normal", "San Valentín", "Carnaval", "Comida", "Python"]
        self.SALIR = 5

    @staticmethod
    def borrar_pantalla(segundos: int = 2)-> None: 
        time.sleep(segundos)
        os.system("cls")

    def bienvenida(self)-> str: 
        return "Bienvenido a la ruleta"
    
#     def establecer_num_jugadores(self)-> int:
#         num= int(input("¿Cuántos jugadores van a jugar?: "))
#         self.borrar_pantalla(1)
#         return num
    
    def pedir_nombre_jugador(self, i:int)-> str:      
        return f"Jugador {i+1}"
    
#     def mostrarJugadores(self, lista : list[Jugador])-> None:
#         for i in range(len(lista)): 
#             print(f"\nJugador {i+1}: {lista[i]}\n" )  
#         self.borrar_pantalla()
            
#     def establecer_tematica(self)-> int: 
#         for i in range(len(self.tematicas_disponibles)): 
#             print(i+1,".", self.tematicas_disponibles[i], end="\n")
#         tematica = int(input("De las temáticas anteriores elige una: "))
#         self.borrar_pantalla()
#         return tematica - 1 
    
    def turno(self, jugador: Jugador)-> str: 
        return f"Jugador {jugador.nombre} es tu turno, gira la ruleta"
    
    def aviso_medicion_fuerza(self) -> str: 
        return "Midamos fuerzas: Presiona la barra espaciadora tanto como puedas para girar la ruleta"

    
    def mostrar_premio(self, puntero: int, ruleta : Ruleta)-> str:
        lista = ruleta.devuelve_ruleta()  
        return lista[puntero]
    
    def caer_en(self): 
        return "Has caído en..."
  

#     def mostrar_ruleta(self, ruleta: list[str], __puntero: int = 0)-> None: 
#         for i in range(len(ruleta)):
#             if i == __puntero: 
#                 print("->", end="")
#             print(ruleta[i], end=", ")
#         print()
#         self.borrar_pantalla(5)

    def introducir_letra(self) -> str: 
        return "Introduce una letra: "
    
    def mostrar_enigma(self, enigma: str)-> None:
        print(enigma)
    
    def mostrar_pista(self, pista: str)-> None: 
        print(pista)
        self.borrar_pantalla(5)
    
    def mostrar_enigma_encriptado(self, enigma)-> str: #Pylance da error si se pone el type hints en tal caso es enigma:str
        enigma = enigma.split()
        enigma_encriptado = "" #Lo convertimos en lista
        for palabra in enigma:  
            enigma_encriptado += (len(palabra)*"_")
        enigma_encriptado += " " 
        return enigma_encriptado
    
    def mostrar_panel_cifrado(self, enigma:str, letra:str, letras: list[str], vocales: list[str]):  
        lista_enigma = enigma.split()
        enigma_encriptado = ""
        for palabras in lista_enigma: 
            for char in palabras:
                if (char.lower() != letra) and ((char.lower() not in letras) and (char.lower() not in vocales)): 
                    enigma_encriptado += "_"
                else: 
                    enigma_encriptado += char 
            enigma_encriptado += " "
        return enigma_encriptado
        
    def decir_letra_esta_repetida(self, letra: str): 
        return f"Lo siento, la letra {letra}, está repetida, has perdido el turno"

    def decir_letra_no_aparece(self, letra:str): 
        return f"Lo siento, la letra {letra}, no existe en este enigma, has perdido el turno"   

    def vocal_sin_comprar(self):
        return "Lo siento, no puedes decir una vocal sin haberla comprado antes, vuelve a intentarlo"
    

    def decir_letra_pierdeTurno(self):
        return "Lo siento, acabas de caer en pierde Turno, por tanto pierdes el turno"

    def comprar_letra_no_vocal(self): 
        return "Lo siento, no puedes comprar esa letra porque no es una vocal."
        

    def letra_en_comprar_vocal(self): 
        return "Lo siento, has intentado comprar una letra la cual no es vocal, vuelve a intentarlo"
        

    def saldo_insuficiente(self): 
        return "Lo siento, no puedes comprar la vocal porque no tienes suficiente dinero"
        

    def no_resolviste_panel(self): 
        return "No has resuelto el panel :("
        

    def panel_resuelto(self):
        return "Has resuelto el panel!"
        

    def has_ganado(self, jugador: Jugador): 
        return f"{jugador.nombre} has ganado. Te llevas {jugador.puntuacion}"



    def longitud_incorrecta(self): 
        return "Entrada inválida, Introduce una letra"
    
    def decir_adios(self): 
        return "¡Adiós! Os esperamos de vuelta"
        
# if __name__ == "__main__": 
#     vista = Vista()
#     vista.mostrar_premio(7)