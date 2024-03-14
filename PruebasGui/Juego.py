from Jugador import Jugador
from Ruleta import Ruleta
from Tarjetas import Tarjetas
from Controlador import Controlador
import pygame
from os import system
import sys
import time
from Ventana import Ventana
from VentanaTematica import VentanaTematica
from Vista import Vista
from VentanaPanel import VentanaPanel
from VentanaMenu import VentanaMenu
from VentanaFuerza import VentanaFuerza
from VentanaPremio import VentanaPremio
from VentanaPanelEntrada import VentanaPanelEntrada
from VentanaError import VentanaError
from VentanaResolucionEnigma import VentanaResolucion
from VentanaAdios import VentanaAdios

class Juego(): 
    vista : Vista
    jugador : Jugador
    ruleta: Ruleta
    enigma : Tarjetas
    enigma_juego : str
    lista_jugadores: list[Jugador] #Hay que protegerlo
    letras : list[str]
    vocales : list[str]
    vocales_tilde: dict[str, str]
    ventana : Ventana


    def __init__(self):  
        self.controlador = Controlador()
        self.vista = Vista()
        self.ruleta = Ruleta()
        self.lista_jugadores = []
        self.vocales_tilde = {"a": "á",
                              "e": "é",
                              "i": "í",
                              "o": "ó",
                              "u" : "úü"
                              }
        self.precio = 100 
        self.ventana = Ventana(800, 600)
        self.ventanaError = VentanaError(800,600)

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

    def comprobaciones_al_introducir(self, i= 0)-> bool: #Comprueba todos los fallos, en caso de no ejecutarse ninguno, devolverá True
        if len(self.letra) > 1: 
            self.error = 1
            self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales)
            return False
        
        elif self.letra_repetida(self.letra): 
            self.error = 2
            self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales)
            return False

        elif self.letra_no_aparece(self.letra):      
            self.error = 3
            self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales)            
            return False 
        return True            


    def comprobaciones_juego(self,jugador:int,  premio: int |float)-> bool: #Comprueba el premio donde cayó el jugador
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
       
        nom_jugadores = self.ventana.ejecutar()
        for i in range(len(nom_jugadores)):
            nombre= nom_jugadores[i]
            jugadorCreado = Jugador(nombre)
            self.anhadirJugador(jugadorCreado)

        print(self.lista_jugadores)
        # self.vista.mostrarJugadores(self.lista_jugadores)
        # Proceso de añadir jugadores al juego


        tematica = VentanaTematica(800,600).ejecutar()
        self.enigma = Tarjetas(tematica)
        self.enigma_juego = self.enigma.devolver_enigma_aleatorio()
        self.pista_enigma = self.enigma.devolver_pista()

        self.letras = []
        self.vocales = []
        self.enigma_encriptado = self.vista.mostrar_panel_cifrado(self.enigma_juego, "", self.letras, self.vocales)
        
        # self.vista.mostrar_enigma(self.enigma_juego) #Habría que quitar esto, pq si no no tiene gracia jeje
        self.vista.mostrar_pista(self.pista_enigma) 
        
        
        turno = True 
        index_jugador = 0 
        VentanaPanel(800, 600).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
        
        # Proceso de establecer el enigma y la temática de este, se repetirá según las rondas que se jueguen

        while turno:   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            jugador = self.lista_jugadores[index_jugador]        

            fuerza = VentanaFuerza(800, 600).ejecutar(jugador)

            jugador.girar_ruleta(self.ruleta, fuerza)  #Se tiene que pasar la ruleta con la que se esta iniciando el juego si no exisitirían 2 ruletas
            
            # self.vista.mostrar_ruleta(self.ruleta.devuelve_ruleta(), self.ruleta.puntero)
            premio = self.ruleta.devuelve_premio()
            VentanaPremio(800,600).ejecutar(self.ruleta.puntero, self.ruleta, premio)
            # Proceso de girar la ruleta
            
            mismo_jugador = True

            while mismo_jugador: 
                if self.comprobaciones_juego(index_jugador, premio): #Esta comprobacion está para que se pueda ejecutar el juego aunque caigas en la mitad
                    self.error = 0 
                    opcion = VentanaMenu(800, 600, jugador).ejecutar()

                    if opcion == 1: 
                        opcion1_ejecucion = True 
                        self.letra = VentanaPanelEntrada(800,600, jugador).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        while opcion1_ejecucion: 
                            if self.controlador.es_vocal(self.letra): #Esto se encuentra aquí porque no debe estar en las comprobaciones comunes
                                self.vista.vocal_sin_comprar()
                                self.error = 4
                                self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[index_jugador], self.error,self.letras, self.vocales)

                                
                            elif self.comprobaciones_al_introducir(index_jugador):  
                                self.letras.append(self.letra)
                                self.vista.mostrar_panel_cifrado(self.enigma_juego, self.letra, self.letras, self.vocales)
                                jugador.ganar_puntuacion(premio, self.apariciones(self.letra))
                                VentanaPanel(800,600).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                                mismo_jugador = False 
                                opcion1_ejecucion = False
                            else: 
                                index_jugador, mismo_jugador = jugador.perder_turno( index_jugador, self.lista_jugadores)
                                opcion1_ejecucion = False

                    elif opcion == 2:
                        opcion2_ejecucion = True 
                        self.letra = VentanaPanelEntrada(800,600, jugador).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        while opcion2_ejecucion: 
                           
                            if not self.controlador.es_vocal(self.letra): 
                                self.error = 5
                                self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, jugador, self.error, self.letras, self.vocales, self.letra)
                                
                            if self.comprobaciones_al_introducir(index_jugador): 
                                vocal_comprada = jugador.comprar_vocal(self.letra, self.precio)
                                if not vocal_comprada:
                                    self.error = 6
                                    self.letra = self.ventanaError.ejecutar(self.enigma_juego, self.pista_enigma, jugador, self.error, self.letras, self.vocales, self.letra)
                                    opcion2_ejecucion = False
                                else: 
                                    self.letras.append(self.letra) 
                                    for j in self.vocales_tilde[self.letra]: 
                                        self.letras.append(j)
                                    self.vista.mostrar_panel_cifrado(self.enigma_juego, self.letra, self.letras, self.vocales)
                                    jugador.ganar_puntuacion(premio)
                                    VentanaPanel(800,600).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                                    mismo_jugador = False
                            else: 
                                opcion2_ejecucion = False

                    elif opcion == 3: 
                        enigma_jugador = VentanaPanelEntrada(800,600, jugador).ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        resuelto = jugador.resolver_enigma(self.enigma_juego, enigma_jugador)
                        if resuelto: 
                            jugador.ganar_puntuacion(premio)
                            VentanaResolucion(800, 600).ejecutar(jugador, resuelto)#Ventana
                            # self.vista.has_ganado(jugador) 
                            jugador.comprobar_puntuacion()
                            turno, mismo_jugador = False, False
                        else: 
                            self.vista.no_resolviste_panel() #Ventana
                            VentanaResolucion(800, 600).ejecutar(jugador, resuelto)
                            index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores) 

                    elif opcion == Vista.SALIR:
                        VentanaAdios(800,600).ejecutar()
                        turno, mismo_jugador = False, False
                else:
                    index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores)
    

if __name__ == "__main__": 
    pygame.init()
    prueba_juego = Juego()
    
    prueba_juego.jugar()


    
