# TP 9: Recursividad
# Alumno: De Armas Agustin
# Comision: 7


# Modulo de Utilidades

def pedir_entero_positivo(mensaje: str) -> int:
    '''Solicitar al usuario un nomero entero positivo y validar la entrada.'''
    while True:
        entrada = input(mensaje).strip()

        if not entrada.isdigit():
            print('Error: Ingrese solo numeros enteros positivos.')
            continue
        numero = int(entrada)
        if numero <= 0:
            print('Error: El numero debe ser positivo.')
            continue
        return numero

def pedir_entero_no_negativo(mensaje: str) -> int:
    '''Solicitar al usuario un numero entero no negativo y validar la entrada.'''
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print('Error: Ingrese solo numeros enteros no negativos.')
            continue
        return int(entrada)

def validar_entero_general(num: str) -> bool:
    '''Validar si una cadena representa un numero entero (positivo, negativo o cero).'''
    num = num.strip()
    if not num:
        return False

    if num[0] == '-':
        num = num[1:]

    return num.isdigit()

def validar_flotante_general(num: str) -> bool:
    '''Validar si una cadena representa un numero decimal/flotante.'''
    char_punto = '.'
    char_coma = ','
    char_negativo = '-'

    num = num.strip()
    if not num:
        return False

    # Estandarizar a punto decimal
    num = num.replace(char_coma, char_punto)

    if num[0] == char_negativo:
        num = num[1:]

    if not num:
        return False

    partes = num.split(char_punto)

    # Si tiene mas de un punto, es invalido
    if len(partes) > 2:
        return False

    # Ambas partes (entera y decimal) deben ser digitos
    for parte in partes:
        if parte and not parte.isdigit():
            return False
 
    # Manejar casos como '.' o '-'
    if len(partes) == 1 and not partes[0].isdigit():
        return False

    return True


# Ejercicio 1: Factorial

def calcular_factorial(n: int) -> int:
    '''
    Crea una funcion recursiva que calcula el factorial de un numero.
    Caso Base: Si n es 0 o 1, el factorial es 1.
    Caso Recursivo: n * factorial(n - 1).
    '''
    if n < 0:
        return -1
    if n == 0 or n == 1:    # Caso Base
        return 1
    else:
        return n * calcular_factorial(n - 1)    # Caso Recursivo

def ejecutar_ejercicio_1() -> None:
    '''Funcion principal para el ejercicio 1.'''
    print('\n1) Factorial')
    num_usuario = pedir_entero_positivo('> Ingrese un numero entero positivo (N) para calcular factoriales hasta N: ')

    print(f'Factoriales de 1 hasta {num_usuario}:')
    for i in range(1, num_usuario + 1):
        resultado = calcular_factorial(i)
        print(f'{i}! = {resultado}')


# Ejercicio 2: Serie de Fibonacci

def calcular_fibonacci(posicion: int) -> int:
    '''
    Crea una funcion recursiva que calcula el valor de la serie de Fibonacci en la posicion indicada.
    Caso Base: F(0) = 0, F(1) = 1.
    Caso Recursivo: F(n) = F(n-1) + F(n-2).
    '''
    if posicion < 0:
        return -1
    if posicion == 0:   # Primer Caso Base
        return 0
    elif posicion == 1:    # Segundo Caso Base
        return 1
    else:
        return calcular_fibonacci(posicion - 1) + calcular_fibonacci(posicion - 2)    # Caso Recursivo

def mostrar_serie_fibonacci(limite: int) -> None:
    '''Muestra la serie completa de Fibonacci hasta el limite especificado.'''
    serie = []
    for i in range(limite + 1):
        serie.append(str(calcular_fibonacci(i)))
    print(f'Serie de Fibonacci hasta la posicion {limite}: {", ".join(serie)}')

def ejecutar_ejercicio_2() -> None:
    '''Funcion principal para el ejercicio 2.'''
    print('\n2) Serie de Fibonacci')
    posicion_final = pedir_entero_no_negativo('> Ingrese la posicion final (N >= 0) para mostrar la serie de Fibonacci: ')
    mostrar_serie_fibonacci(posicion_final)


# Ejercicio 3: Potencia

def calcular_potencia(base: float, exponente: int) -> float:
    '''
    Crea una funcion recursiva que calcula la potencia de un numero base elevado a un exponente,
    utilizando la formula n^m = n * n^(m-1).
    '''
    if exponente < 0:
        # Exponente negativo (exponente^-m = 1 / exponente^m)
        return 1 / calcular_potencia(base, -exponente)
    if exponente == 0:    # Caso Base: n^0 = 1
        return 1
    elif exponente == 1:    # Caso Base implicito: n^1 = n
        return base
    else:
        return base * calcular_potencia(base, exponente - 1)    # Caso Recursivo: n^m = n * n^(m-1)

def pedir_base(mensaje: str) -> float:
    '''Solicitar un valor flotante/decimal para la base.'''
    while True:
        base_str = input(mensaje).strip()
        if validar_flotante_general(base_str):
            base_str = base_str.replace(',', '.')
            return float(base_str)
        else:
            print('Error: Ingrese un valor numerico valido (entero o decimal).')

def pedir_exponente(mensaje: str) -> int:
    '''Solicitar un valor entero para el exponente.'''
    while True:
        exponente_str = input(mensaje).strip()
        if validar_entero_general(exponente_str):
            return int(exponente_str)
        else:
            print('Error: Ingrese un valor entero valido (puede ser negativo).')


def ejecutar_ejercicio_3() -> None:
    '''Función principal para el ejercicio 3.'''
    print('\n3) Potencia Recursiva')
    
    # Solicitar y validar la base (puede ser float)
    base = pedir_base('> Ingrese la base: ')
    
    # Solicitar y validar el exponente
    exponente = pedir_exponente('> Ingrese el exponente: ')

    resultado = calcular_potencia(base, exponente)
    print(f'{base} elevado a la {exponente} es: {resultado}')


# Ejercicio 4: Decimal a Binario

def decimal_a_binario(n: int) -> str:
    '''
    Funcion recursiva que convierte un numero entero positivo en base decimal a su
    representacion en binario como una cadena de texto.
    El procedimiento es: n / 2, guardar resto. Repetir con el cociente hasta que sea 0.
    El binario se forma con los restos de abajo hacia arriba.
    '''
    if n == 0:    # Caso Base
        return ''
    else:    # Caso Recursivo
        resto = n % 2

        # Invertir el orden para simular leer de abajo hacia arriba
        return decimal_a_binario(n // 2) + str(resto)

def ejecutar_ejercicio_4() -> None:
    '''Funcion principal para el ejercicio 4.'''
    print('\n4) Decimal a Binario Recursivo')
    decimal_num = pedir_entero_no_negativo('> Ingrese un numero entero positivo o cero para convertir a binario: ')

    if decimal_num == 0:
        binario_str = '0'
    else:
        binario_str = decimal_a_binario(decimal_num)

    print(f'El numero decimal {decimal_num} en binario es: "{binario_str}"')


# Ejercicio 5: Palindromo

def es_palindromo(palabra: str) -> bool:
    '''
    Funcion recursiva que verifica si una cadena de texto es un palindromo.
    '''
    longitud = len(palabra)

    if longitud <= 1:    # Caso Base: cadena vacia o de un solo caracter
        return True
    else:    # Caso Recursivo
        if palabra[0] == palabra[longitud - 1]:
            return es_palindromo(palabra[1:longitud - 1])    # Llamada recursiva con subcadena interna
        else:
            return False

def ejecutar_ejercicio_5() -> None:
    '''Funcion principal para el ejercicio 5.'''
    print('\n5) Palindromo Recursivo')
    palabra_input = input('> Ingrese una palabra: ').strip().lower()

    if es_palindromo(palabra_input):
        print(f'La palabra "{palabra_input}" SI es un palindromo.')
    else:
        print(f'La palabra "{palabra_input}" NO es un palindromo.')


# Ejercicio 6: Suma de Digitos

def suma_digitos(n: int) -> int:
    '''
    Funcion recursiva que devuelve la suma de todos los digitos de un numero entero positivo.
    '''
    if n < 0:
        n = abs(n)    # Parseo de negativos a positivos
    if n < 10:    # Caso Base: Tiene un solo digito
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)    # Caso recursivo

def ejecutar_ejercicio_6() -> None:
    '''Funciin principal para el ejercicio 6.'''
    print('\n6) Suma de Digitos Recursiva')
    num_sumar = pedir_entero_positivo('> Ingrese un numero entero positivo para sumar sus digitos: ')

    resultado = suma_digitos(num_sumar)
    print(f'La suma de los dígitos de {num_sumar} es: {resultado}')


# Ejercicio 7: Contar Bloques de Piramide

def contar_bloques(n: int) -> int:
    '''
    Funcion recursiva que calcula el total de bloques necesarios para una piramide,
    donde el nivel mas bajo tiene 'n' bloques y cada nivel superior uno menos (n + (n-1) + ... + 1).
    '''
    if n <= 0:    # Caso Base: No quedan niveles o entrada invalida
        return 0
    elif n == 1:    # Segundo Caso Base: El ultimo nivel tiene 1 bloque
        return 1
    else:
        return n + contar_bloques(n - 1)    # Caso Recursivo: Bloques en nivel actual (n) + bloques en el resto de la piramide (n-1)

def ejecutar_ejercicio_7() -> None:
    '''Funcion principal para el ejercicio 7.'''
    print('\n7) Bloques de Piramide Recursiva')
    nivel_base = pedir_entero_positivo('> Ingrese el numero de bloques en el nivel mas bajo (N): ')

    total_bloques = contar_bloques(nivel_base)
    print(f'El total de bloques necesarios para la piramide con base {nivel_base} es: {total_bloques}')


# Ejercicio 8: Contar Digito en Numero

def contar_digito(numero: int, digito: int) -> int:
    '''
    Funcion recursiva que cuenta cuantas veces aparece un digito especifico
    dentro de un numero entero positivo.
    '''
    if numero < 0:
        numero = abs(numero)
    if numero == 0:    # Caso Base: No quedan digitos por examinar
        return 0
    else:
        # Comprobar si el ultimo digito de 'numero' coincide con 'digito'
        ultimo_digito = numero % 10
        contador_actual = 0
        if ultimo_digito == digito:
            contador_actual = 1

        return contador_actual + contar_digito(numero // 10, digito)

def ejecutar_ejercicio_8() -> None:
    '''Funcion principal para el ejercicio 8.'''
    print('\n8) Contar Digito Recursivo')
    numero = pedir_entero_no_negativo('> Ingrese el numero entero positivo: ')

    digito_str = input('Ingrese el digito a contar (0-9): ').strip()
    if not digito_str.isdigit() or len(digito_str) != 1:
        print('Error: Debe ingresar un solo digito (0-9). Usando 2 como ejemplo.')
        digito = 2
    else:
        digito = int(digito_str)

    conteo = contar_digito(numero, digito)
    print(f'El digito {digito} aparece {conteo} veces en el numero {numero}.')


# Modulo de ejecucion

if __name__ == '__main__':

    ejecutar_ejercicio_1()
    ejecutar_ejercicio_2()
    ejecutar_ejercicio_3()
    ejecutar_ejercicio_4()
    ejecutar_ejercicio_5()
    ejecutar_ejercicio_6()
    ejecutar_ejercicio_7()
    ejecutar_ejercicio_8()
