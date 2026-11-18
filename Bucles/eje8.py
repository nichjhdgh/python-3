numero = int(input("Ingrese un número: ")) 

for i in range(1, numero + 1):
    for j in range(i, 0, -1):
        print(2 * j - 1, end=" ")
    print()
