# Inicializamos un diccionario vacío
catalogo_materiales = {}

# Usamos un bucle para pedir los datos de 3 materiales
for i in range(3):
    print(f"Ingresando datos del material {i + 1}:")
    nombre = input("Nombre del material: ")
    densidad = float(input("Densidad (kg/m³): "))
    resistencia = float(input("Resistencia máxima (MPa): "))

    # Guardamos la información en el diccionario
    catalogo_materiales[nombre] = {
        "densidad": densidad,
        "resistencia": resistencia
    }

# 2- Mostrar todos los materiales registrados
print("2. Base de Datos Completa")
# Imprimimos el diccionario tal cual para ver su estructura interna
print(catalogo_materiales)

# 3- Consultar un material específico
print("3 y 4. Búsqueda y Evaluación")
busqueda = input("Introduce el nombre del material que deseas consultar: ")

# Buscamos si el material existe en las claves del diccionario
if busqueda in catalogo_materiales:
    # Si existe, extraemos su diccionario de propiedades
    propiedades = catalogo_materiales[busqueda]

    print(f"Resultados de: {busqueda}")
    print(f"Densidad: {propiedades['densidad']} kg/m³")
    print(f"Resistencia: {propiedades['resistencia']} MPa")

    # 4- Indicar si tiene una resistencia mayor a 250 MPa
    supera_resistencia = propiedades['resistencia'] > 250
    print(f"Resistencia superior a 250 MPa?: {supera_resistencia}")

else:
    # Si el usuario busca un material que no está registrado
    print(f"Error: El material '{busqueda}' no se encuentra en el catálogo.")