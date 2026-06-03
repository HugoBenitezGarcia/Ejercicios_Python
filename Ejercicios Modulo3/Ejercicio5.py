datos_sensores = {}

# Definimos una lista auxiliar con los nombres de los sensores que vamos a evaluar
nombres_sensores = ["temperatura", "presion", "vibracion"]

print("------- 1. Adquisición de Datos -------")

# Bucle exterior: Recorre cada uno de los sensores
for sensor in nombres_sensores:
    print(f"Registrando lecturas para el sensor de: {sensor.upper()}")

    # Creamos una lista vacía para las mediciones de este sensor en particular
    mediciones_temporales = []
    for i in range(5):
        valor = float(input(f"Introduce la medición {i + 1}: "))
        mediciones_temporales.append(valor)

    # Una vez recogidas las 5 medidas, guardamos la lista en el diccionario
    datos_sensores[sensor] = mediciones_temporales

print("------- 2. Análisis y Resultados -------")

# Iteramos sobre el diccionario completo
# En cada vuelta, 'clave' recibe el nombre del sensor y 'lista_valores' sus 5 datos
for clave, lista_valores in datos_sensores.items():
    valor_max = max(lista_valores)
    valor_min = min(lista_valores)
    promedio = sum(lista_valores) / len(lista_valores)

    # Mostramos los resultados
    print(f"Resumen para el sensor de {clave.upper()}:")
    print(f"- Registro completo: {lista_valores}")
    print(f"- Valor Máximo: {valor_max}")
    print(f"- Valor Mínimo: {valor_min}")
    print(f"- Promedio calculado: {promedio}")