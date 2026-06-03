# 1- Leer datos del archivo
lista_presiones = []

with open("datos_laboratorio.txt", "r") as archivo_entrada:
    # Leemos y separamos los datos
    valores_texto = archivo_entrada.read().split()

    # Convertimos los textos a números decimales
    for valor_str in valores_texto:
        lista_presiones.append(float(valor_str))

print(f"Datos cargados correctamente: {len(lista_presiones)} mediciones encontradas.")

# 2- Calcular el Promedio y los límites del ±10%
promedio = sum(lista_presiones) / len(lista_presiones)

# Calculamos dónde están las líneas rojas de peligro (10% arriba y 10% abajo)
limite_superior = promedio * 1.10
limite_inferior = promedio * 0.90

# Bandera lógica para saber si hubo alguna alerta
alerta_tolerancia = False

# 3- Generar el archivo reporte.txt
print("Analizando desviaciones y generando 'reporte.txt'...")

with open("reporte.txt", "w") as archivo_salida:
    # Encabezado principal del reporte
    archivo_salida.write("=========================================\n")
    archivo_salida.write("   REPORTE DE PRESIONES DE LABORATORIO   \n")
    archivo_salida.write("=========================================\n\n")

    # Promedio general con 2 decimales
    archivo_salida.write(f"PROMEDIO GENERAL: {promedio:.2f} kPa\n")
    archivo_salida.write(f"Límites de tolerancia : [{limite_inferior:.2f} a {limite_superior:.2f} kPa]\n\n")

    # Encabezados de la tabla
    archivo_salida.write("Medición (kPa)\tDesviación (kPa)\tEstado\n")
    archivo_salida.write("-" * 55 + "\n")

    # Bucle de análisis individual
    for presion in lista_presiones:
        # Calculamos la desviación (puede dar positivo o negativo)
        desviacion = presion - promedio
        estado = "OK"

        # Evaluamos si supera el ±10%
        if presion > limite_superior or presion < limite_inferior:
            estado = "FUERA DE LÍMITE"
            alerta_tolerancia = True

        # Escribimos la fila en la tabla del archivo
        # Usamos :+.2f en la desviación para que siempre muestre el signo
        archivo_salida.write(f"{presion:.2f}\t\t{desviacion:+.2f}\t\t\t{estado}\n")

    # Resumen final al pie del documento
    archivo_salida.write("\n=========================================\n")
    archivo_salida.write("CONCLUSIÓN DEL ANÁLISIS:\n")

    if alerta_tolerancia:
        archivo_salida.write(">> SÍ se detectaron mediciones que superan el ±10% del promedio.\n")
    else:
        archivo_salida.write(">> NO se detectaron mediciones que superen el ±10% del promedio. Sistema estable.\n")

print("Puedes revisar los resultados en 'reporte.txt'.")