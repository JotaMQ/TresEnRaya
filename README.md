TresEnRaya
========================================================================================================================================================================================
TresEnRaya es un juego que he programado en Python basado en el tradicional Tres en Raya con el objetivo de aprender las bases de Python.

📋 Normas de TresEnRaya
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- El cartón de juego es de 3 X 3 casillas.
- Gana el primer jugador que haga una linea de tres casillas.
- Se puede ganar con una linea vertical, horizontal y diagonal.

🎮 ¿Cómo jugar?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1- Seleccionar modo de juego: jugador contra jugador o jugador contra IA

2- Si se ha seleccionado jugador contra IA se debe seleccionar la dificultad.

3- Empieza la partida, durante tu turno deberás seleccionar que casilla quieres marcar indicandolo poniendo primero el eje y y luego el x. Ejemplo: si yo quiero marcar la casilla de
   la columna izquierda en la fila central tendre que poner "10".

4- La partida continuará hasta que uno de los dos jugadores haga una linea o queden en empate.

⚙️ Datos sobre el funcionamiento
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
El programa funciona de la siguiente manera:

1- Se selecciona el modo de juego.

2- En caso de seleccionar "1 vs IA" se selecciona la dificultad.

3- Empieza el bucle de la partida, y este no acabrá hasta que uno de los jugadores gane o pierda.

4- Durnate cada vuelta del bucle se calcula el turno, y cada jugador deberá marcar una casilla para finalizar el turno. En caso de "1 vs IA" se marcará una casilla u otra dependiendo
   de la dificultad seleccionada.

6- Una vez seleccionada la casilla a marcar, esta se marcará.

7- Antes de pasar al siguiente turno se ejecutará una función que comprobará si hay ganador, en caso de que haya ganador se anunciará el mismo y acabara la partida.

8- En caso de que no haya ganador el bucle continuará hasta que un contador cuente 8 vueltas, en ese caso se anunciará el empate y el juego acabará.

✅ Versiones
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Última versión: 1.1
- Se ha arreglado un error por el cual cuando la IA en difícil detectaba que tenia dos casillas marcadas en una linea diagonal intentaba marcar la que quedaba para hacer raya aún que
  el jugador ya la habia marcado, lo que provocaba que el juego fallara.

- Se ha añadido una opción para salir del juego en el menú principal.

Versión 1.0
- Versión de salida.