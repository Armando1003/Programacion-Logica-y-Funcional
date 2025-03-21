# Filtrar estudiantes que tienen más de 80 puntos
estudiantes = [("Alex", 85), ("Haziel", 90), ("Angel", 78), ("Armando", 92)]

# Filtramos los estudiantes que tienen más de 80 puntos usando una función lambda
estudiantes_filtrados = list(filter(lambda x: x[1] > 80, estudiantes))

# Imprimimos la lista filtrada
print(f"Estudiantes con más de 80 puntos: {estudiantes_filtrados}")