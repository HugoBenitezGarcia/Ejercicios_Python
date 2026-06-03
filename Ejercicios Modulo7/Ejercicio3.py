import pandas as pd

#2- Cargar el archivo utilizando pandas.read_csv()
# pandas lee el archivo y lo transforma automáticamente en un DataFrame
df_traccion = pd.read_csv("ensayo_traccion.csv")

# 3- Cálculos solicitados
# Promedio de una columna
promedio_esfuerzo = df_traccion["Esfuerzo_Maximo"].mean()
# Valor máximo de otra columna
maxima_deformacion = df_traccion["Deformacion"].max()

# 4- Mostrar las primeras 3 filas del archivo
print("----- Vista Previa de la Base de Datos -----")
# .head(3) recorta la tabla para mostrar solo el encabezado y las filas 0, 1 y 2
print(df_traccion.head(3))

# 5- Indicar cuántas muestras tienen esfuerzo mayor a 300 MPa
# Reutilizamos el potente filtro booleano que aprendimos en el Ejercicio 1
muestras_criticas = (df_traccion["Esfuerzo_Maximo"] > 300).sum()

print("\n----- Resultados del Análisis -----")
print(f"Promedio del Esfuerzo Máximo: {promedio_esfuerzo:.2f} MPa")
print(f"Deformación máxima registrada: {maxima_deformacion}")
print(f"Total de muestras que superan los 300 MPa: {muestras_criticas}")