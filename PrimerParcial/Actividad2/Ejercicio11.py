#Ejercicio 11. Ahorros

inv = float(input("¿Cuanto es la cantidad de inversión? "))
interes = 1.04

prim = round(inv * interes,2)
seg = round(prim * interes,2)
terc = round(seg * interes,2)

print("El primer año es de: " + str(prim))
print("El segundo año es de: " + str(seg))
print("El tercer año es de: " + str(terc))