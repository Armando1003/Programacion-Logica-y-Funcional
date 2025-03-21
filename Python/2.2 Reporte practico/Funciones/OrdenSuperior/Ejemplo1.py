#Filtrar notas aprobatorias
def filtrar_aprobados(notas, condicion):
    return [nota for nota in notas if condicion(nota)]

def es_aprobado(nota):
    return nota >= 70

notas = [65, 80, 72, 68, 90]
aprobados = filtrar_aprobados(notas, es_aprobado)
print(f"Notas aprobatorias: {aprobados}")