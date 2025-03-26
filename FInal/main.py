
from clases import Jugador
from variables import *

print("Bienvenido a Hundir la flota grumete")

def switch(opcion):
    diccionario = {
        1 : instrucciones,
        2 : id_jugador,
        3 : jugar,
        4 : salir
    }
    if opcion > 4:
        print("Ingrese un número del 1 al 4")
    else:
        return diccionario[opcion]()

def instrucciones():
    print("""Instrucciones de Juego:
    - Dos jugadores: tú y la máquina
    - Coloca tus barcos en el tablero
    - Tipos de barcos:
        4 barcos de 1 casilla
        3 barcos de 2 casillas
        2 barcos de 3 casillas
        1 barco de 4 casillas
    - Cada casilla equivale a una vida
    - Dispara por turnos hasta hundir toda la flota rival""")

def id_jugador():
    nombre = input("Introduce tu nombre: ")
    print(f"{nombre}, estamos creando tu tablero...")
    global jugador
    jugador = Jugador(nombre)
    return True

def jugar():
    # Esta función ahora maneja todo el ciclo del juego de forma clara
    global jugador
    print(f"Empecemos a jugar, {jugador.id}")
    
    jugador.posicionar_barcos()
    maquina = Jugador("máquina")
    maquina.posicionar_barcos()

    jugador.imprimir_tableros(maquina)

    # Bucle del juego. Jugador y máquina se disparan hasta que uno pierda todas las vidas.
    while jugador.vidas > 0 and maquina.vidas > 0:
        jugador.disparo(maquina)
        if maquina.vidas == 0: break

        maquina.disparo_maquina(jugador)
        if jugador.vidas == 0: break

        pregunta = input("""¿Qué quieres hacer ahora?
1: Seguir jugando
2: Ver marcador
3: Salir del juego
> """)
        if pregunta == "2":
            jugador.marcador(maquina)
        elif pregunta == "3":
            salir()
            break

    if jugador.vidas == 0:
        print(f"Has perdido, {jugador.id}")
    elif maquina.vidas == 0:
        print(f"¡Enhorabuena, {jugador.id}! Has ganado a la máquina.")

def salir():
    print("¡Hasta pronto!")
    exit()

while True:
    print("""Seleccione una opción:
1 - Instrucciones de juego
2 - Introducir nombre
3 - Comenzar a jugar
4 - Salir del juego""")
    try:
        opcion = int(input("> "))
        switch(opcion)
    except ValueError:
        print("Por favor, introduce un número válido.")
