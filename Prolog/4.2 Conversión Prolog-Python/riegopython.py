# Hechos (estado de sensores)
humedad_suelo = "baja"
temperatura = 35
hora = 20
pronostico_lluvia = False

# Regla: Hora adecuada para regar
def hora_adecuada(h):
    return h < 10 or h > 18

# Regla: Activar riego
def activar_riego(humedad, lluvia, h):
    return humedad == "baja" and not lluvia and hora_adecuada(h)

# Diagnóstico del riego
def estado_riego(humedad, lluvia, h):
    return "Activado" if activar_riego(humedad, lluvia, h) else "No activado"

# Alerta por temperatura
def alerta_calor(temp):
    return temp >= 32

# Recomendación del sistema
def recomendacion(humedad, lluvia, h, temp):
    if activar_riego(humedad, lluvia, h) and alerta_calor(temp):
        return "Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo."
    else:
        return "Sin recomendaciones especiales para el riego."

# Ejecución del diagnóstico
def diagnostico():
    estado = estado_riego(humedad_suelo, pronostico_lluvia, hora)
    alerta = alerta_calor(temperatura)
    recomend = recomendacion(humedad_suelo, pronostico_lluvia, hora, temperatura)

    print(f"Estado del sistema de riego: {estado}")
    if estado == "Activado":
        print("✔️ El riego está activado.")
    else:
        print("❌ El riego no está activado.")
    if alerta:
        print("⚠️ Alerta: Condiciones de calor extremo.")
    print(f"🔎 Recomendación del sistema: {recomend}")

# Ejecutar
diagnostico()
