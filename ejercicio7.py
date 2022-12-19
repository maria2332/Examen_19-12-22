"""
Dadas dos posiciones diferentes en un tablero de ajedrez, encuentre el menor número de movimientos que le tomaría a un caballo pasar de una a la otra. Las posiciones se pasarán como dos argumentos en notación algebraica. 

Por ejemplo, knight("a3", "b5")debería devolver 1.

El caballo no puede moverse fuera del tablero. El tablero es de 8x8.

Para resolver este problema, podemos seguir los siguientes pasos:

Convertimos las posiciones de notación algebraica a coordenadas (fila, columna) en un tablero de 8x8. Por ejemplo, la posición "a3" se convertiría a (3, 1) donde 3 es la fila y 1 es la columna.
Creamos una matriz de 8x8 que represente el tablero de ajedrez, y marcamos las posiciones inicial y final con un valor especial (por ejemplo, 0 y 1).
Utilizamos un algoritmo de búsqueda como BFS (Breadth-First Search) para encontrar el camino más corto entre la posición inicial y final. La búsqueda se realiza desde la posición inicial y se expande en todas las posibles posiciones a las que el caballo puede moverse. Cada vez que se encuentra una posición válida (es decir, que está dentro del tablero y no ha sido visitada antes), se agrega a la cola de búsqueda, para nuestro caso una lista. La búsqueda termina cuando se encuentra la posición final o se agota la cola de búsqueda(lista) sin encontrarla.
El número de movimientos requeridos se calcula como la longitud del camino encontrado menos 1 (ya que la posición inicial se cuenta como un movimiento).
"""

from ast import main
import numpy as np

def caballo(pos1, pos2):
    pos1 = algebraic_to_numeric(pos1)
    pos2 = algebraic_to_numeric(pos2)

    tablero = np.zeros((8, 8))

    tablero[pos1] = 0 # Posición inicial
    tablero[pos2] = 1 # Posición final

    queue = [pos1]

    movimientos = 0 # Contador de movimientos

    while queue:
        current_pos = queue.pop(0) # Obtenemos la posición actual

        if tablero[current_pos] == 1:
            break

        mov_posibles = obtener_movimientos_posibles(current_pos)

        for move in mov_posibles:
            if mov_valido(move, tablero):
                queue.append(move)

        movimientos += 1 # Incrementamos el contador de movimientos

    return movimientos

def algebraic_to_numeric(pos):
    # Obtenemos la fila y columna
    row = int(pos[1]) - 1
    col = ord(pos[0]) - ord('a')

    return (row, col)

def obtener_movimientos_posibles(pos):
    fila, col = pos

    # Calculamos las posiciones a las que puede moverse el caballo
    movimientos = [
        (fila + 2, col + 1),
        (fila + 2, col - 1),
        (fila - 2, col + 1),
        (fila - 2, col - 1),
        (fila + 1, col + 2),
        (fila + 1, col - 2),
        (fila - 1, col + 2),
        (fila - 1, col - 2)
    ]

    return movimientos

def mov_valido(pos, tablero):
    fila, col = pos

    # Verificamos que la posición esté dentro del tablero
    if fila < 0 or fila >= 8:
        return False
    if col < 0 or col >= 8:
        return False

    # Verificamos que la posición no haya sido visitada
    if tablero[pos] != 0:
        return False

    return True

if __name__ == '__main__':
    main()
    