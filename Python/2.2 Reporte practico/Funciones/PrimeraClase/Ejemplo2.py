# Pasar una función como argumento
def aplicar_funcion(func, valor):
    return func(valor)

def duplicar(x):
    return x * 2

resultado = aplicar_funcion(duplicar, 5)
print(f"El resultado de duplicar 5 es: {resultado}")