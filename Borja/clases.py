"""
Clases usadas en "main.py"
last modification: Mar 15 2025
@authors:LV
"""
import numpy as np
from variables import vidas_j, eslora, orientacion
from funciones import pos_barcos_aleatorio, disparo_coordenada, disparo_maq, visualizar_tableros


class Jugador:

    eslora  = eslora
    orientacion = orientacion 
    vidas = vidas_j
    tablero_vacio  = np.full((10,10), " ") 
    
    def __init__(self, id_jugador, tablero_v = tablero_vacio , tablero_j = tablero_vacio , vidas = vidas_j):
        self.id = id_jugador
        self.tablero_v = tablero_v
        self.tablero_j = tablero_j
        self.vidas = vidas
        
    #introducir barcos en el tablero 
    def posicionar_barcos(self):
        #pos barcos aleatorios
        self.tablero_j= pos_barcos_aleatorio(self.eslora, self.orientacion)
        #pos_manual()
        #poner_barcos()
        #imprimir_tableros()
        return self. tablero_j

    
    #jugador en ese tablero, tendrás que comprobar si ahi
    #había un barco, o simplemente agua. 
    #Acuérdate de marcar en el tablero, tanto si hay un impacto,
    #como si dio agua.
    def disparo(self, user): 
        return disparo_coordenada(user.tablero_j, self.tablero_v)
    
    def disparo_maquina(self, jugador):
        
        return disparo_maq(jugador.tablero_j, self.tablero_v)
    
    def reduccion_vidas(self):
        self.vidas = self.vidas - 1
        print(f"A {self.id} le quedan {self.vidas} vidas")
        return self.vidas
    
    def contador_vidas(self):
        print(self.vidas)
        return self.vidas
    
    def marcador(self, user):
        print(f"El marcador es:\n"
              f"{self.id} ---- {self.vidas}  | {user.id} ----{user.vidas}")
    

    def imprimir_tablero(self):
        print(f"--->Tablero {self.id}<----->{self.vidas} vidas")
        print(self.tablero_j, self.tablero_v)
        
    def imprimir_tableros(self, maquina):
        self.maquina = maquina
        print(f"->Tablero {self.id}<->{self.vidas} vidas<--------->Tablero {self.maquina.id}<->{self.maquina.vidas} vidas")
        visualizar_tableros(self.tablero_j, self.maquina.tablero_j)

