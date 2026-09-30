c = float(input("Cantidad a invertir: "))#usamos float para que nos permita poner decimales, si ponemos int solo nos permite poner numeros enteros
i = float(input("Interés anual: "))
anos = int(input("Número de años: "))#usamos int porque el número de años si queda en un numero entero 

c = c * (1 + i / 100) ** anos

print("El capital obtenido es", round(c, 2), "€")