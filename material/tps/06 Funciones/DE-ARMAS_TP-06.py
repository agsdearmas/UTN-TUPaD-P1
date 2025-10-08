# TP 6: Funciones
# Alumno: De Armas Agustin
# Comision: 7


# Modulo de Validaciones

NUMEROS_ENTEROS = ('edad', 'segundos', 'numero')
NUMEROS_FLOTANTES = ('peso', 'altura', 'radio', 'celsius', 'numero_a', 'numero_b', 'numero_c')
POSITIVOS = ('edad', 'segundos', 'num_tabla', 'peso', 'altura', 'radio')

def validar_entero(num: str) -> bool:
    '''Validar numero entero.'''
    char_negativo = '-'

    if char_negativo in num:
        return False
    if not num.isdigit():
        return False
    return True

def validar_flotante(arg, num: str) -> bool:
    '''Validar numero decimal.'''
    char_punto = '.'
    char_negativo = '-'
    num_entero = num.replace(char_punto, '').replace(char_negativo, '')

    if not num_entero.isdigit():
        return False
    elif arg in POSITIVOS and float(num) < 0:
        return False
    return True

def validar_entradas(lista_argumentos: list) -> dict:
    '''
    Validar entradas ingresadas por el usuario,
    utilizando la lista de argumentos definida.
    '''
    kwargs = {}

    for arg in lista_argumentos:
        entrada = ''

        while True:
            entrada = input(f'Ingrese {arg}: ').strip()
            if not entrada:
                print('Error: Este campo no puede estar vacio.\n')
                continue

            if arg in NUMEROS_ENTEROS:
                if not validar_entero(entrada):
                    print(f'Error: {arg} debe ser un numero entero valido.\n')
                    continue
            elif arg in NUMEROS_FLOTANTES:
                if not validar_flotante(arg, entrada):
                    print(f'Error: {arg} debe ser un numero decimal valido.\n')
                    continue
            else:
                entrada.title()

            kwargs.update({arg: entrada})
            break

    return kwargs


# Modulo de Ejercicios

'''
Ejercicio 1

Se define la funcion imprimir_hola_mundo.
'''
def imprimir_hola_mundo():
    '''Imprimir mensaje en pantalla.'''
    print('Hola Mundo!')


'''
Ejercicio 2

Se define la funcion saludar_usuario(nombre).
Esta recibe un nombre como parametro y retorna un mensaje.
'''
def saludar_usuario(nombre: str) -> str:
    '''Retornar un mensaje de saludo utilizando el nombre ingresado.'''
    saludo = f'Hola {nombre}!'
    return saludo


'''
Ejercicio 3

Se define la funcion informacion_personal(nombre, apellido, edad, residencia).
Esta recibe cuatro parametros y retorna un mensaje.
'''
def informacion_personal(nombre, apellido, edad, residencia) -> str:
    '''Retornar un mensaje de informacion personal utilizando los datos ingresados.'''
    mensaje_info = f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.'
    return mensaje_info


'''
Ejercicio 4

Se define la funcion calcular_area_circulo(radio).
Se define la funcion calcular_perimetro_circulo(radio).
Estas retornan tanto el area como el perimetro de un circulo.
'''
from math import pi

def calcular_area_circulo(radio: str) -> float:
    '''Calcular y retornar el area de un circulo utilizando el radio.'''
    area = pi * float(radio)**2
    return area

def calcular_perimetro_circulo(radio: str) -> float:
    '''Calcular y retornar el perimetro de un circulo utilizando el radio.'''
    perimetro = 2 * pi * float(radio)
    return perimetro


'''
Ejercicio 5

Se define la funcion segundos_a_horas(segundos).
Esta retorna el resultado de la conversion
de los segundos ingresados a horas.
'''
def segundos_a_horas(segundos: str) -> int:
    '''Convertir segundos a horas y retornar el resultado.'''
    horas = int(segundos) / 3600
    return round(horas, 2)


'''
Ejercicio 6

Se define la funcion tabla_multiplicar(num_tabla).
Esta imprime la tabla del numero ingresado.
'''
def tabla_multiplicar(numero: str):
    '''Imprimir la tabla del numero ingresado por pantalla.'''
    tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in tabla:
        print(f'{numero} x {i} = {(int(numero)*i)}')


'''
Ejercicio 7

Se define la funcion tabla_multiplicar(num_tabla).
Esta imprime la tabla del numero ingresado.
'''
def operaciones_basicas(numero_a: str, numero_b: str) -> tuple:
    '''Calcular operaciones basicas y retornar tupla de resultados.'''
    a = float(numero_a)
    b = float(numero_b)

    suma = round(a + b, 2)
    resta = round(a - b, 2)
    multiplicacion = round(a * b, 2)
    division = round(a / b, 2)
    return (suma, resta, multiplicacion, division)


'''
Ejercicio 8

Se define la funcion tabla_multiplicar(num_tabla).
Esta imprime la tabla del numero ingresado.
'''
def calcular_imc(peso: str, altura: str) -> float:
    ''' Calcular y retornar el IMC, utilizando el peso y la altura ingresados.'''
    imc = float(peso) / (float(altura) ** 2)
    return round(imc, 2)


'''
Ejercicio 9

Se define la funcion celsius_a_fahrenheit(celsius).
Esta realiza una conversion de grados Celsius a Fahrenheit y retorna el resultado.
'''
def celsius_a_fahrenheit(celsius: str) -> float:
    '''Convertir grados Celsius a Fahrenheit y retornar el resultado'''
    fahrenheit = (float(celsius) * 9/5) + 32
    return fahrenheit


'''
Ejercicio 10

Se define la funcion calcular_promedio(a, b, c).
Esta retorna el promedio de los tres numeros ingresados.
'''
def calcular_promedio(numero_a: str, numero_b: str, numero_c: str) -> float:
    '''Calcular y retornar el promedio de los numeros ingresados.'''
    promedio = (float(numero_a) + float(numero_b) + float(numero_c)) / 3
    return round(promedio, 2)



# Modulo de Ejecucion

args = []
kwargs = {}


# Ejercicio 1
print('--- Ejercicio 1 ---')
imprimir_hola_mundo()


# Ejercicio 2
print('\n--- Ejercicio 2 ---')
nombre = input('Ingrese un nombre: ').strip().title()
saludo = saludar_usuario(nombre)
print(saludo)


# Ejercicio 3
print('\n--- Ejercicio 3 ---')
args = ['nombre', 'apellido', 'edad', 'residencia']
kwargs = validar_entradas(args)

mensaje_info = informacion_personal(**kwargs)
print(mensaje_info)


# Ejercicio 4
print('\n--- Ejercicio 4 ---')
args = ['radio']
kwargs = validar_entradas(args)

area = calcular_area_circulo(**kwargs)
perimetro = calcular_perimetro_circulo(**kwargs)
print(f'El area del circulo es: {area} y el perimetro: {perimetro}.')


# Ejercicio 5
print('\n--- Ejercicio 5 ---')
args = ['segundos']
kwargs = validar_entradas(args)

horas = segundos_a_horas(**kwargs)
print(f'La cantidad de segundos ingresados equivalen a: {horas} hs')


# Ejercicio 6
print('\n--- Ejercicio 6 ---')
args = ['numero']
kwargs = validar_entradas(args)

tabla_multiplicar(**kwargs)


# Ejercicio 7
print('\n--- Ejercicio 7 ---')
args = ['numero_a', 'numero_b']
kwargs = validar_entradas(args)

res_operaciones = operaciones_basicas(**kwargs)
operaciones = ['+', '-', 'x', '/']

for op in range(len(operaciones)):
    print(f'{kwargs["numero_a"]} {operaciones[op]} {kwargs["numero_b"]} = {res_operaciones[op]}')


# Ejercicio 8
print('\n--- Ejercicio 8 ---')
args = ['peso', 'altura']
kwargs = validar_entradas(args)

imc = calcular_imc(**kwargs)
print(f'El Indice de Masa Corporal es de: {imc}')


# Ejercicio 9
print('\n--- Ejercicio 9 ---')
args = ['celsius']
kwargs = validar_entradas(args)

fahrenheit = celsius_a_fahrenheit(**kwargs)
print(f'La conversion de grados Celsius a Fahrenheit equivale a : {fahrenheit} ºF')


# Ejercicio 10
print('\n--- Ejercicio 10 ---')
args = ['numero_a', 'numero_b', 'numero_c']
kwargs = validar_entradas(args)

promedio = calcular_promedio(**kwargs)
print(f'El promedio de los numeros ingresados es: {promedio}')
