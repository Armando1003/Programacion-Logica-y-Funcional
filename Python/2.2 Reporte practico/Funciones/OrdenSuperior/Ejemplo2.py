# Crear una función que devuelve otra función
def crear_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

duplicar = crear_multiplicador(2)
print(f"El doble de 5 es: {duplicar(5)}")