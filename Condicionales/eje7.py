renta = float(input("cual es tu renta anual : "))
if renta < 10000 :
    print ("tu tiipo de impositivo es 5%")
elif renta >= 10000 and renta <= 20000 :
    print ("tu tiipo de impositivo es 15%")
elif renta >= 20000 and renta <= 35000 :
    print ("tu tiipo de impositivo es 20%")
elif renta >= 35000 and renta <= 60000 :
    print ("tu tiipo de impositivo es 30%")
elif renta > 60000 :
    print ("tu tiipo de impositivo es 45%")
else :
    print("datos mal intrucucidos. ")