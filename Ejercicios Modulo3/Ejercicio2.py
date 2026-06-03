# 1- Solicitar las tres coordenadas al usuario
x = float(input("Introduce la coordenada X: "))
y = float(input("Introduce la coordenada Y: "))
z = float(input("Introduce la coordenada Z: "))

# 2- Almacenarlas en una tupla
punto_espacial = (x, y, z)

# 3- Calcular la distancia al origen
# Elevamos cada componente al cuadrado, las sumamos, y elevamos
distancia_origen = (x**2 + y**2 + z**2) ** 0.5

# 4- Mostrar los resultados
print(f"Coordenadas registradas: {punto_espacial}")
print(f"Distancia al origen: {distancia_origen} unidades")