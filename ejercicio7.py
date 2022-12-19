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
    # Convertimos las posiciones a coordenadas
    pos1 = algebraic_to_numeric(pos1)
    pos2 = algebraic_to_numeric(pos2)

    # Creamos el tablero de ajedrez
    tablero = np.zeros((8, 8))

    # Marcamos la posición inicial y final
    tablero[pos1] = 0
    tablero[pos2] = 1

    # Inicializamos la cola de búsqueda
    queue = [pos1]

    # Inicializamos el contador de movimientos
    movimientos = 0

    # Mientras haya posiciones en la cola de búsqueda
    while queue:
        # Obtenemos la posición actual
        current_pos = queue.pop(0)

        # Si la posición actual es la posición final, terminamos
        if tablero[current_pos] == 1:
            break

        # Obtenemos las posiciones a las que el caballo puede moverse
        possible_moves = get_possible_moves(current_pos)

        # Agregamos las posiciones válidas a la cola de búsqueda
        for move in possible_moves:
            if is_valid_move(move, tablero):
                queue.append(move)

        # Incrementamos el contador de movimientos
        movimientos += 1

    return movimientos

def algebraic_to_numeric(pos):
    # Obtenemos la fila y columna
    row = int(pos[1]) - 1
    col = ord(pos[0]) - ord('a')

    return (row, col)

def get_possible_moves(pos):
    # Obtenemos la fila y columna de la posición actual
    row, col = pos

    # Calculamos las posiciones a las que puede moverse el caballo
    movimientos = [
        (row + 2, col + 1),
        (row + 2, col - 1),
        (row - 2, col + 1),
        (row - 2, col - 1),
        (row + 1, col + 2),
        (row + 1, col - 2),
        (row - 1, col + 2),
        (row - 1, col - 2)
    ]

    return movimientos

def is_valid_move(pos, tablero):
    # Obtenemos la fila y columna de la posición actual
    row, col = pos

    # Verificamos que la posición esté dentro del tablero
    if row < 0 or row >= 8:
        return False
    if col < 0 or col >= 8:
        return False

    # Verificamos que la posición no haya sido visitada
    if tablero[pos] != 0:
        return False

    return True

if __name__ == '__main__':
    main()
    