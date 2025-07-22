import math
import string

#En este primer documeto tendremos lo siguiente:
#1. Tipos de Variables
#2. Funciones sencillas
#3. Ejercicios de secuenciales
#4. Introduccion a las estructuras de control

#1. Tipos de Variables

#Variables de tipo entero

a = 10
b = 20
c = a + b
print("La suma de a y b es:", c)

print("dime el valor de a:")
a = int(input())
print ("dime el valor de b:")
b = int(input())
c = a + b
print("La suma de a y b es:", c)

#Variables de tipo flotante

x = 10.5
y = 20.3
z = x + y
print("La suma de x y y es:", z)

#Variables de tipo cadena

nombre= string(input("dime que quieres de  nombre"))
apellido = string(input("dimer el apellido que quieres"))
print("El nombre completo es:", nombre + " " + apellido)

#Variables booleanas
es_estudiante = True
tiene_trabajo = False
print("Es estudiante:", es_estudiante)
print("Tiene trabajo:", tiene_trabajo)

#2. Funciones sencillas

def sumar(a, b):
    return a + b

# Solicitar al usuario dos números y mostrar la suma
print("que numeros quieres sumar?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = sumar(num1, num2)
print("La suma es:", resultado)

def restar(a, b):
    return a - b

# Solicitar al usuario dos números y mostrar la resta
print ("que numeros quieres restar?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = restar(num1, num2)
print("La resta es:", resultado)

def multiplicar(a, b):
    return a * b

# Solicitar al usuario dos números y mostrar la multiplicación
print("que numeros quieres multiplicar?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = multiplicar(num1, num2)
print("La multiplicación es:", resultado)

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
    
# Solicitar al usuario dos números y mostrar la división
print("que numeros quieres dividir?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = dividir(num1, num2)
print("La división es:", resultado)
    

    
#3. Ejercicios de secuenciales


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(calcular_area_rectangulo(num1, num2))


def calcular_area_rectangulo(base, altura):
    return base * altura
def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

#4. Introducción a las estructuras de control
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"


