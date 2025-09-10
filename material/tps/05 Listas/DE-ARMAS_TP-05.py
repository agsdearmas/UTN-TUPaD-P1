# TP 5: Listas
# Alumno: De Armas Agustin
# Comision: 7

import random


'''
Ejercicio 1

Se define una lista con la nota de 10 estudiantes y se imprime en pantalla.
Luego se calcula el promedio y se imprime en pantalla.
Para finalizar, indicamos la nota mas alta y mas baja.
'''
lista_notas = [9.0, 7.0, 6.5, 10.0, 9.5, 7.5, 6, 7.0, 8.0, 8.5]
suma_notas = 0

# Recorremos la lista para sumar todos sus elementos
# Luego calculamos el promedio y lo imprimimos en pantalla
print(f'Notas de 10 estudiantes: \n{lista_notas}')
for nota in lista_notas:
    suma_notas += nota

promedio = suma_notas / len(lista_notas)
print(f'El promedio del total de notas es: {promedio}')

# Realizamos la busqueda del valor mas alto y mas bajo de la lista
nota_mayor = lista_notas[0]
nota_menor = lista_notas[0]

if lista_notas:
    for nota in lista_notas:
        # Comprobamos si la nota es la mas alta
        if nota > nota_mayor:
            nota_mayor = nota
        # Comprobamos si la nota es la mas baja
        if nota < nota_menor:
            nota_menor = nota

print(f'La nota mas alta es: {nota_mayor}')
print(f'La nota mas baja es: {nota_menor}')


'''
Ejercicio 2

Se solicita al usuario que ingrese cinco productos en una lista.
Se imprime en pantalla la lista ordenada alfabeticamente.
Y luego se consulta al usuario que producto desea eliminar,
y se actualiza la lista.
'''
lista_productos = []

# Solicitamos 5 elementos para nuestra lista y los ordenamos
for producto in range(5):
    producto = input(f"Ingrese el nombre del producto {producto+1}: ")
    lista_productos.append(producto.lower())

lista_productos = sorted(lista_productos)
print(f'Lista ordenada de productos ingresados: \n{lista_productos}')

# Validamos que la lista contenga elementos
while len(lista_productos) > 0:
    eliminar_producto = input(f"Ingrese el nombre del producto que desea eliminar: ").lower()

    # Validamos si el producto existe en la lista
    if eliminar_producto in lista_productos:
        lista_productos.remove(eliminar_producto)
        print(f'El producto {eliminar_producto} se elimino correctamente de la lista')
        print(f'Su lista actual es: \n{lista_productos}')
    else:
        print(f'El producto {eliminar_producto} no se encuentra en la lista')


'''
Ejercicio 3

Se define una lista de quince numeros en un rango de 1 a 100.
Luego recorremos la lista y validamos los numeros pares e impares,
los asignamos a su respectiva lista, y se imprimen en pantalla.
'''
lista_numeros = [random.randint(1, 100) for i in range(15)]
numeros_pares = []
numeros_impares = []

# Validamos si el numero es par o impar, y lo asignamos a la lista correspondiente
for num in lista_numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

print(f'La lista de numeros pares contiene {len(numeros_pares)} numeros: \n{numeros_pares}')
print(f'La lista de numeros impares contiene {len(numeros_impares)} numeros: \n{numeros_impares}')


'''
Ejercicio 4

Se define una lista de numeros con valores duplicados.
Luego recorremos la lista parar armar una nueva sin elementos duplicados,
y se imprime en pantalla.
'''
lista_duplicados = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_duplicados = []

print(f'Lista inicial con duplicados: \n{lista_duplicados}')

# Iteramos cada numero en la lista inicial de duplicados
for num in lista_duplicados:
    # Si el elemento no existe en la nueva lista, lo agregamos
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

print(f'Lista final sin duplicados: \n{lista_sin_duplicados}')


'''
Ejercicio 5

Se define una lista de 8 estudiantes.
Luego se solicita al usuario que ingrese una de las 2 opciones,
en el caso de opcion 1 agregamos un nuevo estudiante a la lista,
en el caso de opcion 2 eliminamos un estudiante existente de la lista.
Para finalizar, se imprime por pantalla la lista actualizada.
'''
lista_estudiantes = ["Ana", "Carlos", "Hugo", "Nicolas", "Romina", "Gabriel", "Laura", "Pedro"]
CONTROLADOR = True

print(f'Lista de estudiantes actual: \n{lista_estudiantes}')

# Utilizamos un bucle while para validar que se ingresa una opcion valida
while CONTROLADOR:
    opcion = int(input('Por favor, ingrese una de las siguientes opciones: \n' \
    '(1) Agregar un estudiante\n(2) Eliminar un estudiante\n'))

    # Agregamos un nuevo estudiante a la lista
    if opcion == 1:
        nuevo_estudiante = input('Por favor, ingrese el nombre del nuevo estudiante: ').title()
        lista_estudiantes.append(nuevo_estudiante)
        break

    # Si es un usuario existente en la lista, lo eliminamos
    elif opcion == 2:
        eliminar_estudiante = input('Por favor, ingrese el nombre del estudiante que desea eliminar: ').title()
        if eliminar_estudiante in lista_estudiantes:
            lista_estudiantes.remove(eliminar_estudiante)
            print(f'El estudiante {eliminar_estudiante}, se elimino correctamente de la lista')
        else:
            print(f'El estudiante {eliminar_estudiante} no se encuentra en la lista')
        break

    else:
        print('La opcion ingresada no es valida, por favor intente nuevamente')

print(f'Lista de estudiantes final: \n{lista_estudiantes}')


'''
Ejercicio 6

Se define una lista de 7 numeros.
Luego rotamos todos los elementos una posicion a la derecha.
Para finalizar, se imprime la nueva lista en pantalla
'''
lista_numeros = [1, 2, 3, 4, 5, 6, 7]

print(f'Lista de numeros inicial: \n{lista_numeros}')

# Extraemos el ultimo elemento de la lista y lo asignamos a una nueva
# Luego asignamos el resto de la lista a una nueva modificada
ultimo_numero = lista_numeros[-1:]
lista_modificada = lista_numeros[:-1]

# Concatenamos las nuevas listas
lista_final = ultimo_numero + lista_modificada
print(f'La lista de numeros final es: \n{lista_final}')


'''
Ejercicio 7

Se define una lista de temperaturas semanal y una lista de dias de la semana.
Luego calculamos el promedio de las temperaturas minimas y maximas.
Para finalizar, mostramos en que dia se registro la mayor amplitud termica
'''
lista_temperatura = [
    [12, 24],
    [10, 21],
    [7, 16],
    [8, 18],
    [7, 18],
    [12, 22],
    [14, 24]
]
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
temp_minima = 0
temp_maxima = 0

# Recorremos la lista de temperatura y calculamos los promedios min y max
for i in range(len(lista_temperatura)):
    temp_minima += lista_temperatura[i][0]
    temp_maxima += lista_temperatura[i][1]

promedio_min = temp_minima / len(lista_temperatura)
promedio_max = temp_maxima / len(lista_temperatura)

print(f'El promedio de temperaturas minimas es: {promedio_min:.1f} ºC')
print(f'El promedio de temperaturas maximas es: {promedio_max:.1f} ºC')

dia_amplitud_mayor = ''
amplitud_mayor = 0

# Recorremos la lista de temperatura y calculamos el dia con mayor amplitud termica
for i in range(len(lista_temperatura)):
    temp_minima = lista_temperatura[i][0]
    temp_maxima = lista_temperatura[i][1]
    
    amplitud_aux = temp_maxima - temp_minima
    
    if amplitud_aux > amplitud_mayor:
        amplitud_mayor = amplitud_aux
        dia_amplitud_mayor = dias_semana[i]

print(f'El dia {dia_amplitud_mayor} se registro la mayor amplitud termica: {amplitud_mayor:.1f} ºC')


'''
Ejercicio 8

Se define una matriz de notas de 5 estudiantes en 3 materias.
Luego calculamos el promedio de cada uno y lo imprimimos en pantalla.
Para finalizar calculamos la suma de notas de cada materia en una nueva lista,
obtenemos el promedio final de cada materia, y lo imprimimos en pantalla.
'''
lista_notas = [
    [8.0, 9.0, 7.5],    # Ana
    [9.0, 6.0, 9.5],    # Nicolas
    [7.5, 8.0, 8.0],    # Hugo
    [6.5, 8.5, 7.0],    # Romina
    [9.0, 10.0, 9.5]    # Julio
]
lista_estudiantes = ['Ana', 'Nicolas', 'Hugo', 'Romina', 'Julio']
lista_materias = ['Programacion', 'Matematica', 'AySO']

print(f'El promedio de cada estudiante es:')

for i in range(len(lista_notas)):
    # Utilizamos sum para iterar y sumar el listado de notas, y luego calculamos el promedio
    suma_notas = sum(lista_notas[i])
    promedio_estudiante = suma_notas / len(lista_notas[i])
    print(f'{lista_estudiantes[i]}: {promedio_estudiante:.1f}')

# Creamos una lista para almacenar la suma de las notas de cada materia
suma_materias = [0, 0, 0]

# Iteramos cada fila estudiante, y cada columna materias para almacenar la suma de notas
for estudiante in lista_notas:
    for materia in range(len(estudiante)):
        suma_materias[materia] += estudiante[materia]

print(f'\nEl promedio de cada materia es:')

# Iteramos cada columna materia y calculamos el promedio de la suma de sus notas
for materia in range(len(lista_materias)):
    materia_promedio = suma_materias[materia] / len(lista_estudiantes)
    print(f'{lista_materias[materia]}: {materia_promedio:.1f}')


'''
Ejercicio 9

Definimos un tablero de Ta-Te-Ti como una matriz de 3x3.
Inicializamos el tablero con casilleros vacios ('-').
Definimos ambos jugadores como 'X' y 'O'.
Y luego permitimos que cada uno ingrese una posicion (fila y columna),
imprimiendo en pantalla el tablero actual al concluir cada turno.
Para finalizar imprimimos el tablero final con todas las jugadas.
'''
tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
opciones_validas = [0, 1, 2]
jugadores = ['X', 'O']
turno = 0
CONTROLADOR = True

# Inicializamos el juego con 9 movimientos posibles
for jugadas in range(9):
    jugador = jugadores[turno]
    print(f'\nEs el turno del jugador: {jugador}')
    
    # Imprimimos el tablero con los datos actuales
    for fila in tablero:
        for casillero in fila:
            print(casillero, end=' ')
        print('')

    # Utilizamos CONTROLADOR para mantener un flujo valido de opciones ingresadas
    while CONTROLADOR:
        fila = input('Ingrese el numero de fila [0, 1, 2]: ')
        columna = input('Ingrese el numero de columna [0, 1, 2]: ')

        # Verificamos que los inputs sean digitos validos para evitar errores de parseo
        if fila.isdigit() and columna.isdigit():
            fila = int(fila)
            columna = int(columna)

            # Verificamos que la opcion ingresada, sea una coordenada valida en nuestro tablero
            if fila in opciones_validas and columna in opciones_validas:
                if tablero[fila][columna] == '-':
                    tablero[fila][columna] = jugador
                    break
                else:
                    print('La posicion ya se encuentra en uso, por favor intente nuevamente')
            else:
                print('La opcion ingresada esta fuera del rango, por favor intente nuevamente')
        else:
            print('El valor ingresado no es un digito, por favor intente nuevamente')

    # Realizamos el cambio de jugador(turno)
    turno = 1 - turno

# Imprimimos el resultado final del juego
for fila in tablero:
    for casillero in fila:
        print(casillero, end=' ')
    print('')


'''
Ejercicio 10

Se define un registro de ventas de 4 productos durante 7 dias, en una matriz de 4x7.
En el modulo 1, recorremos las ventas diarias de cada producto, para mostrar la venta total por producto.
En el modulo 2, obtenemos el total de ventas por dia, y luego buscamos el indice del dia con mayor total de ventas.
En el modulo 3, buscamos el indice del producto con mas vendido de la semana.
'''
ventas = [
    [200, 100, 165, 150, 250, 180, 140],   # Producto 1
    [25, 15, 15, 18, 20, 21, 17],          # Producto 2
    [50, 65, 100, 60, 150, 120, 70],       # Producto 3
    [25, 30, 35, 60, 70, 100, 26]          # Producto 4
]
lista_dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
lista_productos = ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4']
ventas_por_dia = [0, 0, 0, 0, 0, 0, 0]
ventas_por_producto = [0, 0, 0, 0]

# Modulo 1: Total de ventas por producto
print(f'El total de ventas por productos es:')

for producto in range(len(ventas)):
    total_producto = 0
    # Iteramos sobre las ventas diarias de cada producto en especifico para obtener la venta total
    for venta_diaria in ventas[producto]:
        total_producto += venta_diaria
    ventas_por_producto[producto] = total_producto

    print(f'{lista_productos[producto]}: {total_producto}')

# Modulo 2: Dia con mayores ventas totales
print(f'\nEl dia con mayores ventas totales es:')

for dia in range(len(lista_dias)):
    total_dia = 0
    # Iteramos sobre todas las ventas de un producto en un mismo dia para obtener el total de ventas
    for producto in range(len(lista_productos)):
        total_dia += ventas[producto][dia]
    ventas_por_dia[dia] = total_dia

dia_mayor_venta = lista_dias[0]
total_venta_dia = ventas_por_dia[0]

# Buscamos el indice del dia con el mayor total de ventas
for dia in range(len(lista_dias)):
    if ventas_por_dia[dia] > total_venta_dia:
        dia_mayor_venta = lista_dias[dia]
        total_venta_dia = ventas_por_dia[dia]

print(f'{dia_mayor_venta}: {total_venta_dia} ventas')

# Modulo 3: Producto mas vendido de la semana
print(f'\nEl producto mas vendido de la semana es:')

producto_mayor_venta = lista_productos[0]
total_venta_producto = ventas_por_producto[0]

# Buscamos el indice del producto con el mayor total de ventas
for producto in range(len(lista_productos)):
    if ventas_por_producto[producto] > total_venta_producto:
        producto_mayor_venta = lista_productos[producto]
        total_venta_producto = ventas_por_producto[producto]

print(f'{producto_mayor_venta}: {total_venta_producto} ventas')
