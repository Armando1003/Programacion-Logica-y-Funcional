# Retornar una función desde otra función
def crear_mensaje():
    def mensaje():
        return "¡Éxito en tu semestre!"
    return mensaje

mensaje_estudiante = crear_mensaje()
print(mensaje_estudiante())  # Se ejecuta la función retornada
