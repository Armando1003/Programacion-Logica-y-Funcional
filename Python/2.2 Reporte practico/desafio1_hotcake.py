
def hotcake():
    return "🥞"

def preparar_hotcake(numero_piezas):
    piezas_hotcakes = [hotcake() for _ in range(numero_piezas)]
    return piezas_hotcakes

num_hotcakes =int(input("¿Cuantos hotcakes quieres? "))

hotcakes_familia = preparar_hotcake(num_hotcakes)

print(hotcakes_familia)


#print(hotcake())