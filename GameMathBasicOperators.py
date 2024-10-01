import random

# Variables to track correct answers and lives
correctas = 0
vidas = 3
homero = 0

# START: Introduction and level explanation
print('Bienvenido al juego de operadores matemáticos básicos \n')
print('En este primer nivel se te pedirá SUMAR dos números, recuerda contestar rápido')

# Nivel 1: Sumar dos números aleatorios
for i in range(5):
    num1 = random.randint(10, 120)
    print(num1)
    num2 = random.randint(10, 120)
    print(num2)
    suma = num1 + num2
    respuesta_suma = int(input('Introduce la suma de los dos números:'))

    # Check if the answer is correct
    if respuesta_suma == suma:
        correctas += 1
    else:
        print('¡Lástima, la próxima lo lograrás!')
        print('La respuesta era:', suma)
        vidas -= 1

print('Te quedan', vidas, 'vidas')
print('Llevas', correctas, 'respuestas correctas')

# Check if the player still has lives
if vidas <= 0:
    print('Lamentablemente, se acabaron tus vidas, ¡intenta de nuevo, sabemos que lo lograrás!')
    homero += 1
else:
    print('¡BIEN HECHO! HAS TERMINADO EL NIVEL DE SUMAS')
    print('En este segundo nivel se te pedirá RESTAR dos números, recuerda contestar rápido')

    # Nivel 2: Restar dos números aleatorios
    for i in range(5):
        num3 = random.randint(10, 120)
        num4 = random.randint(10, 120)

        # Ensure the subtraction result is positive
        if num3 < num4:
            res = num4 - num3
            print(num4)
            print(num3)
        else:
            res = num3 - num4
            print(num3)
            print(num4)

        respuesta_resta = int(input('Introduce la resta de los dos números:'))

        # Check if the answer is correct
        if respuesta_resta == res:
            correctas += 1
        else:
            print('¡Lástima, la próxima lo lograrás!')
            print('La respuesta era:', res)
            vidas -= 1

# Check if the player still has lives after subtraction level
if vidas <= 0 and homero == 0:
    print('Lamentablemente, se acabaron tus vidas, ¡intenta de nuevo, sabemos que lo lograrás!')
    homero += 1
else:
    print('Te quedan', vidas, 'vidas')
    print('Llevas', correctas, 'respuestas correctas')
    print('¡BIEN HECHO! HAS TERMINADO EL NIVEL DE RESTAS')
    print('En este tercer nivel se te pedirá MULTIPLICAR dos números, recuerda contestar rápido')

    # Nivel 3: Multiplicar dos números aleatorios
    for i in range(5):
        num5 = random.randint(2, 13)
        print(num5)
        num6 = random.randint(2, 13)
        print(num6)
        multi = num5 * num6
        respuesta_multi = int(input('Introduce la multiplicación de los dos números:'))

        # Check if the answer is correct
        if respuesta_multi == multi:
            correctas += 1
        else:
            print('¡Lástima, la próxima lo lograrás!')
            print('La respuesta era:', multi)
            vidas -= 1

# Check if the player still has lives after multiplication level
if vidas <= 0 and homero == 0:
    print('Lamentablemente, se acabaron tus vidas, ¡intenta de nuevo, sabemos que lo lograrás!')
    homero += 1
else:
    print('Te quedan', vidas, 'vidas')
    print('Llevas', correctas, 'respuestas correctas')
    print('¡BIEN HECHO! HAS TERMINADO EL NIVEL DE MULTIPLICACIONES')
    print('En este cuarto nivel se te pedirá DIVIDIR dos números, recuerda contestar rápido')

    # Nivel 4: Dividir dos números de una lista predefinida
    safe = [24, 3, 27, 18, 8, 12, 20, 30, 10, 26]
    for j in range(5):
        aleatorio = random.choice(safe)
        aleatorio2 = random.randint(2, 20)

        # Ensure the division is exact
        while aleatorio % aleatorio2 != 0:
            aleatorio2 = random.randint(2, 20)

        print('Realiza la división de:', aleatorio, 'entre', aleatorio2)
        boing = aleatorio / aleatorio2
        respuesta_div = float(input())

        # Check if the answer is correct
        if respuesta_div == boing:
            correctas += 1
        else:
            print('¡Lástima, la próxima lo lograrás! La respuesta era:', boing)
            vidas -= 1

# Final messages based on performance
if vidas <= 0 and homero == 0:
    print('Lamentablemente, se acabaron tus vidas, ¡intenta de nuevo, sabemos que lo lograrás!')
    homero += 1
else:
    print('¡BIEN HECHO! HAS TERMINADO TODOS LOS NIVELES')

if correctas == 20:
    print('¡Excelente! Completaste el juego sin errores, ¡intenta mejorar tu velocidad!')
elif correctas >= 15 and correctas < 20:
    print('Te quedaste con', vidas, 'vidas y tuviste', correctas, 'respuestas correctas, ¡felicitaciones!')
    print('Intenta nuevamente completar el juego sin equivocarte, ¡sabemos que lo lograrás!')
