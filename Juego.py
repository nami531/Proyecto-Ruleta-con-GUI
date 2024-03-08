from Vista import Vista
from Jugador import Jugador
from Ruleta import Ruleta
from Tarjetas import Tarjetas
from Controlador import Controlador
from Listener import Listener
import pygame
from os import system
import time


class Juego(): 
    vista : Vista
    jugador : Jugador
    ruleta: Ruleta
    enigma : Tarjetas
    enigma_juego : str
    lista_jugadores: list[Jugador] #Hay que protegerlo
    letras : list[str]
    vocales : list[str]


    def __init__(self):  
        self.controlador = Controlador()
        self.vista = Vista()
        self.ruleta = Ruleta()
        self.lista_jugadores = []
        self.precio = 100 

    def anhadirJugador(self, jugador: Jugador):
        self.lista_jugadores.append(jugador)
    
    def letra_repetida(self, letra): 
        return letra in self.letras
    
    def letra_no_aparece(self, letra): 
        return letra not in self.enigma_juego.lower()

    def apariciones(self, letra: str)-> int: 
        return self.enigma_juego.count(letra)

    def acceder_puntos(self, jugador: int) -> list: 
        return self.lista_jugadores[jugador]._puntuacion 

    def comprobaciones_al_introducir(self, letra : str)-> bool : #Comprueba todos los fallos, en caso de no ejecutarse ninguno, devolverá True
        if self.letra_repetida(letra): 
            self.vista.decir_letra_esta_repetida(letra)
            return False

        elif self.letra_no_aparece(letra):      
            self.vista.decir_letra_no_aparece(letra)
            return False
        return True         

    def comprobaciones_juego(self,jugador:int,  premio: int |float)-> bool: 
        if premio == -1: 
            self.vista.decir_letra_pierdeTurno()
            return False
        elif premio == 0: 
            self.lista_jugadores[jugador].en_quiebra(premio)
            return False
        elif premio == 0.5: 
            self.lista_jugadores[jugador].perder_mitad(premio)
        return True
              
    def jugar(self): 
        self.vista.bienvenida()

        num_jugadores = self.vista.establecer_num_jugadores()
        for i in range(num_jugadores):
            nombre= self.vista.pedir_nombre_jugador(i).capitalize()
            jugadorCreado = Jugador(nombre)
            self.anhadirJugador(jugadorCreado)

        self.vista.mostrarJugadores(self.lista_jugadores)
        # Proceso de añadir jugadores al juego

        pygame.init()
        tematica = self.vista.establecer_tematica()
        self.enigma = Tarjetas(tematica)
        self.enigma_juego = self.enigma.devolver_enigma_aleatorio()
        self.pista_enigma = self.enigma.devolver_pista()
        self.vista.mostrar_enigma_encriptado(self.enigma_juego)
        # self.vista.mostrar_enigma(self.enigma_juego) #Habría que quitar esto, pq si no no tiene gracia jeje
        self.vista.mostrar_pista(self.pista_enigma) 
        self.letras = []
        self.vocales = []
        turno = True 
        index_jugador = 0 
        jugador = self.lista_jugadores[index_jugador]
        # Proceso de establecer el enigma y la temática de este, se repetirá según las rondas que se jueguen

        while turno:   
                
            fuerza = 0            
            self.vista.turno(jugador)
            self.vista.aviso_medicion_fuerza()
            time.sleep(1)


            fuerza = Listener().medir_fuerza()
            self.vista.borrar_pantalla()
            jugador.girar_ruleta(self.ruleta, fuerza)  #Se tiene que pasar la ruleta con la que se esta iniciando el juego si no exisitirían 2 ruletas
            self.vista.mostrar_premio(self.ruleta.puntero, self.ruleta)
            self.vista.mostrar_ruleta(self.ruleta.devuelve_ruleta(), self.ruleta.puntero)
            premio = self.ruleta.devuelve_premio()
            # Proceso de girar la ruleta
            
            mismo_jugador = True

            while mismo_jugador: 
                if self.comprobaciones_juego(index_jugador, premio): #Esta comprobacion está para que se pueda ejecutar el juego aunque caigas en la mitad
                    opcion = self.vista.mostrar_menu()

                    if opcion == 1: 
                        
                        letra = self.vista.introducir_letra()
                        if self.controlador.es_vocal(letra): #Esto se encuentra aquí porque no debe estar en las comprobaciones comunes
                            self.vista.vocal_sin_comprar()
                        

                        elif self.comprobaciones_al_introducir(letra):  
                            self.letras.append(letra)
                            self.vista.mostrar_panel_cifrado(self.enigma_juego, letra, self.letras, self.vocales)
                            jugador.ganar_puntuacion(premio, self.apariciones(letra))
                            mismo_jugador = False 
                        else: 
                            index_jugador, mismo_jugador = jugador.perder_turno( index_jugador, self.lista_jugadores)

                    elif opcion == 2: 
                        letra = self.vista.introducir_letra()
                        if not self.controlador.es_vocal(letra): 
                            self.vista.letra_en_comprar_vocal()
                            
                        elif self.comprobaciones_al_introducir(letra): 
                            if jugador.comprar_vocal(letra, self.precio):
                                self.letras.append(letra) 
                                self.vista.mostrar_panel_cifrado(self.enigma_juego, letra, self.letras, self.vocales)
                                jugador.ganar_puntuacion(premio)
                            mismo_jugador = False

                    elif opcion == 4: 
                        jugador.comprobar_puntuacion()
                    
                    elif opcion == 3: 

                        enigma_jugador = self.vista.introducir_letra()
                        resuelto = jugador.resolver_enigma(self.enigma_juego, enigma_jugador)
                        if resuelto: 
                            jugador.ganar_puntuacion(premio)
                            self.vista.panel_resuelto()
                            self.vista.has_ganado(jugador) 
                            jugador.comprobar_puntuacion() #Preguntar a marta
                            turno, mismo_jugador = False, False
                        else: 
                            self.vista.no_resolviste_panel()
                            index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores) 

                    elif opcion == self.vista.SALIR:
                        print("ADIOS!") 
                        turno, mismo_jugador = False, False
                else:
                    index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores)
    

if __name__ == "__main__": 
    ruleta = Ruleta()
    prueba_juego = Juego()
    prueba_juego.jugar()


    
