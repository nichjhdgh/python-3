#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.
precio = 3.49
descuento = 0.6 
barras = int(input("Número de barras vendidas que no son del día: "))
precio_total = barras * precio 
precio_descuento = precio_total * descuento
precio_final = precio_total - precio_descuento

print("Precio habitual de una barra de pan:", precio, "€")
print("Descuento por no ser fresca:", precio_descuento, "€")
print("Coste final total:", precio_final, "€") 
