import time
from Tarjetas import Tarjetas
from Jugador import Jugador
from Ruleta import Ruleta
import os

class Vista: 
    SALIR = 5
    OPCIONES_TURNO_JUG: list[str] = ["1.Letra", "2.Comprar vocal", "3.Resolver enigma", "4.Comprobar puntuación", "5.Salir"]
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

    def bienvenida(self)-> None: 
        print('''#####    #######  ####     ###  ##  ###  ##  ####     ###  ##  #######  #####     #####              ###             ##         ###             ######   ###  ##  ##       ####     #######    ###
##  ##     ###    ##       ###  ##  ###  ##  ##       ###  ##    ###    ### ##   ###  ##            #####            ##        #####            ###  ##  ###  ##  ##       ##       #######   #####
#####      ###    #####    #### ##  ###  ##  #####    #### ##    ###    ###  ##  ###  ##            ## ##            ##        ## ##            ###  ##  ###  ##  ##       #####    #######   ## ##
##  ##     ###    ##       #######  ###  ##  ##       #######    ###    ###  ##  ###  ##           ##   ##           ##       ##   ##           #######  ###  ##  ##       ##         ###    ##   ##
##  ###    ###    ##       #######  ###  ##  ##       #######    ###    ### ###  ###  ##           ##   ##           ##       ##   ##           ######   ###  ##  ##       ##         ###    ##   ##
#######  #######  #######  ### ###   #####   #######  ### ###  #######  #######  #######           ## ####           #######  ## ####           ### ###  #######  #######  #######    ###    ## ####
######   #######  #######  ###  ##   #####   #######  ###  ##  #######  #######  #######           ## ####           #######  ## ####           ### ###  #######  #######  #######    ###    ## ####
######   #######  #######  ###  ##    ###    #######  ###  ##  #######  ######    #####            ## ####           #######  ## ####           ### ###  #######  #######  #######    ###    ## ####''')
        self.borrar_pantalla()
    
    def establecer_num_jugadores(self)-> int:
        num= int(input("¿Cuántos jugadores van a jugar?: "))
        self.borrar_pantalla(1)
        return num
    
    def pedir_nombre_jugador(self, i:int)-> str: 
        nombre = input(f'''+-------------------------------------+
|   Jugador {i+1} ¿Cuál es tu nombre?:    |  
+-------------------------------------+\n''')
        self.borrar_pantalla(1)
        return nombre
    
    def mostrarJugadores(self, lista : list[Jugador])-> None:
        for i in range(len(lista)): 
            print(f"\nJugador {i+1}: {lista[i]}\n" )  
        self.borrar_pantalla()
            
    def establecer_tematica(self)-> int: 
        for i in range(len(self.tematicas_disponibles)): 
            print(i+1,".", self.tematicas_disponibles[i], end="\n")
        tematica = int(input("De las temáticas anteriores elige una: "))
        self.borrar_pantalla()
        return tematica - 1 
    
    def turno(self, jugador: Jugador)-> None: 
        print(f"Jugador {jugador.nombre} es tu turno, gira la ruleta")
        self.borrar_pantalla()
    
    def aviso_medicion_fuerza(self) -> None: 
        print("Cuando desaparezca este mensaje, tendrás 5 segundos para presionar cualquier tecla lo más rápido posible")
        self.borrar_pantalla()
    
    def mostrar_premio(self, __puntero: int, ruleta : Ruleta)-> None:
        lista = ruleta.devuelve_ruleta()
        print("Has caído en", end="")
        for i in range(3): 
            print(".", end="")
            time.sleep(1)
        time.sleep(2)
        print(f"\n{lista[__puntero]}")
  

    def mostrar_ruleta(self, ruleta: list[str], __puntero: int = 0)-> None: 
        for i in range(len(ruleta)):
            if i == __puntero: 
                print("->", end="")
            print(ruleta[i], end=", ")
        print()
        self.borrar_pantalla(5)


    def mostrar_menu(self)-> int: 
        opcion = 0 
        while opcion < 1 or opcion > Vista.SALIR: 
            for opcion_jug in range(len(Vista.OPCIONES_TURNO_JUG)): 
                print(Vista.OPCIONES_TURNO_JUG[opcion_jug])
                time.sleep(1)
            opcion = int(input("Escoge una opción: "))      #Hay que comprobar la opción 
        self.borrar_pantalla(1)
        return opcion


    def introducir_letra(self) -> str: 
        letra = input("Introduce una letra: ").lower()
        self.borrar_pantalla()
        return letra
    
    def mostrar_enigma(self, enigma: str)-> None:
        print(enigma)
    
    def mostrar_pista(self, pista: str)-> None: 
        print(pista)
        self.borrar_pantalla(5)
    
    def mostrar_enigma_encriptado(self, enigma)-> None: #Pylance da error si se pone el type hints en tal caso es enigma:str
        enigma = enigma.split() #Lo convertimos en lista
        for palabra in enigma:  
            print(len(palabra)*"_", end=" ")
        print(" ", end="")
    
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
        self.borrar_pantalla(5)
    

    def decir_letra_esta_repetida(self, letra: str): 
        print(f"Lo siento, la letra {letra}, está repetida, has perdido el turno")
        self.borrar_pantalla(5)

    def decir_letra_no_aparece(self, letra:str): 
        print(f"Lo siento, la letra {letra}, no existe en este enigma, has perdido el turno")
        self.borrar_pantalla(5)   

    def vocal_sin_comprar(self):
        print("Lo siento, no puedes decir una vocal sin haberla comprado antes, vuelve a intentarlo")
        self.borrar_pantalla(5)

    def decir_letra_pierdeTurno(self):
        print("Lo siento, acabas de caer en pierde Turno, por tanto pierdes el turno")
        self.borrar_pantalla(5)

    def comprar_letra_no_vocal(self): 
        print("Lo siento, no puedes comprar esa letra porque no es una vocal.")
        self.borrar_pantalla(5)

    def letra_en_comprar_vocal(self): 
        print("Lo siento, has intentado comprar una letra la cual no es vocal, vuelve a intentarlo")
        self.borrar_pantalla(5)

    def saldo_insuficiente(self): 
        print("Lo siento, no puedes comprar la vocal porque no tienes suficiente dinero")
        self.borrar_pantalla(5)

    def no_resolviste_panel(self): 
        print("No has resuelto el panel :(")
        self.borrar_pantalla(5)

    def panel_resuelto(self):
        print("Has resuelto el panel!")
        self.borrar_pantalla(5)

    def has_ganado(self, jugador: Jugador): 
        print(f"{jugador.nombre} has ganado. Te llevas {jugador.puntuacion}")
        self.borrar_pantalla(5)

    def decir_adios(self): 
        print("ADIÓS!")

    def comodin(self): 
        print("Te salvaste, tienes un comodin")
        self.borrar_pantalla()

    def longitud_incorrecta(self): 
        print("Entrada inválida, Introduce una letra")
        self.borrar_pantalla()
    
        
