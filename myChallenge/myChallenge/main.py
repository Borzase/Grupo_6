

from clases import Jugador
from variables import *


#Después de eso ya comienza el juego. 
#Básicamente se irá ejecutando iterativamente en el while,
# y le irá preguntando coordenadas al usuario.

##Mensaje de bienvenida
print("Bienvenido a Hundir la flota grumete")

#Print Menu
def switch(opcion):
    diccionario = {
        1 : "instrucciones()",
        #2 : "id_jugador()",
        3 : "jugar()",
        4 : "salir()"
    }
    if opcion > 4:
        return print("Ingrese un numero 1 al 4")
    return eval (diccionario.get(opcion))



def instrucciones():
    print("""Intrucciones de Juego:
          =========================================
          - Hay dos jugadores, usted y la máquina
          - Sobre un tablero debe colocar la posicion de sus barcos
          - Cuenta con: 4 barcos de 1 posición de eslora
                        3 barcos de 2 posiciones de eslora
                        2 barcos de 3 posiciones de eslora
                        1 barco de 4 posiciones de eslora
          - Cada posición del barco cuenta como una vida
          - Tiene 10 posiciones en total, por lo que empieza con 10 vidas
          - Para disparar tiene que introducir unas coordenas
          - Si en las coordenas hay barco, le resta una vida a su oponente y sigue disparando
          - Si en las coordenas hay agua, no resta vidas y pierde su turno
          - Gana quien hunde todos los barcos del contrario
          - Pierde el que se ha quedado sin vidas
          ==========================================
          """)
    return
    

def id_jugador():
    nombre = input("Introduzca su nombre:")
    print(f"--->{nombre}, estamos creando tu tablero!<---")
    #Jugador(nombre)
    return nombre


def jugar():
    id = id_jugador()
    jugador = Jugador(id)
    
    # imprmir los tableros del jugador
    # Ejecutar posicionamiento barcos_maquina de manera aleatorio
    jugador.posicionar_barcos()
    jugador.imprimir_tablero()
    jugador.reduccion_vidas()
    
    
    maquina = Jugador("maquina")
    maquina.posicionar_barcos()
    maquina.imprimir_tablero()
    maquina.reduccion_vidas()
    

    
    #imprimir barcos_maquina para chequear que ha funcionadp
    #Empezar a jugar con un bucle while donde:
    #mientras las vidas del jugador o de la maquina no lleguen a "0" seguimos jugando
    #cuando while = 0 del jugador o de la maquina se rompe el bucle y salimos del juego
    while (jugador.vidas >7 and maquina.vidas > 7):
        # llamar a función disparar jugador
        jugador.disparo(maquina.tablero_j)
        jugador.reduccion_vidas()
        
        
        # llamar a funcion disparar de la maquina
        maquina.disparo_maquina(jugador.tablero_j)
        maquina.reduccion_vidas()
        jugador.imprimir_tablero()
        maquina.imprimir_tablero()
        
        # cada "x" disparos ofrecer posibilidad de visualizar
        #marcador o de salir del juego
        ####
        ####
    

def salir():
    print("Hasta pronto!")
    exit()
    

while(True):
    print("""Seleccione una opción:
    1 - Instrucciones de juego
    (no use) 2 - Introduzca su nombre de jugador
    3 - Comenzar a jugar
    4 - Salir del juego""")

    opcion = int(input())
    continuar = switch(opcion)
    if opcion > 4:
        print("Algo ha ido mal, intentalo de nuevo")
    
