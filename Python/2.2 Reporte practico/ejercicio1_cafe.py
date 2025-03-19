
def preparar_Cafe():
    return "Cafe"

def ordenar_Cafe(numero_tazas):
    tazas_cafe=[preparar_Cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupoB = ordenar_Cafe(10)

print(cafe_para_grupoB)


#print(preparar_Cafe())

