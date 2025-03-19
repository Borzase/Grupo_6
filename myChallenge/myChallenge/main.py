

from clases import Jugador


#Después de eso ya comienza el juego. 
#Básicamente se irá ejecutando iterativamente en el while,
# y le irá preguntando coordenadas al usuario.

##MEnsaje de bienvenida
print("Bienvenido a Hundir la flota grumete")


def intrucciones():
    print("""Intrucciones de Juego:
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
          - Pierde el que se ha quedado sin vidas""")
    return
    

def id_jugador():
    nombre = input("Introduzca su nombre")
    print(f"{nombre}, ¿Estás listo para jugar?")
    Jugador(nombre)
    return Jugador(nombre)

    

def jugar():
    jugador1 = Jugador(id_jugador())
    vidas_jugador1 = 10         #quizas haya que hacer alguna funcion para esto
    vidas_maquina = 10
    jugador1.barco4_1()
    jugador1.barco3_2()
    jugador1.barco2_3()
    jugador1.barco1_4()
       
    Jugador.dim_tablero   # imprmir los tableros del jugador
    # Ejecutar posicionamiento barcos_maquina de manera aleatorio
        #imprimir barcos_maquina para chequear que ha funcionadp
    #Empezar a jugar con un bucle while donde:
    #mientras las vidas del jugador o de la maquina no lleguen a "0" seguimos jugando
                    #cuando while = 0 del jugador o de la maquina se rompe el bucle y salimos del juego
        # llamar a función disparar jugador
            #........
        # llamar a funcion disparar de la maquina
            #.........
        # cada "x" disparos ofrecer posibilidad de visualizar marcador o de salir del juego
    
    

def salir():
    pass 

def switch(opcion):
    diccionario = {
        1 : "instrucciones()",
        2 : "id_jugador()",
        3 : "jugar()",
        4 : "salir()"
    }
    if opcion > 4:
        return
    return eval (diccionario.get(opcion))
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
    


