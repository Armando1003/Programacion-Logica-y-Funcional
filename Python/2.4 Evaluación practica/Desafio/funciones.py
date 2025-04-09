from functools import reduce

NUM_ALUMNOS = 3 #numero de alumnos

#Lista de asignaturas disponibles
ASIGNATURAS = [ 
    "Programación Avanzada",
    "Bases de Datos", 
    "Inteligencia Artificial"
]

#Aspectos que se evaluarán en cada asignatura
ASPECTOS = [
    "Claridad del profesor",
    "Dificultad del contenido",
    "Utilidad práctica",
    "Calidad de materiales"
]

#Calcular promedio
def calcular_promedio(notas):
    """Calcula el promedio usando reduce"""
    return round(reduce(lambda x, y: x + y, notas) / len(notas), 1) if notas else 0

#Contar las mejores notas
def contar_excelentes(notas):
    """Cuenta notas >= 9 usando filter"""
    return len(list(filter(lambda x: x >= 9, notas)))

#Notas minimas y maximas
def obtener_min_max(notas):
    """Obtiene nota mínima y máxima usando reduce"""
    min_nota = reduce(lambda x, y: x if x < y else y, notas)
    max_nota = reduce(lambda x, y: x if x > y else y, notas)
    return min_nota, max_nota

#Total de puntos
def calcular_total_asignatura(datos_asignatura):
    """Calcula el total sumando todas las notas de todos los alumnos"""
    return reduce(lambda x, y: x + sum(y), datos_asignatura, 0)

#Procesar los aspectos
def procesar_resultados_aspecto(aspecto_notas):
    """Procesa los resultados para un aspecto"""
    aspecto, notas = aspecto_notas
    return {
        'aspecto': aspecto,
        'promedio': calcular_promedio(notas),
        'excelentes': contar_excelentes(notas),
        'min_max': obtener_min_max(notas),
        'notas': notas
    }

#Procesar los datos de asignatura
def procesar_asignatura(asignatura_datos):
    """Procesa los datos de una asignatura"""
    asignatura, datos_asignatura = asignatura_datos
    notas_por_aspecto = list(zip(*datos_asignatura))  # Transponer la matriz
    
    return (
        asignatura,
        {
            'resultados': list(map(
                procesar_resultados_aspecto,
                zip(ASPECTOS, notas_por_aspecto)
            )),
            'total_asignatura': calcular_total_asignatura(datos_asignatura)
        }
    )

#Procesar las encuestas
def procesar_encuestas(encuestas):
    """Procesa todas las encuestas sin bucles"""
    return dict(map(procesar_asignatura, encuestas.items()))