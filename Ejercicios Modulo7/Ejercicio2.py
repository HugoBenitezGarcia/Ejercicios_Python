import pandas as pd

print("----- 1- Creación y Visualización del DataFrame -----")
# Creamos un diccionario con la estructura de la tabla
datos_materiales = {
    "Material": ["Acero", "Aluminio", "Titanio", "Cobre"],
    "Densidad (kg/m3)": [7850, 2700, 4500, 8960],
    "Resistencia (MPa)": [250, 150, 900, 210]
}

# Convertimos el diccionario en un DataFrame
df_materiales = pd.DataFrame(datos_materiales)

# 1- Mostrar el DataFrame
print("Base de datos original:")
print(df_materiales)


print("\n----- 2. Cálculo Estadístico -----")
# 2- Calcular el promedio de densidad
# Seleccionamos la columna exacta y aplicamos .mean()
promedio_dens = df_materiales["Densidad (kg/m3)"].mean()
print(f"El promedio de densidad de los materiales es: {promedio_dens} kg/m³")


print("\n----- 3. Filtrado de Datos -----")
# 3- Filtrar los materiales con resistencia mayor a 200 MPa
# El DataFrame evalúa su propia columna y devuelve solo las filas que cumplen la condición
materiales_resistentes = df_materiales[df_materiales["Resistencia (MPa)"] > 200]
print("Materiales con resistencia superior a 200 MPa:")
print(materiales_resistentes)


print("\n----- 4. Ordenamiento de Datos -----")
# 4- Ordenar los materiales por resistencia descendente
materiales_ordenados = df_materiales.sort_values(by="Resistencia (MPa)", ascending=False)
print("Catálogo de materiales ordenado por resistencia:")
print(materiales_ordenados)