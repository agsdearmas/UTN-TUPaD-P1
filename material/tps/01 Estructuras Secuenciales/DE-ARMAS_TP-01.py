# TP 1: Estructuras Secuenciales
# Alumno: De Armas Agustin

# Ejercicio 1
print('Hola Mundo!')

# Ejercicio 2
nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}!')

# Ejercicio 3
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
residencia = input('Ingrese su lugar de residencia: ')
print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# Ejercicio 4
radio = int(input('Ingrese el radio de un circulo: '))
area = 3.1416 * (radio**2)
perimetro = 2 * 3.1416 * radio
print(f'El area es: {area}, y el perimetro: {perimetro}')

# Ejercicio 5
segundos = int(input('Ingrese la cantidad de segundos: '))
horas = segundos // 3600
print(f'La cantidad de segundos ingresada equivale a: {horas}hs')

# Ejercicio 6
numero = int(input('Ingrese un numero: '))
resultado = 0

resultado = numero * 1
print(f'{numero} x 1 = {resultado}')
resultado = numero * 2
print(f'{numero} x 2 = {resultado}')
resultado = numero * 3
print(f'{numero} x 3 = {resultado}')
resultado = numero * 4
print(f'{numero} x 4 = {resultado}')
resultado = numero * 5
print(f'{numero} x 5 = {resultado}')
resultado = numero * 6
print(f'{numero} x 6 = {resultado}')
resultado = numero * 7
print(f'{numero} x 7 = {resultado}')
resultado = numero * 8
print(f'{numero} x 8 = {resultado}')
resultado = numero * 9
print(f'{numero} x 9 = {resultado}')
resultado = numero * 10
print(f'{numero} x 10 = {resultado}')

# Ejercicio 7
primerNum = int(input('Ingrese el primer numero distinto de 0: '))
segundoNum = int(input('Ingrese el segundo numero distinto de 0: '))
resultado = 0

resultado = primerNum + segundoNum
print(f'{primerNum} + {segundoNum} = {resultado}')
resultado = primerNum // segundoNum
print(f'{primerNum} // {segundoNum} = {resultado}')
resultado = primerNum * segundoNum
print(f'{primerNum} * {segundoNum} = {resultado}')
resultado = primerNum - segundoNum
print(f'{primerNum} - {segundoNum} = {resultado}')

# Ejercicio 8
altura = float(input('Ingrese su altura: '))
peso = float(input('Ingrese su peso: '))
imc = peso / (altura**2)
print(f'El IMC es igual a: {imc}')

# Ejercicio 9
celsius = float(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'El equivalente en grados fahrenheit es: {fahrenheit} °F')

# Ejercicio 10
primerNum = float(input('Ingrese el primer numero: '))
segundoNum = float(input('Ingrese el segundo numero: '))
tercerNum = float(input('Ingrese el tercer numero: '))
promedio = (primerNum + segundoNum + tercerNum) / 3
print(f'El promedio es: {promedio}')
