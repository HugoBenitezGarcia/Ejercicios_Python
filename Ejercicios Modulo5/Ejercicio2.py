# 1 y 2- Leer el archivo y almacenar los valores en una lista
lista_voltajes = []

print("----- Procesamiento de Archivo de Voltajes -----")

# Abrimos el archivo en modo lectura
with open("voltajes.txt", "r") as archivo:
    # .read() extrae el contenido del archivo como un único bloque de texto
    contenido = archivo.read()

    # .split() divide ese bloque de texto en una lista de palabras/números, separando automáticamente por espacios o saltos de línea
    valores_texto = contenido.split()

    # Recorremos cada trozo de texto, lo convertimos a número y lo guardamos
    for valor in valores_texto:
        numero_decimal = float(valor)
        lista_voltajes.append(numero_decimal)

# 3- Calcular máximo, mínimo y promedio
# Como ya tenemos una lista de floats puros, usamos las funciones nativas
voltaje_maximo = max(lista_voltajes)
voltaje_minimo = min(lista_voltajes)
promedio = sum(lista_voltajes) / len(lista_voltajes)

# 4- Mostrar los resultados en pantalla
print("----- Resultados del Análisis -----")
print(f"Total de mediciones procesadas: {len(lista_voltajes)}")
print(f"Voltaje Máximo: {voltaje_maximo} V")
print(f"Voltaje Mínimo: {voltaje_minimo} V")
print(f"Voltaje Promedio: {promedio} V")