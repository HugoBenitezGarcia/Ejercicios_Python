print("----- Generador de Reportes: Ley de Ohm -----")

# 1- Solicitar el valor de la resistencia
resistencia = float(input("Introduce el valor de la resistencia en Ohmios: "))

print("----- Procesando los cálculos y generando el archivo -----")

# 2 y 3- Generar la tabla y guardarla en el archivo
with open("tabla_ohm.txt", "w") as archivo:
    # Escribimos los encabezados descriptivos separados por tabulador
    archivo.write("Corriente (A)\tVoltaje (V)\n")
    archivo.write("-" * 30 + "\n")

    for corriente in range(11):
        # Aplicamos la fórmula física
        voltaje = corriente * resistencia

        # Escribimos cada fila separando con \t.
        archivo.write(f"{corriente}\t\t{voltaje:.2f}\n")

print("El archivo 'tabla_ohm.txt' se ha guardado correctamente.")