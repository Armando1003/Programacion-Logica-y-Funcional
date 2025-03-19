def pizza():
    return "🍕"

def hamburguesa():
    return "🍔"

def hotdog():
    return "🌭"

def ordenar_alimento(preparar_alimento,num_porciones):
    porcion_alimento = [preparar_alimento() for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)
    return porcion_alimento, bonus

def calcular_bonus(porciones):
    if porciones > 2:
        return "COCA GRATIS 🥤"    
    else:
        return "😞"

porcion_pizza = ordenar_alimento(pizza, 7)
porcion_hamburguesa = ordenar_alimento(hamburguesa, 4)
porcion_hotdog = ordenar_alimento(hotdog, 1)

print(porcion_pizza)
print(porcion_hamburguesa)
print(porcion_hotdog)