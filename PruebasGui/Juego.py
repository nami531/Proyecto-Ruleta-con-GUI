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
    vista: Vista
    jugador: Jugador
    ruleta: Ruleta
    enigma: Tarjetas
    enigma_juego: str
    __lista_jugadores: list[Jugador]
    letras: list[str]
    vocales: list[str]
    vocales_tilde: dict[str, str]
    ventana: Ventana
    controlador: Controlador
    _error: int
    _precio: int
    _letra: str
    _perder_turno: bool
    _opcion_ejecucion: bool


    def __init__(self):  
        self.controlador = Controlador()
        self.vista = Vista()
        self.ruleta = Ruleta()
        self.__lista_jugadores = []
        self.vocales_tilde = {"a": "á",
                              "e": "é",
                              "i": "í",
                              "o": "ó",
                              "u" : "úü"
                              }
        self.precio = 100 
        self.ventana = Ventana()

    @property
    def lista_jugadores(self) -> list[Jugador]:
        return self.__lista_jugadores
    
    @lista_jugadores.setter
    def lista_jugadores(self, jugadores: list[Jugador]):
        self.__lista_jugadores = jugadores

    @property
    def error(self) -> int:
        return self._error
    
    @error.setter
    def error(self, valor: int):
        self._error = valor

    @property
    def precio(self) -> int:
        return self._precio
    
    @precio.setter
    def precio(self, valor: int):
        if valor >= 0:
            self._precio = valor
        else:
            self._precio = 0

    @property
    def letra(self) -> str:
        return self._letra
    
    @letra.setter
    def letra(self, valor: str):
        self._letra = valor

    @property
    def perder_turno(self) -> bool:
        return self._perder_turno
    
    @perder_turno.setter
    def perder_turno(self, valor: bool):
        self._perder_turno = valor

    @property
    def opcion_ejecucion(self) -> bool:
        return self._opcion_ejecucion
    
    @opcion_ejecucion.setter
    def opcion_ejecucion(self, valor: bool):
        self._opcion_ejecucion = valor

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
            self.letra = VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales)
            return False
        
        elif self.letra_repetida(self.letra): 
            self.error = 2
            VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales)
            self.opcion_ejecucion = False 
            return False

        elif self.letra_no_aparece(self.letra):      
            self.error = 3
            VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[i], self.error,self.letras, self.vocales) 
            self.opcion_ejecucion = False            
            return False 
        return True            


    def comprobaciones_juego(self,jugador:int,  premio: int |float)-> bool: #Comprueba el premio donde cayó el jugador
        if premio == -1: 
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

        tematica = VentanaTematica().ejecutar()
        self.enigma = Tarjetas(tematica)
        self.enigma_juego = self.enigma.devolver_enigma_aleatorio()
        self.pista_enigma = self.enigma.devolver_pista()

        self.letras = []
        self.vocales = []
        self.enigma_encriptado = self.vista.mostrar_panel_cifrado(self.enigma_juego, "", self.letras, self.vocales)
        
        turno = True 
        index_jugador = 0 
        VentanaPanel().ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
        
        # Proceso de establecer el enigma y la temática de este, se repetirá según las rondas que se jueguen

        while turno:   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            jugador = self.lista_jugadores[index_jugador]        

            fuerza = VentanaFuerza().ejecutar(jugador)

            jugador.girar_ruleta(self.ruleta, fuerza)  #Se tiene que pasar la ruleta con la que se esta iniciando el juego si no exisitirían 2 ruletas

            premio = self.ruleta.devuelve_premio()
            VentanaPremio().ejecutar(self.ruleta.puntero, self.ruleta, premio)
            # Proceso de girar la ruleta
            
            mismo_jugador = True

            while mismo_jugador: 
                if self.comprobaciones_juego(index_jugador, premio): #Esta comprobacion está para que se pueda ejecutar el juego aunque caigas en el premio mitad
                    self.error = 0 
                    opcion = VentanaMenu().ejecutar(jugador)

                    if opcion == 1: 
                        self.perder_turno = True
                        self.opcion_ejecucion = True 
                        self.letra = VentanaPanelEntrada().ejecutar(jugador, self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        while self.opcion_ejecucion: 
                            if self.controlador.es_vocal(self.letra): #Esto se encuentra aquí porque no debe estar en las comprobaciones comunes
                                self.vista.vocal_sin_comprar()
                                self.error = 4
                                self.letra = VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, self.lista_jugadores[index_jugador], self.error,self.letras, self.vocales)

                            elif self.comprobaciones_al_introducir(index_jugador):  
                                self.letras.append(self.letra)
                                self.vista.mostrar_panel_cifrado(self.enigma_juego, self.letra, self.letras, self.vocales)
                                jugador.ganar_puntuacion(premio, self.apariciones(self.letra))
                                VentanaPanel().ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                                mismo_jugador = False 
                                self.opcion_ejecucion = False
                                self.perder_turno = False
                        if self.perder_turno:   
                            index_jugador, mismo_jugador = jugador.perder_turno( index_jugador, self.lista_jugadores)
                        

                    elif opcion == 2:
                        self.opcion_ejecucion = True 
                        self.perder_turno = True
                        self.letra = VentanaPanelEntrada().ejecutar(jugador, self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        while self.opcion_ejecucion: 
                           
                            if not self.controlador.es_vocal(self.letra): 
                                self.error = 5
                                self.letra = VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, jugador, self.error, self.letras, self.vocales, self.letra)
                                
                            if self.comprobaciones_al_introducir(index_jugador): 
                                vocal_comprada = jugador.comprar_vocal(self.letra, self.precio)
                                if not vocal_comprada:
                                    self.error = 6
                                    VentanaError().ejecutar(self.enigma_juego, self.pista_enigma, jugador, self.error, self.letras, self.vocales, self.letra)
                                    self.opcion_ejecucion = False
                                else: 
                                    self.letras.append(self.letra) 
                                    for j in self.vocales_tilde[self.letra]: 
                                        self.letras.append(j)
                                    self.vista.mostrar_panel_cifrado(self.enigma_juego, self.letra, self.letras, self.vocales)
                                    jugador.ganar_puntuacion(premio)
                                    VentanaPanel().ejecutar(self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                                    mismo_jugador = False
                                    self.opcion_ejecucion = False
                                    self.perder_turno = False
                            else: 
                                self.opcion_ejecucion = False
                        if self.perder_turno: 
                            index_jugador, mismo_jugador = jugador.perder_turno( index_jugador, self.lista_jugadores)

                    elif opcion == 3: 
                        enigma_jugador = VentanaPanelEntrada().ejecutar(jugador, self.enigma_juego, self.pista_enigma, self.letras, self.vocales)
                        resuelto = jugador.resolver_enigma(self.enigma_juego, enigma_jugador)
                        if resuelto: 
                            jugador.ganar_puntuacion(premio)
                            VentanaResolucion().ejecutar(jugador, resuelto)
                            jugador.comprobar_puntuacion()
                            turno, mismo_jugador = False, False
                        else: 
                            self.vista.no_resolviste_panel()
                            VentanaResolucion().ejecutar(jugador, resuelto)
                            index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores) 

                    elif opcion == Vista.SALIR:
                        VentanaAdios().ejecutar()
                        turno, mismo_jugador = False, False
                else:
                    index_jugador, mismo_jugador = jugador.perder_turno(index_jugador, self.lista_jugadores)
    

if __name__ == "__main__": 
    pygame.init()
    prueba_juego = Juego()
    
    prueba_juego.jugar()


    
