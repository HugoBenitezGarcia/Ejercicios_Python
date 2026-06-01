# Definición de constantes
PI = 3.14159
DENSIDAD_AGUA = 1000         # kg/m³
LIMITE_PESO_KG = 10000       # 10 toneladas es igual a 10000 kg

# 1- Solicitar datos al usuario
radio_metros = float(input("Introduce el radio del tanque: "))
altura_metros = float(input("Introduce la altura del tanque: "))

# 2- Cálculos
#fórmula del volumen: V = π * r² * h
volumen_cilindro = PI * (radio_metros ** 2) * altura_metros

#Masa = Volumen * Densidad
masa_agua = volumen_cilindro * DENSIDAD_AGUA

# Evaluamos la condición lógica, guarada True o False
supera_diez_toneladas = masa_agua > LIMITE_PESO_KG

# 3- Mostrar los resultados en pantalla
print(f"Volumen calculado: {volumen_cilindro} m³")
print(f"Masa estimada del agua: {masa_agua} kg")
print(f"La masa supera las 10 toneladas?: {supera_diez_toneladas}")