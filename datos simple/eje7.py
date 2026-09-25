piso = float(input("Introduce tu peso en kg: "))
e = float(input("Introduce tu estatura en metros: "))

imc = piso / (e ** 2)

print("Tu índice de masa corporal es", round(imc, 2))
