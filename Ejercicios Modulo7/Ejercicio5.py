import pandas as pd

print("----- Sistema Analítico de Ensayos de Materiales -----\n")

# 1- Cargar el archivo de la base de datos
df_ensayos = pd.read_csv("ensayos_materiales.csv")

carga_aplicada = df_ensayos["Carga_Aplicada"]
area = df_ensayos["Area"]

esfuerzo_calculado = carga_aplicada / area

# Finalmente, inyectamos el resultado de vuelta en la tabla
df_ensayos["Esfuerzo"] = esfuerzo_calculado


# 3- Cálculos agrupados por Material
esfuerzo_promedio = df_ensayos.groupby("Material")["Esfuerzo"].mean()

es_falla = df_ensayos["Falla"] == "Sí"
porcentaje_fallas = df_ensayos.groupby("Material")[es_falla].mean() * 100

# 4- Generar un resumen final unificando los cálculos
df_resumen = pd.DataFrame({
    "Esfuerzo Promedio (MPa)": esfuerzo_promedio,
    "Porcentaje de Falla (%)": porcentaje_fallas
})

# Ordenamos de mayor a menor porcentaje de falla
df_resumen_ordenado = df_resumen.sort_values(by="Porcentaje de Falla (%)", ascending=False)

print("----- REPORTE FINAL DE CRITICIDAD -----")
print(df_resumen_ordenado)

# Extraemos el nombre del material más crítico
material_critico = df_resumen_ordenado.index[0]
peor_porcentaje = df_resumen_ordenado.iloc[0]["Porcentaje de Falla (%)"]

print("\n----- CONCLUSIÓN TÉCNICA -----")
print(f"El material más crítico es el '{material_critico}', presentando un {peor_porcentaje:.1f}% de tasa de falla en los ensayos.")