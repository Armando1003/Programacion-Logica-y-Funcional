#Verificar si un estudiante aprobó una materia
def aprobado(nota):
    return nota >= 70

nota_estudiante = 75
if aprobado(nota_estudiante):
    print("El estudiante de ISC aprobó la materia.")
else:
    print("El estudiante de ISC no aprobó la materia.")