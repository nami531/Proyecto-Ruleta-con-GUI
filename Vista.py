import time
from Tarjetas import Tarjetas
from Jugador import Jugador
from Ruleta import Ruleta

class Vista(): 
    SALIR = 5
    OPCIONES_TURNO_JUG: list[str] = ["1.Letra", "2.Comprar vocal", "3.Resolver enigma", "4.Comprobar puntuación"]
    tematicas_disponibles : list[str]
    ruleta: Ruleta
    enigma_generado : str

    def __init__(self):
        self.enigma = Tarjetas()
        self.enigma_generado = ""
        self.tematicas_disponibles = ["Normal", "San Valentín"]
        self.SALIR = 5
        self.ruleta = Ruleta()



    def bienvenida(self): 
        print("Bienvenido a la ruleta de la fortuna")
    
    def pedir_nombre_jugador(self, i): 
        nombre = input(f"Jugador {i+1} ¿Cuál es tu nombre?: ")
        return nombre
    
    def introducir_letra(self) -> str: 
        letra = input("Introduce una letra: ").lower()
        return letra
    
    def mostrar_menu(self): 
        opcion = 0 
        while opcion < 1 or opcion > Vista.SALIR: 
            for opcion_jug in range(len(Vista.OPCIONES_TURNO_JUG)): 
                print(Vista.OPCIONES_TURNO_JUG[opcion_jug])
                time.sleep(1)
            opcion = int(input("Escoge una opción: "))      #Hay que comprobar la opción 
        return opcion

    def mostrar_premio(self, puntero: int, ruleta : Ruleta):
        lista = ruleta.devuelve_ruleta()
        print("Has caído en", end="")
        for i in range(3): 
            print(".", end="")
            time.sleep(1)
        print(f"\n{lista[puntero]}")

    def turno(self, jugador: Jugador): 
        print(f"Jugador {jugador.nombre} es tu turno, gira la ruleta")
    
    def establecer_num_jugadores(self):
        num= int(input("¿Cuántos jugadores van a jugar?: "))
        return num
    
    def establecer_tematica(self): 
        for i in range(len(self.tematicas_disponibles)): 
            print(i+1,".", self.tematicas_disponibles[i], end="\n")
        tematica = int(input("De las temáticas anteriores elige una "))
        return tematica -  1 
    # def mostrar_enigma(self, tarjeta: Tarjeta): 
    #     if respuesta_correcta: 
             
    #         print(enigma)
    def mostrar_enigma(self, enigma):
        
        print(enigma)
    
    def mostrar_enigma_encriptado(self, enigma): 
        enigma = enigma.split() #Lo convertimos en lista
        for palabra in enigma:  
            print(len(palabra)*"_", end=" ")
        print(" ", end="")
    
    

 
        
    def decir_letra_esta_repetida(self, letra: str): 
        print(f"Lo siento, la letra {letra}, está repetida, has perdido el turno")

    def decir_letra_no_aparece(self, letra:str): 
        print(f"Lo siento, la letra {letra}, no existe en este enigma, has perdido el turno")
    
    def vocal_sin_comprar(self):
        print("Lo siento, no puedes decir una vocal sin haberla comprado antes, vuelve a intentarlo")
    
    def decir_letra_pierdeTurno(self):
        print("Lo siento, acabas de caer en pierde Turno, por tanto pierdes el turno")

    def comprar_letra_no_vocal(self): 
        print("Lo siento, no puedes comprar esa letra porque no es una vocal.")

    def letra_en_comprar_vocal(self): 
        print("Lo siento, has intentado comprar una letra la cual no es vocal, vuelve a intentarlo")

    def saldo_insuficiente(self): 
        print("Lo siento, no puedes comprar la vocal porque no tienes suficiente dinero")
    
    def no_resolviste_panel(self): 
        print("No has resuelto el panel :(")

    def panel_resuelto(self):
        print("Has resuelto el panel!")
    
    def has_ganado(self, jugador: Jugador): 
        print(f"{jugador.nombre} has ganado. Te llevas {jugador.puntuacion}")

    def mostrar_panel_cifrado(self, enigma:str, letra:str, letras: list[str], vocales: list[str]):  
        lista_enigma = enigma.split()
        for palabras in lista_enigma: 
            for char in palabras:
                if (char.lower() != letra) and ((char.lower() not in letras) and (char.lower() not in vocales)): 
                    print("_", end="")
                else: 
                    print(char, end="") 
            print(" ", end="")
        print()
        
if __name__ == "__main__": 
    vista = Vista()
    vista.mostrar_premio(7)