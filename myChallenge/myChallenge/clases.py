"""
Clases usadas en "main.py"
last modification: Mar 15 2025
@authors:LV
"""
from variables import dim_tablero, num_barcos
from funciones import *

class Jugador:

    tablero_barcos_jugador = dim_tablero
    tabler_vacio = dim_tablero
    num_barcos = num_barcos
    
    
    
    def __init__(self, id_jugador, tablero_vacio, tablero_juego):
        self.id = id_jugador
        self.tablero_v = tablero_vacio
        self.tablero_j = tablero_juego
        self.barcos = barcos
        
    #introducir barcos en el tablero 
    def posicionar_barcos(self, id_jugador):
        ###### poner aqui las funciones
        #pos_barcos_aleatorio()
        #pos_manual()
        #poner_barcos()
        #imprimir_tableros()
        pass
    
    #jugador en ese tablero, tendrás que comprobar si ahi
    #había un barco, o simplemente agua. 
    #Acuérdate de marcar en el tablero, tanto si hay un impacto,
    #como si dio agua.
    def disparo_coordenada(self, id_jugador, coordenada):
        self.coordenada = coordenada
        #comprobar_barco_existe()
        #poner_marca()
        