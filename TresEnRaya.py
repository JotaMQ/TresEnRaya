import random
import time
import os
import sys

# Función para limpiar la pantalla
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Función para pintar TresEnRaya
def TresEnRaya():
    print(" _______            ______       _____                   ")
    print("|__   __|          |  ____|     |  __ \                  ")
    print("   | |_ __ ___  ___| |__   _ __ | |__) |__ _ _   _  __ _ ")
    print("   | | '__/ _ \/ __|  __| | '_ \|  _  // _` | | | |/ _` |")
    print("   | | | |  __/\__ \ |____| | | | | \ \ (_| | |_| | (_| |")
    print("   |_|_|  \___||___/______|_| |_|_|  \_\__,_|\__, |\__,_|")
    print("                                              __/ |      ")
    print("                                             |___/       ")

# Función para pintar el cartón
def pintarCarton(carton):
    for i, fila in enumerate(carton):
        if i == 0:
            print("    0   1   2  ")
            print("  +---+---+---+")

        print(i, "|", end="")

        for casilla in fila:
            print("", casilla, "", end="|")

        print()
        print("  +---+---+---+")

# Función para tachar la casilla correspondiente
def marcarCasilla(usuario, turno):
    usuario = str(usuario)

    for i, digito in enumerate(usuario):
        if i == 0:
            digitoUno = int(digito)

        elif i == 1:
            digitoDos = int(digito)
        
    carton[digitoUno][digitoDos] = turno

# Función para comprobar el ganador
def comprobarGanador(carton, turno):
    ganador = 0

    # Comprobar Horizontal
    for fila in carton:
        horizontal = 0
        for elemento in fila:
            if elemento == turno:
                horizontal += 1

            if horizontal == 3:
                clear()
                ganador += 1
                print("El ganador es", turno)
                final = input("Pulsa cualquier tecla para continuar")
                return ganador
        
    # Comprobar vertical
    vertical = [0, 0, 0]
    for iFila in range(3):
        for iColumna in range(3):
            if carton[iFila][iColumna] == turno:
                vertical[iColumna] += 1

            if vertical[iColumna] == 3:
                clear()
                ganador += 1
                print("El ganador es", turno)
                final = input("Pulsa cualquier tecla para continuar")
                return ganador
            
    # Comprobar diagonal
    if carton[0][0] == turno:
        if carton[1][1] == turno:
            if carton[2][2] == turno:
                clear()
                ganador += 1
                print("El ganador es", turno)
                final = input("Pulsa cualquier tecla para continuar")
                return ganador
    
    elif carton[0][2] == turno:
        if carton[1][1] == turno:
            if carton[2][0] == turno:
                clear()
                ganador += 1
                print("El ganador es", turno)
                final = input("Pulsa cualquier tecla para continuar")
                return ganador

# Función para que la IA juegue
# -----------------------------------------------------
# Explicación de las variables de la función:
# -----------------------------------------------------
# dificultad = Dificultad seleccionada por el jugador
# turnoJugador = Hace referencia al simbolo del jugador, es decir X o O
# turno = Hace referencia al simbolo de la IA, es decir X o O
# carton = Variable dónde se juega la partida
def dificultadIA(dificultad, turno, turnoJugador, carton):
    time.sleep(1)

    opciones = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    opcionAleatoria = random.sample(opciones, len(opciones))

    # Dificultad fácil
    if dificultad == 1:
        # Pinta de manera aleatoría
        for opcion in opcionAleatoria:
            for i, digito in enumerate(opcion):
                if i == 0:
                    digitoUno = int(digito)

                elif i == 1:
                    digitoDos = int(digito)
            
            if not (carton[digitoUno][digitoDos] == "o" or carton[digitoUno][digitoDos] == "x"):
                return opcion

    # Dificultad difícil
    elif dificultad == 2:
        # Si no hay nada en el centro lo pinta
        if carton[1][1] == " ":
                opcion = "11"
                return opcion  
        
        # Revisa que hay pintado en el cartón
        horizontal = [0, 0, 0]
        horizontalPropia = [0, 0, 0]
        vertical = [0, 0, 0]
        verticalPropia = [0, 0, 0]
        
        for iFila, fila in enumerate(carton):
            for iElemento, elemento in enumerate(fila):
                if elemento == turnoJugador:   
                    horizontal[iFila] += 1
                    horizontalPropia[iFila] -= 1
                    vertical[iElemento] += 1
                    verticalPropia[iElemento] -= 1

                elif elemento == turno:
                        horizontal[iFila] -= 1
                        horizontalPropia[iFila] += 1
                        vertical[iElemento] -= 1
                        verticalPropia[iElemento] += 1

        # Revisa lo que hay pintado en las diagonales del cartón
        diagonalIzquierda = 0
        diagonalIzquierdaPropia = 0
        diagonalDerecha = 0
        diagonalDerechaPropia = 0

        # Diagonal izquierda
        if carton[0][0] == turnoJugador:
            diagonalIzquierda += 1
        if carton[1][1] == turnoJugador:
            diagonalIzquierda += 1
        if carton[2][2] == turnoJugador:
            diagonalIzquierda += 1

        if carton[0][0] == turno:
            diagonalIzquierdaPropia += 1
        if carton[1][1] == turno:
            diagonalIzquierdaPropia += 1
        if carton[2][2] == turno:
            diagonalIzquierdaPropia += 1
        
        diagonalIzquierdaPropia = diagonalIzquierda - diagonalIzquierdaPropia

        # Diagonal derecha
        if carton[0][2] == turnoJugador:
            diagonalDerecha += 1
        if carton[1][1] == turnoJugador:
            diagonalDerecha += 1
        if carton[2][0] == turnoJugador:
            diagonalDerecha += 1

        if carton[0][2] == turno:
            diagonalDerechaPropia += 1
        if carton[1][1] == turno:
            diagonalDerechaPropia += 1
        if carton[2][0] == turno:
            diagonalDerechaPropia += 1

        diagonalDerechaPropia = diagonalDerecha - diagonalDerechaPropia

        # Si ve que puede ganar con una raya horizontal actua
        if (horizontalPropia[0] == 2 or horizontalPropia[1] == 2 or horizontalPropia[2] == 2):
            for iFila, fila in enumerate(horizontalPropia):
                if fila == 2:
                    if carton[iFila][0] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "0"
                        return opcion
                    
                    elif carton[iFila][1] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "1"
                        return opcion
                    
                    elif carton[iFila][2] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "2"
                        return opcion

        # Si ve que puede ganar con una raya vertical actua
        elif (verticalPropia[0] == 2 or verticalPropia[1] == 2 or verticalPropia[2] == 2):
            for iColumna, columna in enumerate(verticalPropia):
                if columna == 2:
                    if carton[0][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "0" + opcion
                        return opcion
                    
                    elif carton[1][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "1" + opcion
                        return opcion
                    
                    elif carton[2][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "2" + opcion
                        return opcion

        # Si ve que puede ganar con una diagonal izquierda actua
        elif diagonalIzquierdaPropia == 2:
            if carton[0][0] == " ":
                opcion = "00"
                return opcion
            
            elif carton[1][1] == " ":
                opcion = "11"
                return opcion
            
            elif carton[2][2] == " ":
                opcion = "22"
                return opcion

        # Si ve que puede ganar con una diagonal derecha actua
        elif diagonalDerechaPropia == 2:
            if carton[0][2] == " ":
                opcion = "02"
                return opcion
            
            elif carton[1][1] == " ":
                opcion = "11"
                return opcion
            
            elif carton[2][0] == " ":
                opcion = "20"
                return opcion

        # Si ve posibilidad de raya horizontal enemiga actua
        elif (horizontal[0] == 2 or horizontal[1] == 2 or horizontal[2] == 2):
            for iFila, fila in enumerate(horizontal):
                if fila == 2:
                    if carton[iFila][0] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "0"
                        return opcion
                    
                    elif carton[iFila][1] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "1"
                        return opcion
                    
                    elif carton[iFila][2] == " ":
                        opcion = str(iFila)
                        opcion = opcion + "2"
                        return opcion
                       
        # Si ve posibilidad de raya vertical enemiga actua        
        elif (vertical[0] == 2 or vertical[1] == 2 or vertical[2] == 2):
            for iColumna, columna in enumerate(vertical):
                if columna == 2:
                    if carton[0][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "0" + opcion
                        return opcion
                    
                    elif carton[1][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "1" + opcion
                        return opcion
                    
                    elif carton[2][iColumna] == " ":
                        opcion = str(iColumna)
                        opcion = "2" + opcion
                        return opcion
        
        # Si ve posibilidades de diagonal izquierda enemiga actua
        elif diagonalIzquierda == 2:
            if carton[0][0] == " ":
                opcion = "00"
                return opcion
            
            elif carton[1][1] == " ":
                opcion = "11"
                return opcion
            
            elif carton[2][2] == " ":
                opcion = "22"
                return opcion

        # Si ve posibilidades de diagonal derecha enemiga actua
        elif diagonalDerecha == 2:
            if carton[0][2] == " ":
                opcion = "02"
                return opcion
            
            elif carton[1][1] == " ":
                opcion = "11"
                return opcion
            
            elif carton[2][0] == " ":
                opcion = "20"
                return opcion
        
        # Si no sabe que hacer actua de manera aleatoría
        else:
            for opcion in opcionAleatoria:
                for i, digito in enumerate(opcion):
                    if i == 0:
                        digitoUno = int(digito)
                    elif i == 1:
                        digitoDos = int(digito)
                
                if not (carton[digitoUno][digitoDos] == "o" or carton[digitoUno][digitoDos] == "x"):
                    return opcion

# Acá empieza el juego
while True:
    clear()

    filaUno = [" ", " ", " "]
    filaDos = [" ", " ", " "]
    filaTres = [" ", " ", " "]
    carton = [filaUno, filaDos, filaTres]

    # Menú
    while True:
        clear()

        TresEnRaya()
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print()
        print("¿Contra quien quieres jugar?")
        print("---------------------------------------------------------")
        print("1 -> 1 vs IA")
        print("2 -> 1 vs 1")
        print("---------------------------------------------------------")
        print("4 -> Salir del juego")
        print("---------------------------------------------------------")
        usuario = input("-> ")

        turnoJugador = "o"
        turnoGuardado = "x"

        if usuario == "1":
            while True:
                dificultad = 0

                clear()

                TresEnRaya()
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                print()
                print("¿Que dificultad? | Estas jugando como ->", turnoJugador)
                print("---------------------------------------------------------")
                print("1 -> Normal")
                print("2 -> Difícil")
                print("---------------------------------------------------------")
                print("c -> Cambiar turno")
                print("---------------------------------------------------------")
                usuario = input("-> ")

                if usuario == "1":
                    dificultad = 1
                    break

                elif usuario == "2":
                    dificultad = 2
                    break

                elif usuario == "c":
                    turnoTemporal = turnoJugador
                    turnoJugador = turnoGuardado
                    turnoGuardado = turnoTemporal
                
                else:
                    clear()
                    print("Ese carácter no es valido")
                    time.sleep(2)

                if dificultad > 0:
                    break
            
            modoJuego = 1
            break

        elif usuario == "2":
            modoJuego = 2
            break
        
        elif usuario == "4":
            clear()
            
            print("¿Ya te vas? Adios :(")

            time.sleep(2)

            sys.exit(0)

        else:
            clear()
            print("Ese carácter no es valido")
            time.sleep(2)
    
    # Empieza la partida
    contador = 0
    while True:
        clear()

        turno = ""

        calcularTurno = contador % 2

        if calcularTurno == 0:
            turno = "o"

        elif calcularTurno == 1:
            turno = "x"

        # Input
        while True:
            clear()

            # Se pinta la interfaz de juego dependiendo del modo
            if modoJuego == 1:
                print("Modo de juego -> 1 vs IA")

            elif modoJuego == 2:
                print("Modo de juego -> 1 vs 1")

            print("Turno de", turno)
            print("■■■■■■■■■■■■■■■■■■■■")
            pintarCarton(carton)

            # Si el modo de juego es "1 vs IA" y dependiendo del turno se va turnando el jugardor con la IA
            if modoJuego == 1:
                if turnoJugador == "o":
                    if turno == "o":
                        usuario = input("Selecciona casilla -> ")
                    
                    elif turno == "x":
                        usuario = dificultadIA(dificultad, turno, turnoJugador, carton)

                elif turnoJugador == "x":
                    if turno == "x":
                        usuario = input("Selecciona casilla -> ")

                    elif turno == "o":
                        usuario = dificultadIA(dificultad, turno, turnoJugador, carton)

            # Si el modo de juego es "1 vs 1" los jugadores se van turnando
            elif modoJuego == 2:
                usuario = input("Selecciona casilla -> ")

            # Se comprueba que se puede marcar la casilla que se quiere marcar
            if usuario in ["00", "01", "02", "10", "11", "12", "20", "21", "22"]:
                for i, digito in enumerate(usuario):
                    if i == 0:
                        digitoUno = int(digito)

                    elif i == 1:
                        digitoDos = int(digito)
            
                if not (carton[digitoUno][digitoDos] == "o" or carton[digitoUno][digitoDos] == "x"):
                    break

                else:
                    clear()
                    print("Esa casilla ya esta tachada")
                    time.sleep(2)

            else:
                clear()
                print("El carácter", usuario, "no es valido")
                time.sleep(2)
        
        marcarCasilla(usuario, turno)

        comprobarGanador(carton, turno)

        if contador == 8:
            time.sleep(1)
            clear()
            print(" ______ __  __ _____     _______ ______ ")
            print("|  ____|  \/  |  __ \ /\|__   __|  ____|")
            print("| |__  | \  / | |__) /  \  | |  | |__   ")
            print("|  __| | |\/| |  ___/ /\ \ | |  |  __|  ")
            print("| |____| |  | | |  / ____ \| |  | |____ ")
            print("|______|_|  |_|_| /_/    \_\_|  |______|")
            print()
            salir = input("Pulsa cualquier tecla para terminar :)")

            break

        if comprobarGanador(carton, turno) == 1:
            break

        contador += 1

    time.sleep(4)
