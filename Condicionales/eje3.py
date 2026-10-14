#Escribir un programa que pida al usuario dos números y muestre por pantalla su 
#división. Si el divisor es cero el programa debe mostrar un error.
n1 = float(input("dime un numero: "))
n2 = float(input("dime otro numero: "))
if n2 > 0 :
    print (n1/n2)
else : 
   print ("error error ")