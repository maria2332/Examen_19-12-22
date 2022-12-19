"""
¡A nadie le gustan los lunes! Pasaste el fin de semana de fiesta y con amigos, y luego llega el lunes y tienes que levantarte temprano, ponerte ropa de negocios e ir a trabajar. Entonces, ¿cuántos de estos horribles días tiene que soportar alguien? Bueno, averigüémoslo.

Cree un método para encontrar el número de lunes dado el cumpleaños de una persona y la fecha actual. Para este ejercicio simple, no te preocupes por los días festivos/vacaciones, licencia por enfermedad, etc. Supongamos que una persona tiene un trabajo y va a trabajar durante todo el año si está en edad de trabajar. Para simplificar las cosas, suponga que alguien comienza a trabajar cuando tiene 22 años y se jubila cuando tiene 78.

¡Así es, los lunes no cuentan cómo días malos si estás en la escuela/universidad o eres jubilado!

En las pruebas, la fecha actual será la misma o posterior al cumpleaños de una persona y ambas fechas serán no nulas y válidas. Y aunque no tener que trabajar los fines de semana es una moda bastante reciente (¡búscalo!), asume que los lunes siempre serán y serán días malos en cualquier época.

Para resolver este problema, se puede seguir los siguientes pasos:

Calcular la edad de la persona en la fecha actual. Para ello, se puede calcular la diferencia en años entre la fecha actual y la fecha de cumpleaños de la persona.
Verificar si la persona está en edad de trabajar. Para ello, se puede comprobar si su edad está entre 22 y 78 años.
Calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual. Para ello, se puede calcular el número de días que hay entre ambas fechas y dividirlo por 7, ya que una semana tiene 7 días.
Si la persona está en edad de trabajar, devolver el número de lunes calculado en el paso 3. En caso contrario, devolver 0.
"""

from ast import main
import numpy as np

def contar_lunes(cumple, fecha_actual):
    edad = fecha_actual.año - cumple.año # Calcular la edad de la persona en la fecha actual
    if edad >= 22 and edad <= 78: # Verificar si la persona está en edad de trabajar
        return (fecha_actual - cumple).dias // 7 # Calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual
    else:
        return 0

if __name__ == "__main__":
    main()
