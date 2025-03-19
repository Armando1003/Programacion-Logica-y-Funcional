def preparar_cafe_americano():
    return "Cafe americano☕"

def preparar_Cafe_olla():
    return "Cafe de olla☕" 

def ordenar_Cafe(funcion, numero_tazas):
    tazas_cafe=[funcion() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupoA = ordenar_Cafe(preparar_cafe_americano, 3)
cafe_grupoB = ordenar_Cafe(preparar_Cafe_olla, 5)

print(cafe_grupoA, cafe_grupoB)