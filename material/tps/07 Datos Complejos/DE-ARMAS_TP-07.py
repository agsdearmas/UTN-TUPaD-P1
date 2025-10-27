# TP 7: Estructuras de Datos Complejas
# Alumno: De Armas Agustin
# Comision: 7

import re


# Modulo de Validaciones

POSITIVOS = ('nota_str')

def validar_entero(num: str) -> bool:
    '''Validar numero entero. Permite solo digitos positivos para esta validacion.'''
    if not num.isdigit():
        return False
    return True

def validar_flotante(arg, num: str) -> bool:
    '''Validar numero decimal. Permite solo positivos si el argumento lo requiere.'''
    char_punto = '.'
    char_negativo = '-'
    
    num = num.replace(',', '.')
    num_entero = num.replace(char_punto, '').replace(char_negativo, '')

    if not num_entero.isdigit():
        return False
    elif arg and arg in POSITIVOS and float(num) < 0:
        return False
    return True


# Modulo de Ejercicios

'''
Ejercicio 3 (La lógica simple se resuelve en el Módulo de Ejecución)
Crea una lista con solo las frutas del diccionario.
'''
def obtener_solo_frutas(precios_frutas: dict) -> list:
    '''Crea y retorna una lista que contiene solo las frutas (claves) del diccionario.'''
    return list(precios_frutas.keys())


'''
Ejercicio 4
Permite almacenar y consultar numeros telefonicos utilizando un diccionario.
'''
def crear_y_consultar_contactos():
    '''
    Permite al usuario cargar 5 contactos (nombre: clave, numero: valor)
    y luego consultar el numero de un nombre.
    '''
    contactos = {}
    NUM_CONTACTOS = 5

    print('Carga de 5 contactos')
    for i in range(NUM_CONTACTOS):
        nombre = input(f'Ingrese el nombre del contacto {i+1}: ').strip().title()
        
        numero = ''
        while True:
            numero = input(f'Ingrese el número de {nombre}: ').strip()
            if not numero:
                print('Error: El número no puede estar vacío.')
                continue
            break
        
        contactos[nombre] = numero

    print('\nConsulta de Contacto')
    nombre_a_consultar = input('Ingrese el nombre a consultar: ').strip().title()
    numero_asociado = contactos.get(nombre_a_consultar)

    if numero_asociado:
        print(f'El número asociado a {nombre_a_consultar} es: {numero_asociado}')
    else:
        print(f'Error: El contacto "{nombre_a_consultar}" no se encuentra en la agenda.')


'''
Ejercicio 5
Solicita una frase, e imprime sus palabras unicas (set) y el recuento de palabras (diccionario).
'''
def analizar_frase():
    '''
    Solicita una frase al usuario, e imprime las palabras únicas (set)
    y la cantidad de veces que aparece cada palabra (diccionario).
    '''
    frase = input('Ingrese una frase: ').strip().lower()
    
    # Obtener solo las palabras, ignorando puntuación
    palabras = re.findall(r'\b\w+\b', frase) 
    
    # Palabras unicas
    palabras_unicas = set(palabras)

    # Conteo de palabras
    recuento_palabras = {}
    for palabra in palabras:
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

    print(f'\nPalabras únicas: {palabras_unicas}')
    print(f'Recuento: {recuento_palabras}')


'''
Ejercicio 6
Permite ingresar alumnos y sus notas (en una tupla), luego muestra el promedio de cada uno.
'''
def calcular_promedio_alumnos():
    '''
    Permite ingresar los nombres de 3 alumnos y una tupla de 3 notas para cada uno.
    Luego, muestra el promedio de cada alumno.
    '''
    alumnos = {}
    NUM_ALUMNOS = 3
    NUM_NOTAS = 3

    print('Carga de Notas de 3 Alumnos')
    for i in range(NUM_ALUMNOS):
        nombre = input(f'Ingrese el nombre del alumno {i+1}: ').strip().title()
        notas = []
        for j in range(NUM_NOTAS):
            while True:
                nota_str = input(f'Ingrese la nota {j+1} para {nombre} (0-10): ').strip()
                
                # Validar que la entrada sea un número flotante
                if not validar_flotante('nota_str', nota_str):
                    print('Error: Ingrese un número entero válido.')
                    continue
                        
                nota = int(nota_str)
                
                # Validar que la nota esté en el rango permitido
                if nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print('Error: La nota debe estar entre 0 y 10.')

        alumnos[nombre] = tuple(notas)

    print('Promedio de Alumnos')
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f'El promedio de {nombre} es: {promedio:.2f}')


'''
Ejercicio 7
Dados dos sets (Parcial 1 y Parcial 2), muestra aprobados en ambos, solo uno, y total (sin repetir).
'''
def analizar_aprobados():
    '''Realiza operaciones con sets para mostrar aprobados de ambos, solo uno, y el total sin repetir.'''
    parcial_1 = {'Juan', 'Ana', 'Pedro', 'Sofía', 'Luis', 'Carla'}
    parcial_2 = {'Ana', 'Pedro', 'Martín', 'Luis', 'Elías', 'Carla'}

    print(f'Aprobados Parcial 1: {parcial_1}')
    print(f'Aprobados Parcial 2: {parcial_2}')

    # Aprobaron ambos parciales: Intersección (&)
    ambos_aprobados = parcial_1 & parcial_2

    # Aprobaron solo uno de los dos: Diferencia simétrica (^)
    solo_uno_aprobado = parcial_1 ^ parcial_2

    # Lista total de estudiantes que aprobaron al menos un parcial: Unión (|)
    total_aprobados = parcial_1 | parcial_2

    print(f'\nAprobaron ambos parciales (Intersección): {ambos_aprobados}')
    print(f'Aprobaron solo uno de los dos (Diferencia Simétrica): {solo_uno_aprobado}')
    print(f'Total de estudiantes que aprobaron al menos uno (Unión): {total_aprobados}')


'''
Ejercicio 8
Arma un diccionario de productos y stock, permitiendo consultar, agregar unidades o crear uno nuevo.
'''
def gestionar_stock():
    '''
    Implementa un sistema de gestión de stock simple:
    permite consultar stock, agregar unidades o añadir un nuevo producto.
    '''
    stock_productos = {'Televisor': 15, 'Notebook': 22, 'Mouse': 50}

    while True:
        print('\nGestión de Stock')
        print(f'Stock actual: {stock_productos}')
        print('1. Consultar Stock')
        print('2. Agregar Unidades / Nuevo Producto')
        print('3. Salir')

        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            producto = input('Ingrese el nombre del producto a consultar: ').strip().title()
            stock = stock_productos.get(producto)
            if stock is not None:
                print(f'El stock de {producto} es: {stock} unidades.')
            else:
                print(f'El producto "{producto}" no existe en el inventario.')

        elif opcion == '2':
            producto = input('Ingrese el nombre del producto: ').strip().title()
            
            cantidad = 0
            while True:
                cantidad_str = input('Ingrese la cantidad a agregar: ').strip()
                if not validar_entero(cantidad_str):
                    print('Error: Ingrese un número entero válido y positivo.')
                    continue
                cantidad = int(cantidad_str)
                break

            if producto in stock_productos:
                stock_productos[producto] += cantidad
                print(f'Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}')
            else:
                stock_productos[producto] = cantidad
                print(f'El producto "{producto}" fue agregado con {cantidad} unidades de stock.')

        elif opcion == '3':
            print('Saliendo del gestor de stock.')
            break
        else:
            print('Opción no válida. Intente de nuevo.')


'''
Ejercicio 9
Crea una agenda donde las claves son tuplas (dia, hora) y los valores son eventos.
Permite consultar un evento por dia y hora.
'''
def gestionar_agenda():
    '''
    Crea una agenda con tuplas (día, hora) como claves y eventos como valores.
    Permite consultar qué actividad hay en un día y hora específicos.
    '''
    agenda = {
        ("lunes", "10:00"): "Reunión de equipo",
        ("martes", "15:00"): "Clase de inglés",
        ("jueves", "09:30"): "Entrega de proyecto"
    }
    print('Agenda de ejemplo:', agenda)

    dia = input('Ingrese el día a consultar (ej: lunes): ').strip().lower()
    hora = input('Ingrese la hora a consultar (ej: 10:00): ').strip()
    clave_consulta = (dia, hora)

    evento = agenda.get(clave_consulta)

    if evento:
        print(f'El evento para el {dia.title()} a las {hora} es: "{evento}"')
    else:
        print(f'No hay ninguna actividad registrada para el {dia.title()} a las {hora}.')


'''
Ejercicio 10
Dado un diccionario que mapea paises con capitales,
construye uno nuevo con las claves y valores invertidos.
'''
def invertir_diccionario(paises_capitales: dict) -> dict:
    '''
    Construye y retorna un nuevo diccionario donde las claves son las capitales
    y los valores son los países del diccionario original.
    '''
    # Uso de comprensión de diccionarios
    return {capital: pais for pais, capital in paises_capitales.items()}


# Modulo de Ejecucion

if __name__ == '__main__':
    
    # Diccionario inicial para los ejercicios 1, 2 y 3
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    print('Ejercicio 1: Añadir Frutas')
    print(f'Diccionario Inicial: {precios_frutas}')
    
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    print(f'Diccionario actualizado: {precios_frutas}')
    
    
    print('\nEjercicio 2: Actualizar Precios')
    
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    print(f'Diccionario después de actualizar precios: {precios_frutas}')
    
    # Ejercicio 3
    print('\nEjercicio 3: Obtener solo Frutas')
    lista_solo_frutas = obtener_solo_frutas(precios_frutas)
    print(f'Lista de frutas: {lista_solo_frutas}')
    
    
    # Ejercicio 4
    print('\nEjercicio 4: Almacenar y Consultar Contactos')
    crear_y_consultar_contactos()
    
    
    # Ejercicio 5
    print('\nEjercicio 5: Análisis de Frase (Set y Conteo)')
    analizar_frase()
    
    
    # Ejercicio 6
    print('\nEjercicio 6: Promedio de Alumnos (Diccionario y Tupla)')
    calcular_promedio_alumnos()
    
    
    # Ejercicio 7
    print('\nEjercicio 7: Operaciones con Sets de Aprobados')
    analizar_aprobados()
    
    
    # Ejercicio 8
    print('\nEjercicio 8: Gestión de Stock de Productos')
    gestionar_stock()
    
    
    # Ejercicio 9
    print('\nEjercicio 9: Agenda con Clave de Tupla')
    gestionar_agenda()
    
    
    # Ejercicio 10
    print('\nEjercicio 10: Inversión de Diccionario')
    paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo", "Perú": "Lima"}
    diccionario_invertido = invertir_diccionario(paises_capitales)
    print(f'Diccionario original: {paises_capitales}')
    print(f'Diccionario invertido: {diccionario_invertido}')
