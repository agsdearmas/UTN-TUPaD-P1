# TP 8: Manejo de Archivos
# Alumno: De Armas Agustin
# Comision: 7

import os


# Módulo de validaciones

POSITIVOS = ('precio',)

def validar_entero(num: str) -> bool:
    '''Validar numero entero. Permite solo dígitos positivos para esta validación.'''
    char_negativo = '-'
    if char_negativo in num:
        return False
    if not num.isdigit():
        return False
    return True

def validar_flotante(arg, num: str) -> bool:
    '''Validar número decimal. Reemplaza coma por punto y verifica que pertenezca al formato.'''
    char_punto = '.'
    char_negativo = '-'
    num = num.replace(',', '.')
    num_entero = num.replace(char_punto, '').replace(char_negativo, '')
    if not num_entero.isdigit():
        return False
    elif arg in POSITIVOS and float(num) < 0:
        return False
    return True


# Funciones

def crear_archivo_inicial(ruta_archivo: str) -> None:
    '''
    Ejercicio 1:
    Crear archivo inicial productos.txt con 3 productos si no existe.
    Formato por línea: nombre,precio,cantidad
    '''
    if os.path.exists(ruta_archivo):
        print(f'El archivo "{ruta_archivo}" ya existe. Se mantiene el contenido actual.')
        return

    productos_iniciales = [
        'Notebook,120000.5,30',
        'Mouse,2500,15',
        'Televisor,50000,100'
    ]
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        for linea in productos_iniciales:
            archivo.write(linea + '\n')
    print(f'Archivo "{ruta_archivo}" creado con 3 productos iniciales.')


def leer_y_mostrar_productos(ruta_archivo: str) -> None:
    '''
    Ejercicio 2:
    Leer productos.txt y mostrar cada producto con formato:
    Producto: Lapicera | Precio: $120.5 | Cantidad: 30
    '''
    if not os.path.exists(ruta_archivo):
        print('No se encontró el archivo de productos.')
        return
    print('\nLista de Productos')

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        columnas = linea.split(',')

        if len(columnas) != 3:
            continue
        nombre = columnas[0].strip().title()
        precio = columnas[1].strip()
        cantidad = columnas[2].strip()
        print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')


def agregar_producto_desde_teclado(ruta_archivo: str) -> None:
    '''
    Ejercicio 3:
    Pedir un nuevo producto (nombre, precio, cantidad) y agregarlo al archivo
    sin borrar el contenido existente.
    '''
    print('\nAgregar nuevo producto')
    nombre = ''
    while True:
        nombre = input('Ingrese nombre del producto: ').strip()
        if not nombre:
            print('Error: El nombre no puede estar vacío.')
            continue
        nombre = nombre.title()
        break

    # Validar flotante ingresado
    precio_str = ''
    while True:
        precio_str = input('Ingrese precio (ej: 120.5): ').strip()
        if not validar_flotante('precio', precio_str):
            print('Error: Ingrese un precio válido.')
            continue
        # Estandarizamos a punto decimal
        precio_str = precio_str.replace(',', '.')
        break

    # Validar entero ingresado
    cantidad_str = ''
    while True:
        cantidad_str = input('Ingrese cantidad (entero positivo): ').strip()
        if not validar_entero(cantidad_str):
            print('Error: Ingrese una cantidad entera y positiva.')
            continue
        break

    # Agregar al archivo en modo append
    with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(f'{nombre},{precio_str},{cantidad_str}\n')

    print(f'Producto "{nombre}" agregado a "{ruta_archivo}".')


def cargar_productos_en_lista(ruta_archivo: str) -> list:
    '''
    Ejercicio 4:
    Leer el archivo y cargar los productos en una lista de diccionarios
    con claves: nombre, precio, cantidad.
    Retorna la lista.
    '''
    productos = []
    if not os.path.exists(ruta_archivo):
        return productos

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(',')
            if len(partes) != 3:
                continue
            nombre = partes[0].strip().title()
            precio_raw = partes[1].strip().replace(',', '.')
            cantidad_raw = partes[2].strip()

            # Si no son válidos, salteamos el registro
            if not validar_flotante('precio', precio_raw) or not validar_entero(cantidad_raw):
                continue

            producto_dict = {
                'nombre': nombre,
                'precio': float(precio_raw),
                'cantidad': int(cantidad_raw)
            }
            productos.append(producto_dict)
    return productos


def buscar_producto_por_nombre(productos: list) -> None:
    '''
    Ejercicio 5:
    Pedir al usuario un nombre de producto y buscarlo en la lista.
    Si lo encuentra, mostrar todos sus datos; si no, mostrar mensaje de error.
    '''
    print('\nBuscar producto por nombre')
    if not productos:
        print('La lista de productos está vacía.')
        return

    nombre_buscar = input('Ingrese el nombre del producto a buscar: ').strip()
    if not nombre_buscar:
        print('Error: Nombre vacío.')
        return
    nombre_buscar = nombre_buscar.title()

    encontrado = False
    for producto in productos:
        if producto['nombre'] == nombre_buscar:
            print(f'Producto encontrado: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}')
            encontrado = True
            break

    if not encontrado:
        print(f'Error: El producto "{nombre_buscar}" no existe en la lista.')


def guardar_productos_actualizados(ruta_archivo: str, productos: list) -> None:
    '''
    Ejercicio 6:
    Sobrescribir el archivo productos.txt escribiendo todos los productos desde la lista.
    Formato por línea: nombre,precio,cantidad
    '''
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        for producto in productos:
            # Validar formato: nombre con título, precio con punto decimal, cantidad entero
            nombre = producto['nombre'].title()
            precio = str(producto['precio'])
            cantidad = str(producto['cantidad'])
            archivo.write(f'{nombre},{precio},{cantidad}\n')
    print(f'Archivo "{ruta_archivo}" actualizado con {len(productos)} productos.')


# Módulo de ejecución

if __name__ == '__main__':
    CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
    ARCHIVO_PRODUCTOS = os.path.join(CARPETA_ACTUAL, 'productos.txt')

    # Ejercicio 1: Crear archivo inicial con 3 productos (si no existe)
    crear_archivo_inicial(ARCHIVO_PRODUCTOS)

    # Ejercicio 2: Leer y mostrar productos
    leer_y_mostrar_productos(ARCHIVO_PRODUCTOS)

    # Ejercicio 3: Agregar un producto desde teclado
    agregar_producto_desde_teclado(ARCHIVO_PRODUCTOS)

    # Ejercicio 4: Cargar productos en una lista de diccionarios
    productos_lista = cargar_productos_en_lista(ARCHIVO_PRODUCTOS)
    print('\nLista cargada en memoria (productos)')
    for p in productos_lista:
        print(p)

    # Ejercicio 5: Buscar producto por nombre dentro de la lista
    buscar_producto_por_nombre(productos_lista)

    # Ejercicio 6: Guardar los productos actualizados sobrescribiendo el archivo
    guardar_productos_actualizados(ARCHIVO_PRODUCTOS, productos_lista)

    print('\nProceso finalizado. Verifica "productos.txt" en el directorio del script.')
