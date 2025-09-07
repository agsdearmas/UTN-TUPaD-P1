# TP 3: Estructuras Repetitivas
# Alumno: De Armas Agustin
# Comision: 7

import random


'''
Ejercicio1

Se define un umbral con limite 100.
Luego se recorre el mismo en orden creciente, y se imprime cada numero
por pantalla.
'''
umbral = 100

for i in range(umbral+1):
    print(i)


'''
Ejercicio 2

Se solicita al usuario que ingrese un numero entero, y luego se determina
la cantidad de digitos que contiene el mismo.
'''
num_inicial = int(input('Por favor, ingrese un numero entero: '))
num_mod = abs(num_inicial)
digitos = 0

while num_mod > 0:
    num_mod //= 10
    digitos += 1
print(f'El numero {num_inicial} contiene: {digitos} digitos.')


'''
Ejercicio 3

Se solicita al usuario que ingrese dos numeros enteros.
Luego sumamos los numeros enteros comprendidos dentro de este rango,
excluyendo los limites.
'''
num1 = int(input('Por favor, ingrese el primer numero: '))
num2 = int(input('Por favor, ingrese el segundo numero: '))

# Validamos que hayan numeros enteros dentro del rango comprendido
if num1 == num2 or abs(num1 - num2) <= 1:
    print('No se encontraron numeros enteros dentro del rango')
else:
    if num1 < num2:
        num_inicial = num1
        num_final = num2
    else:
        num_inicial = num2
        num_final = num1

    suma = 0

    # Se suman los numeros enteros dentro del rango
    for num in range(num_inicial+1, num_final):
        suma += num
    
    print(f'La suma de los numeros enteros entre {num1} y {num2} es: {suma}')


'''
Ejercicio 4

Se solicita al usuario que ingrese numeros enteros
y los sumamos de manera secuencial.
El programa se detiene y mostramos el total acumulado cuando el usuario ingresa 0
'''
acumulado = 0
CONTROLADOR = True

# Utilizamos la variable controlador para mantener el bucle
# Salimos unicamente si el numero ingresado es igual a 0
while CONTROLADOR:
    num = int(input('Por favor, ingrese un numero entero: '))
    if num == 0:
        break
    acumulado += num

print(f'El total acumulado es: {acumulado}')


'''
Ejercicio 5

Se solicita al usuario que adivine un numero aleatorio entre 0 y 9.
Se imprime por pantalla la cantidad de intentos que fueron necesarios para acertar
'''
num_rand = random.randint(0, 9)
controlador = True
contador = 0

# Utilizamos la variable contador para mantener el bucle
# Salimos unicamente si el usuario acierta el numero correcto
while controlador:
    contador += 1
    num = int(input('Adivine el numero ganador entre 0 y 9: '))

    if num == num_rand:
        print(f'El numero ganador es {num_rand}! la cantidad de intentos fue: {contador}')
        break
    print('El numero es incorrecto, por favor intente nuevamente')


'''
Ejercicio 6

Recorremos un rango de 100 numeros en orden decreciente,
e imprimimos por pantalla todos los numeros pares comprendidos
'''
for i in range(100, -1, -2):
    print(i)


'''
Ejercicio 7

Se solicita al usuario que ingrese un numero entero positivo.
Luego calculamos la suma de todos los numeros comprendidos entre 0
y el numero ingresado por el usuario.
'''
suma = 0
num1 = 0
num2 = int(input('Por favor, ingrese un numero entero positivo: '))

# Validamos que el numero ingresado sea positivo o que existan numeros enteros dentro del rango
if num2 < 0:
    print('El numero ingresado es incorrecto')
elif num1 == num2 or abs(num1 - num2) <= 1:
    print('No se encontraron numeros enteros dentro del rango')
else:
    for num in range(num1, num2):
        suma += num

    print(f'La suma de todos los numeros comprendidos entre 0 y {num2} es: {suma}')


'''
Ejercicio 8

Se solicita al usuario que ingrese un total de n numeros enteros.
Almacenamos positivos, negativos, pares e impares.
Y luego mostramos la cantidad por pantalla.
'''
RANGO_NUMEROS = 100
positivos = 0
negativos = 0
pares = 0
impares = 0

print(f'Por favor, ingrese un total de {RANGO_NUMEROS} numeros enteros')

for i in range(RANGO_NUMEROS):
    num = int(input(f'Por favor, ingrese el numero {i+1}: '))

    # Validamos positivos y negativos
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    # Validamos pares e impares
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1

print(f'Numeros positivos: {positivos}')
print(f'Numeros negativos: {negativos}')
print(f'Numeros pares: {pares}')
print(f'Numeros impares: {impares}')


'''
Ejercicio 9

Se solicita al usuario que ingrese n numeros enteros.
Luego calculamos la media de los valores ingresados, y los imprimimos en pantalla.
'''
RANGO_NUMEROS = 100
suma_total = 0

print(f'Por favor, ingrese un total de {RANGO_NUMEROS} numeros enteros')

for i in range(RANGO_NUMEROS):
    num = int(input(f'Por favor, ingrese el numero {i+1}: '))
    suma_total += num

# Se calcula la media si existe un rango de numeros valido
if RANGO_NUMEROS > 0:
    media = suma_total / RANGO_NUMEROS
    print(f'La media de los {RANGO_NUMEROS} ingresados es: {media}')
else:
    print('No existe un rango valido')


'''
Ejercicio 10

Se solicita al usuario que ingrese un numero.
Luego invertimos el numero ingresado y lo mostramos por pantalla.
'''
num_invertido = 0
num_ingresado = int(input('Por favor, ingrese un numero: '))

while num_ingresado > 0:
    # Obtenemos el ultimo digito del numero ingresado
    digito = num_ingresado % 10

    # Construimos el numero invertido en una variable auxiliar, desplazando los digitos
    num_invertido = (num_invertido * 10) + digito

    # Eliminamos el ultimo digito del numero ingresado
    num_ingresado = num_ingresado // 10

print(f'El numero intertido es: {num_invertido}')
