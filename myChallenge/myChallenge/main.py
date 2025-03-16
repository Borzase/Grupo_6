# -*- coding: utf-8 -*-
"""
variables usadas en "main.py"
last modification: Mar 16 2025
@author: lupe, borja, edit, sara
"""

from clases import Jugador



#Después de eso ya comienza el juego. 
#Básicamente se irá ejecutando iterativamente en el while,
# y le irá preguntando coordenadas al usuario.

##MEnsaje de bienvenida
print("=============Bienvenid@======================")
vidas = 1

while (vidas !=0):
    
    # Menu para iniciar (llamar a las funciones)
    
    # Opcion 1: id = input("Como te llamas?")
    # Opcion 2: Ver instrucciones del juego
    # Opcion 3: Jugar--->inicializar tableros
    # Opcion 5: Dejar de jugar 
    print("===Menu====")

    ##Use a switch()
    
    #1.inicializar tableros
    #2. maquina debe ingresar barcos aleatoriamente
    #3.jugador debe ingresar las coordenadas

    #Ejemplo de uso de clase Jugador
    id = "Juanito"
    jugador1 = Jugador(id)
    print(jugador1.dim_tablero)
    print(jugador1.tablero_v)

    vidas -=1
    
    


