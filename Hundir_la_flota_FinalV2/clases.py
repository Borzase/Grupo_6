import numpy as np
from variables import vidas_j, eslora, orientacion
from funciones import pos_barcos_aleatorio, disparo_coordenada, disparo_maq, visualizar_tableros

class Jugador:
    eslora = eslora
    orientacion = orientacion 
    vidas = vidas_j

    def __init__(self, id_jugador, tablero_v=None, tablero_j=None, vidas=vidas_j):
        # COMENTARIO: Antes todos los jugadores compartían el mismo tablero vacío, lo cual podía dar errores
        # raros como que un disparo se reflejara en el tablero del otro jugador. Esto se debía a que en Python
        # no se debe usar un objeto mutable como valor por defecto. Ahora usamos None y creamos una matriz nueva.
        self.id = id_jugador
        self.tablero_v = tablero_v if tablero_v is not None else np.full((10,10), " ")
        self.tablero_j = tablero_j if tablero_j is not None else np.full((10,10), " ")
        self.vidas = vidas
        
    def posicionar_barcos(self):
        self.tablero_j = pos_barcos_aleatorio(self.eslora, self.orientacion)
        return self.tablero_j

    def disparo(self, user):
        repetir = True
        while repetir  == True:
            user, repetir = disparo_coordenada(user)
            
        return user
    
    def disparo_maquina(self, jugador):
        repetir  = True
        while repetir == True:
            jugador, repetir = disparo_maq(jugador)
            
        return jugador
    
    def reduccion_vidas(self):
        self.vidas -= 1
        print(f"A {self.id} le quedan {self.vidas} vidas")
        return self.vidas
    
    def contador_vidas(self):
        print(self.vidas)
        return self.vidas
    
    def marcador(self, user):
        
        print(f"El marcador es:\n{self.id} --> {10-user.vidas} | {user.id} ---> {10-self.vidas}")

    def imprimir_tablero(self):
        # COMENTARIO: Ahora usamos el mismo formato visual que después de los disparos
        print("Tu tablero (barcos propios) a la izquierda  ||  Tablero enemigo (disparos recibidos) a la derecha")
        visualizar_tableros(self.tablero_j, self.tablero_v)
        
    def imprimir_tableros(self, maquina): 
        print(f"-> {self.id} <-> {maquina.vidas} vidas <-----> {maquina.id} <-> {self.vidas} vidas")
        visualizar_tableros(self.tablero_j, maquina.tablero_v)
