# TP 3: Estructuras Condicionales
# Alumno: De Armas Agustin
# Comision: 7

import random
from statistics import mode, median, mean


'''
Ejercicio1

Se solicita al usuario que ingrese su edad, en caso de ser mayor de 18
se imprime un mensaje.
'''
usr_edad = int(input('Por favor, ingrese su edad: '))

if usr_edad >= 18:
    print('Es mayor de edad')
else:
    pass


'''
Ejercicio 2

Se solicita al usuario que ingrese su nota, en caso de ser mayor de 6
se imprime un mensaje de aprobado, en el caso contrario desaprobado.
'''
usr_nota = int(input('Por favor, ingrese su nota: '))

if usr_nota >= 6:
    print('Alumno aprobado')
else:
    print('Alumno desaprobado')


'''
Ejercicio 3

Se solicita al usuario que ingrese un numero par.
Si es par se imprime un mensaje de numero correcto,
en el caso contrario se imprime un mensaje de reintento.
'''
num_par = int(input('Por favor, ingrese un numero par: '))

if (num_par % 2 == 0):
    print('Ha ingresado un numero par')
else:
    print('Por favor, ingrese un numero par')


'''
Ejercicio 4

Se solicita al usuario que ingrese su edad, y se clasifica por categoria.
Niño/a: menor de 12 años
Adolescente: mayor o igual que 12 años y menor que 18 años
Adulto/a joven: mayor o igual que 18 años y menor que 30 años
Adulto/a: mayor o igual que 30 años
'''
usr_edad = int(input('Por favor, ingrese su edad: '))

if usr_edad < 12:
    print('Usted es Niño/a')
elif usr_edad >= 12 and usr_edad < 18:
    print('Usted es Adolescente')
elif usr_edad >= 18 and usr_edad < 30:
    print('Usted es Adulto/a joven')
else:
    print('Usted es Adulto/a mayor')


'''
Ejercicio 5

Se solicita al usuario que ingrese una contraseña de entre 8 y 14 caracteres.
Si se cumple la condicion, se imprime un mensaje de exito,
en el caso contrario se imprime un mensaje de reintento.
'''
usr_contra = str(input('Ingrese una contraseña de entre 8 y 14 caracteres: '))

if len(usr_contra) >= 8 and len(usr_contra) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


'''
Ejercicio 6

Se define una lista con un rango de 50 numeros aleatorios.
Calculamos la moda, mediana y media utilizando el modulo statistics y
luego comparamos las mismas para determinar si hay sesgo positivo,
negativo o si no hay sesgo.
'''
num_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(num_aleatorios)
mediana = median(num_aleatorios)
media = mean(num_aleatorios)

if media > mediana and mediana > moda:
    print('Sesgo positivo')
elif media < mediana and mediana < moda:
    print('Sesgo negativo')
elif media == mediana == moda:
    print('No hay sesgo')
else:
    pass


'''
Ejercicio 7

Se solicita al usuario que ingrese una frase o palabra.
Si esta termina en vocal se le añade un signo de exclamacion y se imprime,
en el caso contrario se imprime el string sin modificaciones.
'''
usr_frase = str(input('Por favor, ingrese una frase o palabra: '))
ultima_palabra = usr_frase[-1].lower()
vocales = 'aeiou'

# Validamos si el ultimo caracter se encuentra dentro de las vocales
if ultima_palabra in vocales:
    usr_frase += '!'
    print(f'{usr_frase}')
else:
    print(f'{usr_frase}')


'''
Ejercicio 8

Se solicita al usuario que ingrese su nombre.
Luego se le solicita ingresar la opcion 1, 2 o 3.
En caso de
opcion 1: se convierte el nombre a mayusculas
opcion 2: se convierte el nombre a minusculas
opcion 3: se convierte la primera letra a mayuscula
'''
usr_name = str(input('Por favor, ingrese su nombre: '))
usr_opc = int(input('Ingrese alguna de las siguientes opciones:\n'
                    '1: Convertir a mayusculas\n2: Convertir a minusculas\n'
                    '3: Convertir primera letra a mayuscula:\n'))

# Verificamos que el valor ingresado corresponda a una opcion valida
if usr_opc == 1:
    usr_name = usr_name.upper()
    print(f'{usr_name}')
elif usr_opc == 2:
    usr_name = usr_name.lower()
    print(f'{usr_name}')
elif usr_opc == 3:
    usr_name = usr_name.title()
    print(f'{usr_name}')
else:
    print('La opcion ingresada es incorrecta, intente de nuevo.')


'''
Ejercicio 9

Se solicita al usuario que ingrese la magnitud de un terremoto.
Luego se clasifica en las siguientes categorias:
Menor que 3: "Muy leve" (imperceptible)
Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible)
Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños)
Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras
debiles)
Mayor o igual que 6  y menor que 7: "Muy Fuerte"
(puede causar daños significativos)
Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)
'''
magnitud = float(input('Por favor, ingrese la magnitud de un terremoto: '))

# Verificamos el rango del valor ingresado y lo clasificamos por categoria
if magnitud < 3:
    print('Muy leve (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('Leve (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte (puede causar daños en estructuras debiles)')
elif magnitud >= 6 and magnitud < 7:
    print('Muy Fuerte (puede causar daños significativos)')
else:
    print('Extremo (puede causar graves daños a gran escala)')


'''
Ejercicio 10

Se solicita al usuario que ingrese hemisferio, mes y dia.
Si los datos ingresados son validos, se clasifica y determina la estacion correspondiente
segun el hemisferio.
'''
# Solicitamos ingreso de hemisferio, mes y dia al usuario
hemisferio = str(input('Por favor, ingrese el hemisferio en el cual se encuentra:\n'
                       'N: Hemisferio Norte\nS: Hemisferio Sur\n')).upper()

mes = int(input('Por favor, ingrese el mes actual:\n(1: Enero, 2: Febrero, 3: Marzo, 4: Abril, 5: Mayo, '
                '6: Junio, 7: Julio, 8: Agosto, 9: Septiembre, 10: Octubre, 11: Noviembre, 12: Diciembre)\n'))

dia = int(input('Por favor, ingrese el dia actual dentro del rango (1, 31): '))

# Verificamos que los datos ingresados correspondan a opciones validas
if hemisferio != 'N' and hemisferio != 'S':
    print('Hemisferio incorrecto, por favor intente nuevamente')
elif not (1 <= mes <= 12):
    print('Mes incorrecto, por favor intente nuevamente')
elif not (1 <= dia <= 31):
    print('Dia incorrecto, por favor intente nuevamente')
else:
    # Clasificamos segun el hemisferio y determinamos la estacion correspondiente
    if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
            estacion = 'Invierno'
        elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
            estacion = 'Primavera'
        elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
            estacion = 'Verano'
        else:
            estacion = 'Otoño'
    else:
        if (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
            estacion = 'Verano'
        elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
            estacion = 'Otoño'
        elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
            estacion = 'Invierno'
        else:
            estacion = 'Primavera'
    
    print(f'La estacion actual es: {estacion}')
