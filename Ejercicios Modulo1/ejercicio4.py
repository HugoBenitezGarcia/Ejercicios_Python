# 1- Solicitar la fuerza al usuario
# Utilizamos float para la entrada de números decimales
fuerza_newtons = float(input("Introduce el valor de la fuerza en Newtons: "))

# 2- Solicitar el área al usuario
area_metros_cuadrados = float(input("Introduce el valor del área en metros cuadrados: "))

# 3- Calcular la presión
#fórmula: Presión = Fuerza / Área
presion_calculada = fuerza_newtons / area_metros_cuadrados

# 4- Mostrar el resultado
print(f"La presión resultante es de {presion_calculada} Pascales.")