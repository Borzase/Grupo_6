"""
Funciones usadas en "main.py"
"""
import numpy as np


# Posicion barco aleatoriamente
def pos_barco_aleatorio(tablero, esl, ori):
    
    pos_barco =  np.array([0, 0])
    pos_eslora = np.array([esl, esl])       # no le encuentro el sentido
    pos = pos_barco + pos_eslora
    while pos[0] >len(tablero) or pos[1]+esl >len(tablero) or tablero[pos_barco[0]][pos_barco[1]] == "O":
        pos_barco =  np.random.randint( 0, len(tablero), 2)


    for fil, vec in enumerate(tablero):
        for col, val in enumerate(vec):
            if val != "O":
                if fil == pos_barco[0] and col == pos_barco[1]: 
                    if ori == "H":
                        tablero[fil:fil+1,col:col+esl] = "O"
                    else:
                        tablero[fil:fil+esl,col:col+1] = "O"
                        
                    tablero_new = tablero
    
    return tablero_new

# Posicionar barcos aleatoriamente
def pos_barcos_aleatorio(eslora, orientacion):
    tablero  = np.full((10,10), " ") 
    for esl, barcos in eslora.items():
        for barco in range(barcos):            
            ori = orientacion[np.random.randint( 0, 2)] 
            tablero_new = pos_barco_aleatorio(tablero, esl, ori)
            tablero = tablero_new 
    
    return tablero

    
#poner barcos en el tablero pidiendole al jugador coordenadas
def posicionar_barcos(tablero_jugador, coordenadas):
    for x in coordenadas:
        tablero_jugador[x] = "O"
        print("Barco colocado correctamente")
    return tablero_jugador


#comprobar barco exite
#poner marca X(disparo), O (barco) o - (agua)
def disparo_coordenada(tablero_j, tablero_v):        #disparo del jugador a la maquina
                                                        # tablero_juego_maquina(barcos), tablero_v_jugador
    x = int(input("Introduzca coordenada para X:"))
    y = int(input("Introduzca coordenada para Y:"))
    coordenada = (x, y)
    if tablero_j[coordenada] == "O":
        tablero_j[coordenada] == "X"
        tablero_v[coordenada] = "X"
        print("Buena punteria\n", tablero_v)
        maquina.reduccion_vidas()
        print("Tiene otro disparo")
        return jugador.disparo(maquina)
    elif tablero_j[coordenada] != "O":
        tablero_v[coordenada]  = "-"
        print("Has fallado")
        print(tablero_v, jugador.tablero_j)
        
    return 


def disparo_maq(tablero_j, tablero_v):           # disparo de la maquina al jugador
    x =  np.random.randint( 0, len(tablero_j)-1, size = 1)
    y =  np.random.randint( 0, len(tablero_j)-1, Size = 1)
    coordenada = (x, y)
    if tablero_j[coordenada] == "O":
        tablero_j[coordenada] == "X"
        tablero_v[coordenada] = "X"
        print("Mala suerte! Te han dado")
        jugador.reduccion_vidas()
        return maquina.disparo_maquina(jugador)
    elif tablero_j[coordenada] != "O":
        tablero_v[coordenada]  = "-"        
    return tablero


def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"
    return tablero


def visualizar_tableros(tablero1, tablero2):

    for vec1, vec2 in zip(tablero1, tablero2):
        print("| "," ".join(vec1)," |          ","| "," ".join(vec2)," |")
    

