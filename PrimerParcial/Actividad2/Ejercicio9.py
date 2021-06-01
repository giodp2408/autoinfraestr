#Ejercicio 9. Inversión

inv = float(input("¿Cuanto es la cantidad a invertir? "))
ianual = float(input("¿Cuanto es el interés porcentual anual? "))
nanos = float(input("¿Cuantos años serán? "))

res = round(inv * (ianual/100+1)**nanos, 2)
print("La ganancia es: " + str(res))