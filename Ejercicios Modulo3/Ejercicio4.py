# 1- Almacenar las lecturas iniciales en una lista
lecturas_lista = [5, 5, 4.9, 5.1, 5, 4.9, 5.2, 5.1]
print("Lecturas originales:", lecturas_lista)
print("Total de lecturas originales:", len(lecturas_lista))

# 2- Convertir la lista en un conjunto
lecturas_unicas = set(lecturas_lista)

# 3- Mostrar los resultados
print("Resultados del Filtrado")
print("Valores únicos detectados:", lecturas_unicas)

# Calculamos la cantidad de valores distintos usando len()
cantidad_distintos = len(lecturas_unicas)
print("Cantidad de valores distintos:", cantidad_distintos)

# EXPLICACIÓN DEL CAMBIO DE TAMAÑO:
# Al convertir la lista en un conjunto mediante set(), Python elimina
# automáticamente cualquier valor duplicado. Esto sucede porque la
# estructura 'set' está diseñada, por definición matemática, para contener
# únicamente elementos únicos. Por eso, aunque entraron 8 elementos en la
# lista original, el conjunto final se reduce a solo 4 elementos distintos.