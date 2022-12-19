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
    if numero < 0 or numero > 999:
        return "Error, el numero debe estar entre 0 y 999"
    numero = str(numero)
    for i in range(len(numero)):
        if numero[i] == "0":
            numero = numero.replace("0", "zero")
        if numero[i] == "1":
            numero = numero.replace("1", "one")
        if numero[i] == "2":
            numero = numero.replace("2", "two")
        if numero[i] == "3":
            numero = numero.replace("3", "three")
        if numero[i] == "4":
            numero = numero.replace("4", "four")
        if numero[i] == "5":
            numero = numero.replace("5", "five")
        if numero[i] == "6":
            numero = numero.replace("6", "six")
        if numero[i] == "7":
            numero = numero.replace("7", "seven")
        if numero[i] == "8":
            numero = numero.replace("8", "eight")
        if numero[i] == "9":
            numero = numero.replace("9", "nine")
    numero = numero.split()
    return numero



if __name__ == "__main__":
    main()


