"""
Para este ejercicio, creará un solucionador de Nonogramas. :)

Si no sabe qué son los nonogramas, puede consultar algunas instrucciones y también probar algunos nonogramas aquí.

Para resolver un Nonograma, primero debemos entender cómo funcionan. Un Nonograma es un rompecabezas que consta de una matriz de celdas en blanco y negro. Las pistas se proporcionan en los bordes de la matriz en forma de números que indican cuántas celdas negras hay en cada fila o columna consecutiva.

Por ejemplo, si las pistas para una fila son [2, 1], significa que hay dos grupos de celdas negras consecutivas en esa fila, el primero con dos celdas y el segundo con una sola celda. La solución para esta fila sería "BB_X_B" (donde "B" representa una celda negra y "X" representa una celda en blanco).

Para resolver un Nonograma completo, debemos usar las pistas y nuestro conocimiento de cómo funcionan los Nonogramas para ir rellenando la matriz poco a poco hasta obtener la solución final.

solo tendrás que resolver Nonogramas 5x5. 
Necesitas completar la clase Nonogram y el método solve:

class Nonogram:
    def __init__(self, clues):

        pass
    def solve(self):

        pass

Se te darán las pistas y deberás devolver el rompecabezas resuelto. Todos los acertijos se podrán resolver, por lo que no tendrás que preocuparte por eso. Habrá exactamente una solución para cada rompecabezas.

Las pistas serán una tupla de las pistas de columna, luego las pistas de fila, que contendrán las pistas individuales. Por ejemplo, para el Nonograma:
Las pistas están en la parte superior e izquierda del rompecabezas, así que en este caso:

Las pistas de columna son: ((1, 1), (4,), (1, 1, 1), (3,), (1,)), y las pistas de fila son: ((1,), (2,), (3,), (2, 1), (4,)). Las pistas de la columna se dan de izquierda a derecha. Si hay más de una pista para la misma columna, la pista superior se da primero. Las pistas de fila se dan de arriba a abajo. Si hay más de una pista para la misma fila, la pista más a la izquierda se da primero.
Por lo tanto, la pista dada al __init__método sería (((1, 1), (4,), (1, 1, 1), (3,), (1,)), ((1,), (2,), (3,), (2, 1), (4,))). Se le dan las pistas de la columna primero y luego las pistas de la fila en segundo lugar.
En la tupla, debe usar 0 para un cuadrado vacío y 1 para un cuadrado lleno. Por lo tanto, en este caso, debe devolver:

((0, 0, 1, 0, 0),

 (1, 1, 0, 0, 0),

 (0, 1, 1, 1, 0),

 (1, 1, 0, 1, 0),

 (0, 1, 1, 1, 1))
"""

from ast import main
import numpy as pd

class Nonogram:
    def __init__(self, pista):
        self.clues = pista 
        self.clues_colum = pista[0]
        self.clues_fila = pista[1]
        self.size = len(self.clues_colum)
        self.tablero = pd.zeros((self.size,self.size), dtype=int)
        self.tablero[0][0] = 1
        self.tablero[0][1] = 1
        self.tablero[0][2] = 1
        self.tablero[0][3] = 1
        self.tablero[0][4] = 1
        self.tablero[1][0] = 1
        self.tablero[1][1] = 1
        self.tablero[1][2] = 1
        self.tablero[1][3] = 1
        self.tablero[1][4] = 1
        self.tablero[2][0] = 1
        self.tablero[2][1] = 1
        self.tablero[2][2] = 1
        self.tablero[2][3] = 1
        self.tablero[2][4] = 1
        self.tablero[3][0] = 1
        self.tablero[3][1] = 1
        self.tablero[3][2] = 1
        self.tablero[3][3] = 1
        self.tablero[3][4] = 1
        self.tablero[4][0] = 1
        self.tablero[4][1] = 1
        self.tablero[4][2] = 1
        self.tablero[4][3] = 1
        self.tablero[4][4] = 1
        print(self.tablero)
        pass
    def solve(self):
        pass

def solve_nonogram(pista):
    nonogram = Nonogram(pista)
    nonogram.solve()
    return nonogram.tablero

if __name__ == '__main__':
    main()
