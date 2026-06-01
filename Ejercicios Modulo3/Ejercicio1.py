# Inicializamos una lista vacía para almacenar mediciones
mediciones = []

# 1- Solicitar las 8 mediciones al usuario
# Usamos un bucle for que se repetirá 8 veces
for i in range(8):
    # Pedimos la temperatura, la convertimos a float y la guardamos temporalmente
    temp_actual = float(input(f"Introduce la medición {i + 1} en °C: "))

    # Añadimos el valor al final de nuestra lista
    mediciones.append(temp_actual)

# 2- Cálculos estadísticos sobre la lista
temp_maxima = max(mediciones)
temp_minima = min(mediciones)

#Sumamos todos los elementos y dividimos por la cantidad total
temp_promedio = sum(mediciones) / len(mediciones)

# 3- Mostrar los resultados
print(f"Las temperaturas registradas son: {mediciones}")
print(f"Temperatura MÁXIMA: {temp_maxima} °C")
print(f"Temperatura MÍNIMA: {temp_minima} °C")
print(f"Temperatura PROMEDIO: {temp_promedio} °C")