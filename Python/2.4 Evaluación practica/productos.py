productos = ["Frijoles Refritos", 
             "Coca Cola", 
             "Zumo de Naranja", 
             "Cafe de Olla", 
             "Gorditas de Chicharron", 
             "Huevos Motuleños"
             ]

print("Gestion de productos")

orden_productos = sorted(productos)
cadena_ordenada = ", ".join(orden_productos)

slugs = list(map(lambda x: x.lower().replace(" ", "-"), orden_productos))

print(" -Lista de slugs:", slugs)
print(" -Cadena ordenada:", cadena_ordenada)