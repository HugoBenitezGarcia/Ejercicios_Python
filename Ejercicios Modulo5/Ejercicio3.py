# Inicializamos una lista para guardar temporalmente las temperaturas problemáticas
temperaturas_alerta = []

print("----- Sistema de Filtrado de Temperaturas -----")

# 1- Leer el archivo de origen
with open("temperaturas.txt", "r") as archivo_entrada:
    contenido = archivo_entrada.read()
    valores_texto = contenido.split()

# 2- Identificar las temperaturas fuera del rango seguro
for valor_str in valores_texto:
    temperatura = float(valor_str)

    # Condición de fuera de rango: menor a 20 O mayor a 80
    if temperatura < 20 or temperatura > 80:
        temperaturas_alerta.append(temperatura)

print("----- Generando reporte de alertas -----")

# 3- Crear el archivo alertas.txt y escribir los valores
with open("alertas.txt", "w") as archivo_salida:
    # Recorremos nuestra lista de alertas para escribirlas una a una
    for alerta in temperaturas_alerta:
        # Añadimos \n para que en el archivo de texto sí queden una por línea
        archivo_salida.write(f"{alerta}\n")

# 4- Indicar cuántas alertas se detectaron
cantidad_alertas = len(temperaturas_alerta)

print("\n--- Resumen de la Operación ---")
if cantidad_alertas > 0:
    print(f" Se han detectado y guardado {cantidad_alertas} alertas en 'alertas.txt'.")
else:
    print(" No se detectaron temperaturas fuera de rango.")