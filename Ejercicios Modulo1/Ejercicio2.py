# 1- Solicitar masa y velocidad al usuario convirtiendolos a float
masa = float(input("Introduce la masa del cuerpo en kg: "))
velocidad = float(input("Introduce la velocidad del cuerpo en m/s: "))

# 2- Calcular la energía cinética
# Fórmula: Ec = 1/2 * m * v^2
# Traducción a Python: 0.5 * masa * velocidad al cuadrado
energia_cinetica = 0.5 * masa * (velocidad ** 2)

# 3- Mostrar el resultado con un mensaje descriptivo
print(f"La energía cinética del cuerpo es de {energia_cinetica} Julios.")