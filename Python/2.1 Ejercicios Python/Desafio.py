# Inicialización de los puntos para cada rama
redes = 0
bases_de_datos = 0
desarrollo_de_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_de_proyectos = 0

# Función para obtener una respuesta válida
def obtener_respuesta(pregunta, opciones):
    while True:
        print(pregunta)
        for i, opcion in enumerate(opciones, 1):
            print(f"  {i}) {opcion}")
        try:
            respuesta = int(input('Ingresa tu respuesta: '))
            if 1 <= respuesta <= len(opciones):
                return respuesta
            else:
                print(f"Respuesta fuera de rango, por favor ingresa un número entre 1 y {len(opciones)}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

print('===============')
print('El Desafio')
print('===============')

# ~~~~~~~~~~~~~~~ Pregunta 1 ~~~~~~~~~~~~~~~
pregunta_1 = "\nSi tuvieras que elegir un proyecto para especializarte, ¿cuál elegirías?"
opciones_1 = [
    "Desarrollar una aplicación que ayude a gestionar proyectos eficientemente.",  # Gestión de Proyectos
    "Diseñar e implementar una infraestructura de redes seguras.",  # Redes
    "Optimizar una base de datos para una empresa con millones de registros.",  # Bases de Datos
    "Crear modelos 3D para una película animada.",  # Modelado 3D
    "Programar un sistema embebido para un dispositivo IoT.",  # Programación Hardware
    "Desarrollar un software innovador para resolver problemas complejos."  # Desarrollo de Software
]
respuesta_1 = obtener_respuesta(pregunta_1, opciones_1)

if respuesta_1 == 1:
    gestion_de_proyectos += 2
elif respuesta_1 == 2:
    redes += 2
elif respuesta_1 == 3:
    bases_de_datos += 2
elif respuesta_1 == 4:
    modelado_3d += 2
elif respuesta_1 == 5:
    programacion_hardware += 2
elif respuesta_1 == 6:
    desarrollo_de_software += 2

# ~~~~~~~~~~~~~~~ Pregunta 2 ~~~~~~~~~~~~~~~
pregunta_2 = "\n¿Qué tipo de problema te gusta resolver?"
opciones_2 = [
    "Crear software para automatizar tareas y mejorar la productividad.",  # Desarrollo de Software
    "Asegurar que la información en bases de datos sea rápida y eficiente.",  # Bases de Datos
    "Coordinar equipos y asegurar la correcta ejecución de proyectos.",  # Gestión de Proyectos
    "Construir y optimizar dispositivos electrónicos.",  # Programación Hardware
    "Diseñar experiencias visuales en 3D para videojuegos.",  # Modelado 3D
    "Configurar y mantener sistemas de redes y servidores."  # Redes
]
respuesta_2 = obtener_respuesta(pregunta_2, opciones_2)

if respuesta_2 == 1:
    desarrollo_de_software += 2
elif respuesta_2 == 2:
    bases_de_datos += 2
elif respuesta_2 == 3:
    gestion_de_proyectos += 2
elif respuesta_2 == 4:
    programacion_hardware += 2
elif respuesta_2 == 5:
    modelado_3d += 2
elif respuesta_2 == 6:
    redes += 2

# ~~~~~~~~~~~~~~~ Pregunta 3 (NUEVA) ~~~~~~~~~~~~~~~
pregunta_3 = "\n¿Cuál de estas actividades disfrutas más?"
opciones_3 = [
    "Configurar routers, switches y asegurar la conectividad de una red.",  # Redes
    "Optimizar consultas SQL y asegurar la integridad de los datos.",  # Bases de Datos
    "Liderar un equipo de programadores en el desarrollo de un software.",  # Gestión de Proyectos
    "Diseñar hardware especializado para sistemas de control industrial.",  # Programación Hardware
    "Programar videojuegos y aplicaciones interactivas.",  # Desarrollo de Software
    "Crear modelos tridimensionales para efectos visuales en cine y TV."  # Modelado 3D
]
respuesta_3 = obtener_respuesta(pregunta_3, opciones_3)

if respuesta_3 == 1:
    redes += 2
elif respuesta_3 == 2:
    bases_de_datos += 2
elif respuesta_3 == 3:
    gestion_de_proyectos += 2
elif respuesta_3 == 4:
    programacion_hardware += 2
elif respuesta_3 == 5:
    desarrollo_de_software += 2
elif respuesta_3 == 6:
    modelado_3d += 2

# ~~~~~~~~~~~~~~~ Pregunta 4 (NUEVA) ~~~~~~~~~~~~~~~
pregunta_4 = "\nSi pudieras aprender una nueva habilidad, ¿cuál elegirías?"
opciones_4 = [
    "Aprender a programar microcontroladores y sistemas embebidos.",  # Programación Hardware
    "Perfeccionar mis habilidades en modelado 3D y animación digital.",  # Modelado 3D
    "Convertirme en un experto en seguridad de redes y ciberseguridad.",  # Redes
    "Aprender a diseñar bases de datos de alta disponibilidad.",  # Bases de Datos
    "Liderar proyectos complejos y aprender metodologías ágiles.",  # Gestión de Proyectos
    "Crear aplicaciones móviles y software escalable."  # Desarrollo de Software
]
respuesta_4 = obtener_respuesta(pregunta_4, opciones_4)

if respuesta_4 == 1:
    programacion_hardware += 2
elif respuesta_4 == 2:
    modelado_3d += 2
elif respuesta_4 == 3:
    redes += 2
elif respuesta_4 == 4:
    bases_de_datos += 2
elif respuesta_4 == 5:
    gestion_de_proyectos += 2
elif respuesta_4 == 6:
    desarrollo_de_software += 2

# ~~~~~~~~~~~~~~~ Resultados ~~~~~~~~~~~~~~~
print("\nResultados:")
print(f"Redes: {redes}")
print(f"Bases de Datos: {bases_de_datos}")
print(f"Desarrollo de Software: {desarrollo_de_software}")
print(f"Programación Hardware: {programacion_hardware}")
print(f"Modelado 3D: {modelado_3d}")
print(f"Gestión de Proyectos de Software: {gestion_de_proyectos}")

max_puntaje = max(redes, bases_de_datos, desarrollo_de_software, programacion_hardware, modelado_3d, gestion_de_proyectos)

print("\n¡Tu rama recomendada es:", end=" ")
if max_puntaje == redes:
    print("Redes!")
elif max_puntaje == bases_de_datos:
    print("Bases de Datos!")
elif max_puntaje == desarrollo_de_software:
    print("Desarrollo de Software!")
elif max_puntaje == programacion_hardware:
    print("Programación Hardware!")
elif max_puntaje == modelado_3d:
    print("Modelado 3D!")
else:
    print("Gestión de Proyectos de Software!")