import numpy as np

def pos_barco_aleatorio(tablero, esl, ori):
    colocado = False
    while not colocado:
        fila, col = np.random.randint(0, len(tablero)), np.random.randint(0, len(tablero))
        if ori == "H":
            if col + esl > len(tablero):
                continue
            if np.any(tablero[fila, col:col + esl] == "O"):
                continue
            tablero[fila, col:col + esl] = "O"
            colocado = True
        else:
            if fila + esl > len(tablero):
                continue
            if np.any(tablero[fila:fila + esl, col] == "O"):
                continue
            tablero[fila:fila + esl, col] = "O"
            colocado = True
    return tablero

def pos_barcos_aleatorio(eslora, orientacion):
    tablero = np.full((10, 10), " ")
    for esl, cantidad in eslora.items():
        for _ in range(cantidad):
            ori = orientacion[np.random.randint(0, 2)]
            tablero = pos_barco_aleatorio(tablero, esl, ori)
    return tablero

def disparo_coordenada(maquina):
#def disparo_coordenada(tablero_j, tablero_v, objetivo):
    x = int(input("Introduzca coordenada para la FILA (0-9): "))
    y = int(input("Introduzca coordenada para la COLUMNA (0-9): "))
    coordenada = (x, y)
    if maquina.tablero_j[coordenada] == "O":
        maquina.tablero_j[coordenada] = "X"
        maquina.tablero_v[coordenada] = "X"
        print("Buena puntería!\n")
        maquina.reduccion_vidas()
        print("Tira otra vez! \n")
        return maquina, True
    else:
        maquina.tablero_j[coordenada] = "-"
        maquina.tablero_v[coordenada] = "-"
        print("Has fallado!\n")
        
    # COMENTARIO: Mostramos ambos tableros claramente tras el disparo
    #print("Tu tablero (barcos propios) a la izquierda  ||  Tablero enemigo (disparos) a la derecha")
    #visualizar_tableros(objetivo.tablero_j, tablero_v)
    return maquina, False

def disparo_maq(user):
    x = np.random.randint(0, len(user.tablero_j))
    y = np.random.randint(0, len(user.tablero_j))
    coordenada = (x, y)
    if user.tablero_j[coordenada] == "O":
        user.tablero_j[coordenada] = "X"
        user.tablero_v[coordenada] = "X"
        print("Mala suerte! Te han dado")
        user.reduccion_vidas()
        return user, True
    else:
        user.tablero_j[coordenada] = "-"
        user.tablero_j[coordenada] = "-"
    return user, False

def visualizar_tableros(tablero1, tablero2):
    # COMENTARIO: Antes los tableros estaban muy juntos y no se distinguía bien cuál era cuál.
    # Ahora se agregan títulos, números de columnas, y separación clara para una visualización más ordenada.

    #print("      TÚ                         MÁQUINA")
    print("   " + " ".join(str(i) for i in range(10)) + "           " + " ".join(str(i) for i in range(10)))
    for i, (fila1, fila2) in enumerate(zip(tablero1, tablero2)):
        fila_str = f"{i}  " + " ".join(fila1) + "           " + " ".join(fila2)
        print(fila_str)