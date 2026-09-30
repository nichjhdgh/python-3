dinero = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: ")) #si ponemos float nos permite poner decimales, si ponemos int solo nos permite poner numeros enteros
interes = 0.04
primer_año = dinero + (dinero * interes)
segundo_año = primer_año + (primer_año * interes)
tercer_año = segundo_año + (segundo_año * interes)
print("Cantidad de ahorros tras el primer año: "  , primer_año) #redondeado a 2 decimales si queremos poner round(primer_año,2) para que nos muestre solo 2 decimales
print("Cantidad de ahorros tras el segundo año: " , segundo_año)
print("Cantidad de ahorros tras el tercer año: "  , tercer_año) 




