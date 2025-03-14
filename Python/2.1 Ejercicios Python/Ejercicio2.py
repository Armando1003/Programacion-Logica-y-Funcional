#tipos de datos

print("\nTipos de datos")

lista = [1, 2, 3, 4, 5]
print("\nListas: ", lista)
print("Valor de la primera posición: ", lista[0])#imprime el primer elemento de la lista
print("Valor de la segunda posición: ", lista[1])#imprime el segundo elemento (2)

#tuplas
tupla = (1, 2, 3, 4, 5)
print("\nTuplas: ", tupla)
print("Valor de la primera posición: ", tupla[0])#imprime el primer elemento de la tupla
print("Valor de la segunda posición: ", tupla[1])

#diccionarios
diccionario = {'nombre': 'Juan', 'edad': 22}
print("\nDiccionarios: ",diccionario)
print("Nombre: ", diccionario['nombre'])#imprime el valor de la clave nombre
print("Edad: ", diccionario['edad'])

#conjuntos
conjunto = {1, 2, 3, 4, 5}
print("\nConjunto: ",conjunto)

print("\nConversiones")
#convertir cadena a entero
numero = int("10")
print("\nConversión Int: ",numero)

#convertir cadena a flotante
numero = float("10.5")
print("Conversión Float: ",numero)

#convertir entero a cadena
numero = str(10)
print("Conversión Cadena Int: ",numero)

#convertir flotante a cadena
numero = str(10.5)
print("Conversión Cadena Float: ",numero)

#convertir entero a flotante
numero = float(10)
print("Conversión Int a Float: ",numero)

#convertir flotante a entero
numero = int(10.5)
print("Conversión Float a Int: ",numero)

#operaciones aritméticas
print("\nOperaciones aritméticas")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("\nSuma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

#operaciones relacionales
print("\nOperaciones relacionales")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("\n¿El primer número es mayor que el segundo?:", num1 > num2)
print("¿El primer número es menor que el segundo?:", num1 < num2)
print("¿El primer número es mayor o igual que el segundo?:", num1 >= num2)
print("¿El primer número es menor o igual que el segundo?:", num1 <= num2)
print("¿El primer número es igual que el segundo?:", num1 == num2)
print("¿El primer número es diferente que el segundo?:", num1 != num2)

#operaciones lógicas
print("\nOperaciones lógicas")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)
print("Not True:", not True)
print("Not False:", not False)

#operaciones de asignación
print("\nOperaciones de asignación")
num1 = 10
num1 += 5
print(num1)
num1 -= 5
print(num1)
num1 *= 5
print(num1)
num1 /= 5
print(num1)
num1 %= 5
print(num1)
num1 **= 5 #exponente
print(num1)
num1 //= 5 #división entera
print(num1)

#operadores de pertenencia
print("\nOperaciones de pertenencia")
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print(6 in lista)#imprime False
print(1 not in lista)#imprime False
print(6 not in lista)

print("\nOperación de validación")
aprobado = float(input("Ingresa tu calificación: ")) >= 70
print("¿Aprobaste?:", aprobado)

