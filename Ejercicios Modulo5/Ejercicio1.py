# librería básica para fechas y horas
import datetime

print("----- Sistema de Registro de Laboratorio -----")

# 1- Solicitar los datos al usuario
nombre_experimento = input("Introduce el nombre del experimento: ")
valor_medido = input("Introduce el valor medido: ")
unidad_medida = input("Introduce la unidad de medida: ")

# Capturamos la fecha y hora exacta del sistema
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2- Generar el archivo resultados.txt
# Usamos el modo 'w' para crear el archivo desde cero o sobrescribirlo
with open("resultados.txt", "w") as archivo:
    # 3- Escribir los datos en el archivo
    # Usamos f-strings e incluimos \n al final para el salto de línea
    archivo.write(f"Nombre del experimento: {nombre_experimento}\n")
    archivo.write(f"Valor registrado: {valor_medido} {unidad_medida}\n")
    archivo.write(f"Fecha y hora del registro: {fecha_actual}\n")

print("\n Los datos se han guardado en 'resultados.txt'.")