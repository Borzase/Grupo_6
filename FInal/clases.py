
"""
Clases usadas en "main.py"
last modification: Mar 15 2025
@authors:LV
"""
import numpy as np
from variables import vidas_j, eslora, orientacion
from funciones import pos_barcos_aleatorio, disparo_coordenada, disparo_maq, visualizar_tableros

class Jugador:
    eslora = eslora
    orientacion = orientacion 
    vidas = vidas_j
    tablero_vacio = np.full((10,10), " ") 
    
    def __init__(self, id_jugador, tablero_v=tablero_vacio, tablero_j=tablero_vacio, vidas=vidas_j):
        self.id = id_jugador
        self.tablero_v = tablero_v
        self.tablero_j = tablero_j
        self.vidas = vidas
        
    def posicionar_barcos(self):
        # Usa una función que coloca los barcos aleatoriamente según las esloras definidas
        self.tablero_j = pos_barcos_aleatorio(self.eslora, self.orientacion)
        return self.tablero_j

    def disparo(self, user): 
        # Antes fallaba por no pasar el objetivo a la función. Ahora se pasa explícitamente.
        return disparo_coordenada(user.tablero_j, self.tablero_v, user)
    
    def disparo_maquina(self, jugador):
        # Igual que arriba, ahora la máquina recibe correctamente al jugador como objetivo
        return disparo_maq(jugador.tablero_j, self.tablero_v, jugador)
    
    def reduccion_vidas(self):
        self.vidas -= 1
        print(f"A {self.id} le quedan {self.vidas} vidas")
        return self.vidas
    
    def contador_vidas(self):
        print(self.vidas)
        return self.vidas
    
    def marcador(self, user):
        print(f"El marcador es:\n{self.id} ---- {self.vidas}  | {user.id} ---- {user.vidas}")

    def imprimir_tablero(self):
        print(f"---> Tablero {self.id} <-----> {self.vidas} vidas")
        print(self.tablero_j, self.tablero_v)
        
    def imprimir_tableros(self, maquina):
        # Versión más clara que imprime ambos tableros con sus vidas
        print(f"-> Tablero {self.id} <-> {self.vidas} vidas <---------> Tablero {maquina.id} <-> {maquina.vidas} vidas")
        visualizar_tableros(self.tablero_j, maquina.tablero_j)
