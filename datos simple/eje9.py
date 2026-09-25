c = float(input("Cantidad a invertir: "))
i = float(input("Interés anual: "))
anos = int(input("Número de años: "))

c = c * (1 + i / 100) ** anos

print("El capital obtenido es", round(c, 2), "€")