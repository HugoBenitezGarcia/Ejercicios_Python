# Importamos la librería pandas con su alias estándar
import pandas as pd

# 1- Crear una Series con las resistencias
resistencias = pd.Series([245, 260, 250, 270, 255, 248, 265])

# 2- Cálculos estadísticos directos
promedio = resistencias.mean()
valor_maximo = resistencias.max()
valor_minimo = resistencias.min()
desviacion_estandar = resistencias.std()

# 3- Determinar cuántas mediciones superan los 255 MPa
superan_255 = (resistencias > 255).sum()

# 4- Mostrar los resultados de forma clara
print("----- Análisis de Resistencias -----")
print("Datos registrados:\n", resistencias, "\n")
print(f"Promedio: {promedio:.2f} MPa")
print(f"Valor Máximo: {valor_maximo} MPa")
print(f"Valor Mínimo: {valor_minimo} MPa")
print(f"Desviación Estándar: {desviacion_estandar:.2f} MPa")
print(f"Mediciones superiores a 255 MPa: {superan_255}")