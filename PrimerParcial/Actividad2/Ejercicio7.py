#Ejercicio 7. IMC

peso = float(input("¿Cuál es tu peso (Kg)? "))
estatura = float(input("¿Cuál es tu estatura (Metros)? "))
imc = peso / (estatura**2)
print("Tu índice de masa corporal es " + str(imc))