from functools import reduce

ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000] #lista de ventas a pesos mexicanos
peso_dolar = 20.45

print("Analisis de ventas")

promedio = reduce(lambda x, y: x + y, ventas) /len(ventas) #Obtener promedio
print(f"  -Promedio de ventas: ${promedio:.2f}")

ventas_dolar = list(map(lambda x: round(x / peso_dolar, 2), ventas)) #Convertir a dolares
print(f"  -Ventas en dólares: {ventas_dolar}")

ventas_150 = list(filter(lambda x: x > 150,ventas_dolar)) #Filtrar ventas de mas de 150 dolares
print(f"  -Ventas mayores a 150USD: {ventas_150}")

suma_ventas150 = reduce(lambda x, y: x + y, ventas_150)
print(f"  -Suma de ventas de más de 150USD: ${suma_ventas150:.2f}")