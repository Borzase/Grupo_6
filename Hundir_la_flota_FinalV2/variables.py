"""
variables usadas en "main.py"
last modification: Mar 16 2025
@authors:LUPE, jORGE, FERNANDO, BORJA
"""
import numpy as np 


vidas_j = 10         

orientacion = ["H", "V"]  #horizontal and vertical
"""
  4 barcos de 1 posición de eslora
  3 barcos de 2 posiciones de eslora
  2 barcos de 3 posiciones de eslora
  1 barco de 4 posiciones de eslora
"""
eslora = { 1: 4, 2: 3 , 3: 2, 4: 1} #eslora: num_barcos