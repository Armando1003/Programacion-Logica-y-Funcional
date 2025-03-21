# Notificar al estudiante después de calcular el promedio
def calcular_promedio(notas, callback):
    promedio = sum(notas) / len(notas)
    callback(promedio)


def notificar(promedio):
    print(f"El promedio calculado es: {promedio}")

# Lista de notas
notas = [85, 90, 78, 92, 98]

# Calcula el promedio y notifica usando 'calcular_promedio' y 'notificar'
calcular_promedio(notas, notificar)