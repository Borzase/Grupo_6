

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
        2 : "id_jugador()",
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
    jugador = Jugador(nombre)
    return True


def jugar():
    from clases import Jugador
    
    print(f"Empecemos a jugar {jugador.id}")
    
    # imprmir los tableros del jugador
    # Ejecutar posicionamiento barcos_maquina de manera aleatorio
    jugador.posicionar_barcos()
    jugador.imprimir_tablero()
    
    
    maquina = Jugador("maquina")
    maquina.posicionar_barcos()
    maquina.imprimir_tablero()
    
    

    
    #imprimir barcos_maquina para chequear que ha funcionadp
    #Empezar a jugar con un bucle while donde:
    #mientras las vidas del jugador o de la maquina no lleguen a "0" seguimos jugando
    #cuando while = 0 del jugador o de la maquina se rompe el bucle y salimos del juego
    jugador.vidas
    maquina.vidas
    while (jugador.vidas != 0 or maquina.vidas != 0):
        # llamar a función disparar jugador
        for x in range(4):
            jugador.imprimir_tablero()
            jugador.disparo(maquina)
                
            maquina.disparo_maquina(jugador)
        
            jugador.contador_vidas()
            maquina.contador_vidas()
        
        pregunta = int(input("""Indique el número con su decision:
                         1: Seguir jugando
                         2: Visualizar marcador
                         3: Salir del juego"""))
        if pregunta == 1:
            return ("sigamos jugando")
        elif pregunta == 2:
            jugador.marcador(maquina)
            break
        elif pregunta == 3:
            break
    

    if jugador.vidas == 0:
        print(f"Has perdido {jugadaor.id}")

    if maquina.vidas == 0:
        print(f"Enhorabuena, {jugador.id} le has ganado a la máquina")

        
    return   
        #jugador.imprimir_tablero()
        #maquina.imprimir_tablero()
        
        
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
    2 - Introduzca su nombre de jugador
    3 - Comenzar a jugar
    4 - Salir del juego""")

    opcion = int(input())
    continuar = switch(opcion)
    if opcion > 4:
        print("Algo ha ido mal, intentalo de nuevo")
    
