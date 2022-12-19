"""
La función de secuencia de Tribonacci se basa en la secuencia de Fibonacci, pero en lugar de sumar los dos últimos números de la secuencia, suma los tres últimos. Como su nombre ya puede revelar, funciona básicamente como un Fibonacci, pero sumando los últimos 3 (en lugar de 2) números de la secuencia para generar el siguiente. Y, lo que es peor, lamentablemente no podré escuchar a hablantes no nativos de italiano tratando de pronunciarlo :(

Esto produce una secuencia diferente, que comienza con una firma dada de tres números. Si la firma es [1, 1, 1], entonces la secuencia comienza así: [1, 1, 1, 3, 5, 9, 17, 31, ...]. Si la firma es [0, 0, 1], entonces la secuencia comienza así: [0, 0, 1, 1, 2, 4, 7, 13, 24, ...].

Entonces, si vamos a comenzar nuestra secuencia Tribonacci con [1, 1, 1]una entrada inicial (también conocida como firma ), tenemos esta secuencia:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]

Pero ¿y si empezáramos con [0, 0, 1]como firma? Como comenzar con [0, 1]en lugar de cambiar [1, 1]básicamente la secuencia común de Fibonacci en un lugar puede sentirse tentado a pensar que obtendríamos la misma secuencia desplazada en 2 lugares, pero ese no es el caso y obtendríamos:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Bueno, es posible que ya lo haya adivinado, pero para que quede claro: debe crear una función de Fibonacci que, dada una matriz/lista de firmas, devuelva los primeros n elementos, incluida la firma de la secuencia así sembrada.

La firma siempre contendrá 3 números; n siempre será un número no negativo; if n == 0, luego devuelve una matriz vacía (excepto en C devuelve NULL) y prepárate para cualquier otra cosa que no esté claramente especificada;)

Entendiendo que la firma siempre contiene 3 números, y que la secuencia de Tribonacci se genera sumando los últimos 3 números de la secuencia…

Bueno, es hora de expandir un poco más la familia: piense en un Quadribonacci que comienza con una firma de 4 elementos y cada elemento siguiente es la suma de los 4 anteriores, un Pentabonacci (bueno , Cinquebonacci probablemente sonaría un poco más italiano, pero sería también suena realmente horrible) con una firma de 5 elementos y cada elemento siguiente es la suma de los 5 anteriores, y así sucesivamente.
¿Bien adivina que? Debe crear una función Xbonacci que tome una firma de X elementos, y recuerde que cada elemento siguiente es la suma de los últimos X elementos, y devuelva los primeros n elementos de la secuencia así sembrada.

xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}

xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}

xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}

xbonacci {1,1} produces the Fibonacci sequence

Para implementar una función que calcule la secuencia de Xbonacci dado un número X y una firma de X elementos, primero deberíamos crear una función que tome una lista (la firma) y un número entero n y devuelva los primeros n elementos de la secuencia Xbonacci así sembrada. Esto se puede hacer usando un bucle que itere sobre los elementos de la secuencia y calcule el elemento siguiente como la suma de los últimos X elementos.
"""

from ast import main

def xbonacci(firma, n):
    final = []
    for i in range(n):
        if i < len(firma): # Si el indice es menor que la longitud de la firma
            final.append(firma[i]) # Agregamos el elemento de la firma
        else:
            final.append(sum(final[-len(firma):])) # Sumamos los ultimos elementos de la firma
    return final

if __name__ == "__main__":
    main()

    