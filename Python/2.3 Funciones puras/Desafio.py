def cuadradosLista(arreglo):
    # Filtramos solo los enteros positivos (usando filter)
    num_positivos = filter(lambda x: x > 0 and x.is_integer(), arreglo)
    
    # Calcula los cuadrados (usando map)
    cuadrados = map(lambda x: x ** 2, num_positivos)
    
    # Convertimos el map object a lista y retornamos
    return list(cuadrados)


cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)  
