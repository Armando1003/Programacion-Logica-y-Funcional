# Ejecutar una acción después de verificar la asistencia
def verificar_asistencia(asistencia, callback):
    if asistencia >= 80:
        callback("Asistencia aprobada")
    else:
        callback("Asistencia insuficiente")

# Definimos una función que muestra un mensaje
def mostrar_mensaje(mensaje):
    print(mensaje)

# Verifica la asistencia y se muestra el mensaje correspondiente
verificar_asistencia(85, mostrar_mensaje)