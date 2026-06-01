# 1- Solicitar al usuario la temperatura medida
# Usamos el float porque la temperatura se suele poner con decimales
temperatura = float(input("Introduce la temperatura actual del sensor en °C: "))

# 2 y 3- Determinar rango seguro y guardar en variable booleana
# La variable alamcena True si se cumplen ambas condiciones o False si falla alguna
rango_seguro = temperatura >= 20 and temperatura <= 80

# 4- Mostrar mensaje indicando el estado del sistema
if rango_seguro:
    # Este print se ejecuta solo si rango_seguro es True
    print("El sistema está funcionando CORRECTAMENTE (rango seguro).")
else:
    # Este print se ejecuta si rango_seguro es False
    print("ALERTA, El sistema está FUERA DEL RANGO SEGURO.")