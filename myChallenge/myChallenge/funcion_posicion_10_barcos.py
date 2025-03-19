


def barco4_1():
    barcos = {"barco1": [],
               "barco2": [],
               "barco3": [],
               "barco4": []}
    for clave, valor in barcos.items():
        x = int(input("Introducza su coordenada para el eje X"))
        y = int(input("Introducza su coordenada para el eje Y"))
        coor = (x, y)
        barcos[clave] = valor.append(coor)
    
    barco_1 = posicionar_barcos(tablero_jugador, barcos["barco1"])
    barco_2 = posicionar_barcos(tablero_jugador, barcos["barco2"])
    barco_3 = posicionar_barcos(tablero_jugador, barcos["barco3"])
    barco_4 = posicionar_barcos(tablero_jugador, barcos["barco4"])
    return tablero_jugador


def barco3_2():
    barcos = {"barco1": [],
               "barco2": [],
               "barco3": []}
    for clave, valor in barcos.items():
            for num in range(2):
                x = int(input("Introducza su coordenada para el eje X"))
                y = int(input("Introducza su coordenada para el eje Y"))
                coor = (x, y) 
                barcos[clave] = valor.append(coor)
    barco_5 = posicionar_barcos(tablero_jugador, barcos["barcos1"])
    barco_6 = posicionar_barcos(tablero_jugador, barcos["barcos2"])
    barco_7 = posicionar_barcos(tablero_jugador, barcos["barcos3"])
    
    return tablero_jugador

        

def barco2_3():
    barcos = {"barco1": [],
               "barco2": []
               }

    for clave, valor in barcos.items():
            for num in range(3):
                x = int(input("Introducza su coordenada para el eje X"))
                y = int(input("Introducza su coordenada para el eje Y"))
                coor = (x, y) 
                barcos[clave] = valor.append(coor)
    barco_8 = posicionar_barcos(tablero_jugador, barcos["barcos1"])
    barco_9 = posicionar_barcos(tablero_jugador, barcos["barcos2"])
    
    return tablero_jugador


def barco1_4():
    barco10 = []
    for num in range(4):
        x = int(input("Introducza su coordenada para el eje X"))
        y = int(input("Introducza su coordenada para el eje Y"))
        coor = (x, y) 
        barco10.append(coor)
    barco_10 = posicionar_barcos(tablero_jugador, barco10)
    return tablero_jugador