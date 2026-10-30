tipodepizza = input("quires una piza vegetariana si o no :")
if tipodepizza == "si" :
    v =input(" los Ingredientes vegetarianos son :Pimiento y tofu puedes elgir uno ingrediente na mas : ")
    print("la piza q has eligido es vegetariana y tiene de ingredientes mozzarella y tomate "+ v)
elif tipodepizza == "no" :
    nv = input(" los Ingredientes no vegetarianos son: Peperoni y jamon y salmon puedes elgir uno ingrediente na mas  : ")
    print("la piza q has eligido es vegetariana y tiene de ingredientes mozzarella y tomate "+ nv)
else :
    print("si contesta con si o no ")