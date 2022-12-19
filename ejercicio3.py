"""
Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de letras en "sixzero" es siete. El número de letras en "siete" es cinco. El número de letras en "cinco" es cuatro. El número de letras en "cuatro" es cuatro: hemos alcanzado un equilibrio estable.

Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que tiene siete letras. El número de letras en "siete" es cinco, y el número de letras en "cinco" es cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y contando el número de letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número de letras es igual a cuatro.

Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola palabra (en lugar del nombre propio del número en inglés). Por ejemplo, escribe 12 como "unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa y nueve).

Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde ese número entero hasta un equilibrio estable:

Ejemplos

numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
numbersOfLetters(1) --> ["one", "three", "five", "four"]
"""

from ast import main
import numpy as pd

def numeroLetras(numero):
    if numero == 0:
        return "zero"
    if numero == 1:
        return "one"
    if numero == 2:
        return "two"
    if numero == 3:
        return "three"
    if numero == 4:
        return "four"
    if numero == 5:
        return "five"
    if numero == 6:
        return "six"
    if numero == 7:
        return "seven"
    if numero == 8:
        return "eight"
    if numero == 9:
        return "nine"

def numbersOfLetters(numero):
    numero = []
    numero.escrito=numero.append(numeroLetras(numero))
    numero.
    if len(numero.escrito) ==
    




if __name__ == "__main__":
    main()


