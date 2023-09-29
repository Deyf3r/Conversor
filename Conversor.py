grados = input ("Ingrese la temperatura a convertir:  ")
temp = input ("¿Es Fahrenheit(F) o Celsius(C)?  ")

grados = int(grados)

C = (grados * 9 / 5) + 32
F = (grados - 32) * 5 / 9

if temp == "F" :
    print (C)
elif temp == "C":
    print (F)
else:
    print ("Escala Invalida")
