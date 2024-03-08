from Vista import Vista
from Juego import Juego
from Controlador import Controlador

def letra_repetida(letra, letras): 
    return letra in letras

lista_jugadores = ["Nadia", "Veruska"]
letras = []
controlador = Controlador()
vista = Vista()
vocal_sin_comprar = True
while vocal_sin_comprar: 
    mismo_jugador = True
    while mismo_jugador: 
        opcion = Vista.mostrar_menu(vista)
        
        if opcion == 1: 
            letra = Vista.introducir_letra(vista)
            if not letra_repetida(letra, letras): 
                letras.append(letra)
                
            if controlador.es_vocal(letra): 
                vocal_sin_comprar = False
                vista.vocal_sin_comprar()

            elif letra_repetida(letra, letras): 
                jugador = 0 
                vista.decir_letra_esta_repetida(letra)
                jugador, mismo_jugador = jugador+1 , False
                

           
       