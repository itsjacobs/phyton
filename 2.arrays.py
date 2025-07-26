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
lista1.append(6) # Añade el elemento 6 al final de lista1
print("Lista1 después de añadir 6:", lista1)

#6. Métodos de listas
len(lista1) # Devuelve la longitud de lista1
print("Longitud de lista1:", len(lista1))




