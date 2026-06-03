import pandas as pd

print("----- Proceso de Limpieza de Datos Térmicos -----")

# 1- Cargar el archivo original
df_temperaturas = pd.read_csv("temperaturas_experimento.csv")

# Guardamos el recuento de filas iniciales para la estadística final
total_inicial = len(df_temperaturas)

# 2- Eliminar los valores vacíos
# Creamos una versión "limpia" del DataFrame sin las filas defectuosas
df_sin_vacios = df_temperaturas.dropna()

# 3- Filtrar los valores fuera del rango razonable
# Usamos & para exigir que se cumplan ambas condiciones obligatoriamente
df_final = df_sin_vacios[(df_sin_vacios["Temperatura"] >= 0) & (df_sin_vacios["Temperatura"] <= 500)]

# 4- Calcular el promedio final sobre los datos ya limpios
promedio_real = df_final["Temperatura"].mean()

# 5- Calcular cuántos datos fueron eliminados
total_final = len(df_final)
datos_eliminados = total_inicial - total_final

# Mostrar los resultados del reporte
print("\n----- Reporte de Calidad del Sensor -----")
print(f"Mediciones iniciales capturadas: {total_inicial}")
print(f"Mediciones válidas procesadas: {total_final}")
print(f"Registros corruptos eliminados: {datos_eliminados}")
print("-" * 40)
print(f"Temperatura PROMEDIO REAL: {promedio_real:.2f} °C")