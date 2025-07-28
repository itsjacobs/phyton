#En este tercer documento empezaremos con los bucles

#1, Bucle While y break
#2. Bucle For
#3. Bucle For con range
#4. Bucle For con enumerate
#5. Bucle For con zip
#6. Bucle For con listas anidadas
#7. Bucle For con cadenas

#1. Bucle While y break

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
    if contador == 3:
        print("Se ha alcanzado el valor 3, saliendo del bucle.")
        break  # Sale del bucle cuando contador es igual a 3
print("Bucle terminado.")
#2. Bucle For
for i in range(5):
    print("Número:", i)
#3. Bucle For con range
for i in range(1, 6):  # Imprime números del 1 al 6
    print("Número:", i)
#4. Bucle For con enumerate
lista = ["a", "b", "c"]
for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")
#5. Bucle For con zip
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
for num, letra in zip(lista1, lista2):
    print(f"Número: {num}, Letra: {letra}")
#6. Bucle For con listas anidadas
matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print("Elemento:", elemento)
#7. Bucle For con cadenas
cadena = "Hola"
for letra in cadena:
    print("Letra:", letra)

#8. Bucle For con listas y condiciones
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_numeros:
    if numero % 2 == 0:  # Verifica si el número es par
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

#9. Bucle While con condiciones
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:  # Verifica si el número es par
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
print("Bucle While terminado.")




#tablas de multiplicar
print("Tablas de multiplicar del 0 al 10:")
for multiplo in range(0, 11):  # Del 0 al 10
    for i in range(0, 11):  # Del 0 al 10
        resultado = multiplo * i
        print(f"{multiplo} x {i} = {resultado}")
    print()  # Línea en blanco entre tablas

