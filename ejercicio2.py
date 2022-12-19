"""
Cuando asistíamos a la escuela secundaria, se nos pidió que simplificáramos expresiones matemáticas como "3x-yx+2xy-x" (o generalmente más grande), y eso fue muy fácil ("2x+xy"). ¡Pero díselo a tu pc y ya veremos!

Existen varias formas de simplificar una expresión matemática, pero una posible solución a su problema sería utilizar la regla de la suma y del producto de los exponentes para combinar términos similares en la expresión.

Por ejemplo, la expresión "3x-zx+2xy-x" se podría simplificar de la siguiente manera:

Identificar los términos que tienen la misma base (por ejemplo, "x") y agruparlos juntos: "3x - x + 2xy - zx"
Aplicar la regla de la suma y del producto de los exponentes para cada grupo de términos:
Para el grupo "3x - x", el exponente de la base "x" es 1 en ambos términos, por lo que se pueden combinar utilizando la regla de la suma de exponentes: 3x - x = 2x
Para el grupo "2xy - zx", el exponente de la base "x" es 1 en ambos términos, por lo que se pueden combinar utilizando la regla de la suma de exponentes: 2xy - zx = (2-z)xy
Reemplazar cada grupo de términos simplificados en la expresión original: "3x - x + 2xy - zx" se convierte en "2x + (2-z)xy"
 

Escriba una función simplify, que tome una cadena en la entrada, que represente un polinomio multilineal no constante en coeficientes enteros (como "3x-zx+2xy-x"), y devuelva otra cadena como salida donde la misma expresión se ha simplificado de la siguiente manera ( ->significa aplicación de simplify):

Se han realizado todas las sumas y restas posibles de monomios equivalentes ("xy==yx"), por ejemplo: "cb+cba" -> "bc+abc", "2xy-yx" -> "xy","-a+5ab+3a-c-2a" -> "-c+5ab"

Todos los monomios aparecen en orden creciente de número de variables, por ejemplo: "-abc+3a+2ac" -> "3a+2ac-abc","xyz-xz" -> "-xz+xyz"
Si dos monomios tienen el mismo número de variables, aparecen en orden lexicográfico , por ejemplo: "a+ca-ab" -> "a-ab+ac","xzy+zby" ->"byz+xyz"

No hay +signo inicial si el primer coeficiente es positivo, por ejemplo: "-y+x" -> "x-y", pero sin restricciones para -: "y-x" ->"-x+y"
Advertencia: 

para mantenerlo más simple, la cadena en la entrada está restringida para representar solo polinomios multilineales no constantes, por lo que no encontrará algo como `-3 + yx ^ 2'. Multilineal significa en este contexto: de grado 1 sobre cada variable.
la cadena de entrada puede contener variables arbitrarias representadas por caracteres en minúsculas en el alfabeto inglés.
"""