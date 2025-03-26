
import numpy as np

# Función para posicionar un solo barco aleatoriamente
def pos_barco_aleatorio(tablero, esl, ori):
    pos_barco = np.array([0, 0])
    pos = pos_barco + np.array([esl, esl])
    while pos[0] > len(tablero) or pos[1] + esl > len(tablero) or tablero[pos_barco[0]][pos_barco[1]] == "O":
        pos_barco = np.random.randint(0, len(tablero), 2)

    for fil, vec in enumerate(tablero):
        for col, val in enumerate(vec):
            if val != "O" and fil == pos_barco[0] and col == pos_barco[1]:
                if ori == "H":
                    tablero[fil, col:col + esl] = "O"
                else:
                    tablero[fil:fil + esl, col] = "O"
                return tablero
    return tablero

# Función que coloca todos los barcos según el diccionario de esloras
def pos_barcos_aleatorio(eslora, orientacion):
    tablero = np.full((10, 10), " ")
    for esl, cantidad in eslora.items():
        for _ in range(cantidad):
            ori = orientacion[np.random.randint(0, 2)]
            tablero = pos_barco_aleatorio(tablero, esl, ori)
    return tablero

# Antes esta función fallaba porque usaba variables globales como 'maquina' o 'jugador' que no existían aquí.
# Ahora le pasamos explícitamente el 'objetivo' del disparo como parámetro.
def disparo_coordenada(tablero_j, tablero_v, objetivo):
    x = int(input("Introduzca coordenada para X: "))
    y = int(input("Introduzca coordenada para Y: "))
    coordenada = (x, y)
    if tablero_j[coordenada] == "O":
        tablero_j[coordenada] = "X"  #  Se corrigió el uso de '==' (comparación) por '=' (asignación)
        tablero_v[coordenada] = "X"
        print("Buena puntería\n", tablero_v)
        objetivo.reduccion_vidas()
    else:
        tablero_v[coordenada] = "-"
        print("Has fallado")
    return tablero_v

# Igual que arriba, antes intentaba acceder a 'jugador' sin recibirlo.
# Ahora recibe el objetivo correctamente para bajarle vidas.
def disparo_maq(tablero_j, tablero_v, objetivo):
    x = np.random.randint(0, len(tablero_j))
    y = np.random.randint(0, len(tablero_j))
    coordenada = (x, y)
    if tablero_j[coordenada] == "O":
        tablero_j[coordenada] = "X"
        tablero_v[coordenada] = "X"
        print("Mala suerte! Te han dado")
        objetivo.reduccion_vidas()
    else:
        tablero_v[coordenada] = "-"
    return tablero_v

# Para mostrar los tableros uno al lado del otro
def visualizar_tableros(tablero1, tablero2):
    for vec1, vec2 in zip(tablero1, tablero2):
        print("| ", " ".join(vec1), " |     | ", " ".join(vec2), " |")
