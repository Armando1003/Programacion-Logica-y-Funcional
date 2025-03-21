# Ordenar una lista de estudiantes por su nota
estudiantes = [("Alex", 85), ("Haziel", 90), ("Angel", 78), ("Armando", 92)]

# Ordenamos la lista de estudiantes por nota en orden descendente usando una función lambda
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1], reverse=True)

# Imprimimos la lista ordenada
print(f"Estudiantes ordenados por nota: {estudiantes_ordenados}")