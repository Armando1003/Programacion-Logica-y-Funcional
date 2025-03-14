#fórmula para calcular la cadena de bits de un número entero 

print("Conversión decimal a binario con valores definidos")
def cadenaBits(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return cadenaBits(numero // 2) + str(numero % 2)

# Ejemplo de uso
print("El número binario de 20 es: ", cadenaBits(20))  # Salida: 10100



