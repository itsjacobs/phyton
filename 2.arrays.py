#En este segundo documento tendremos los arrays o listas

#1, Tipos de Listas
#2. Acceso a los elementos de una lista
#3. Slicing de listas
#4. Desde hasta paso
#5. Modificar y añadir elementos a una lista
#6. Métodos de listas

#1. Tipos de Listas
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = [1.1, 2.2, 3.3] # Lista de flotantes
lista3 = ["a", "b", "c"] # Lista de cadenas
lista4 =[True, False, True] # Lista de booleanos
lista5 = [1,"a", 3.5, True] # Lista mixta
lista6 = [[1, 2], [3, 4]] # Lista de listas

print ("Lista de enteros:", lista1)
print ("Lista de flotantes:", lista2)
print ("Lista de cadenas:", lista3)
print ("Lista de booleanos:", lista4)
print ("Lista mixta:", lista5)
print ("Lista de listas:", lista6)



#2. Acceso a los elementos de una lista
print("Primer elemento de lista1:", lista1[0]) # Acceso al primer elemento
print("Último elemento de lista1:", lista1[-1]) # Acceso al último
print(lista6[0][1]) # Acceso a un elemento de una lista dentro de una lista


#3. Slicing de listas
print("Elementos del índice 1 al 3 de lista1:", lista1[1:4]) # Slicing de lista1
print("Elementos del índice 0 al 2 de lista2:", lista2[:3]) # Slicing de lista2
print("Elementos del índice 2 al final de lista3:", lista3[2:]) # Slicing de lista3
print(lista1[:]) # Imprime todos los elementos de lista1 en una COPIA


#4. Desde hasta paso
lista_ejemplo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_ejemplo[::2]) # Imprime los elementos con paso de 2
print(lista_ejemplo[1::3]) # Imprime los elementos con paso de 3 desde el índice 1
print(lista_ejemplo[::]) # Imprime todos los elementos en una COPIA


#5. Modificar y añadir elementos a una lista

lista1[0] = 10 # Modifica el primer elemento de lista1
print(lista1[0]) # Imprime el primer elemento modificado

#5.1 Añadir elementos

lista1 = [1,2,3]
lista1 += [4, 5] # Añade los elementos 4 y 5 al final de lista1
print("Lista1 después de añadir elementos:", lista1)



#6. Métodos de listas

#6.1 Métodos sueltos o cosas útiles
print("Longitud de lista1:", len(lista1)) # Devuelve la longitud de lista1
print(lista1.count(2)) # Cuenta cuántas veces aparece el número 2 en lista1
print(lista1.index(3)) # Devuelve el índice del primer elemento con valor 3
print(1 in lista1) # Comprueba si el número 1 está en lista1
print(1000 not in lista1) # Comprueba si el número 100 no está en lista1



#6.2 Añadir elementos
lista1.append(6) # Añade el elemento 6 al final de lista1
print("Lista1 después de append:", lista1)
lista1.extend([7, 8]) # Añade más de 1 elemento al final de lista1
print("Lista1 después de extend:", lista1)
lista1.insert(1, 100) # Inserta el elemento 100 en el índice 1 y empuja los demas a la derecha
print("Lista1 después de insertar 100:", lista1)

#6.3 Ordenar elementos
lista1.sort() # Ordena los elementos de lista1
print("Lista1 después de sort:", lista1)
sorted_lista1 = sorted(lista1) # Crea una copia ordenada de lista1
print("Copia ordenada de lista1:", sorted_lista1)
lista1.reverse() # Invierte el orden de los elementos de lista1
print("Lista1 después de reverse:", lista1)
sorted_lista1_reverse = sorted(lista1, reverse=True) # Crea una copia ordenada de lista1 en orden inverso
print("Copia ordenada de lista1 en orden inverso:", sorted_lista1_reverse)


#6.4 Eliminar elementos
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11] # Reiniciamos lista1 para eliminar elementos
del lista1[8:10] # Elimina los elementos del índice 8 al 9 (incluido)
print("Lista1 después de eliminar del índice 8 al 9:", lista1)
lista1.remove(4) # Elimina el primer elemento con valor 4 de lista1
print("Lista1 después de insertar 100 y eliminar 4:", lista1)
lista1.pop() # Elimina el último elemento de lista1
print("Lista1 después de pop:", lista1)
lista1.pop(0) # Elimina el elemento que le pongas como argumento de entrada en este caso el primer elemento
print("Lista1 después de pop en el índice 0:", lista1)
lista1.clear() # Elimina todos los elementos de lista1
print("Lista1 después de clear:", lista1)
print("Comprobación")





