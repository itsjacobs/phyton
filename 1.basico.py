import math
import os
os.system("clear")
#En este primer documeto tendremos lo siguiente:
#1. Tipos de Variables
#2. Funciones sencillas
#3. Introduccion a las estructuras de control

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

nombre= input("dime el nombre que quieres: ") # EL input de tipo string no hace falta definir que es de tipo String
apellido = input("dime el apellido que quieres")
print("El nombre completo es:", nombre + " " + apellido)
pais, ciudad = input("dime el pais y la ciudad que quieres: ").split()
print("El país es:", pais)
print("La ciudad es:", ciudad)

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
resultado = sumar(num1, num2) # Usamos la función sumar previamente creada
print("La suma es:", resultado)

def restar(a, b):
    return a - b

# Solicitar al usuario dos números y mostrar la resta

print ("que numeros quieres restar?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = restar(num1, num2) # Usamos la función restar previamente creada
print("La resta es:", resultado)

def multiplicar(a, b):
    return a * b

# Solicitar al usuario dos números y mostrar la multiplicación

print("que numeros quieres multiplicar?")
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
resultado = multiplicar(num1, num2) # Usamos la función multiplicar previamente creada
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
resultado = dividir(num1, num2) # Usamos la función dividir previamente creada
print("La división es:", resultado)

#4. Introducción a las estructuras de control

#Tenemos los if, elif y else    
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
    

def verificar_edad(edad):
    if edad < 18:
        return "Eres menor de edad"
    elif edad == 18:
        return "Tienes 18 años, eres mayor de edad"
    else:
        return "Eres mayor de edad"
    

edad = int(input("Ingrese su edad: "))
resultado = verificar_edad(edad)
print(resultado)

edad2= int(input("Ingrese su edad: "))
a = input("¿Tienes carnet de conducir? (si/no): ").strip().lower()
if a == "si":
    carnet = True
else:
    carnet = False

if carnet and edad2 >= 18:
    print("Puedes conducir")
else:
    print("No puedes conducir")

