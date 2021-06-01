#Ejercicio 8. Dos numeros

n = input("Teclea el primer numero (n): ")
m = input("Teclea el segundo numero (m): ")

coc = str(int(n) // int(m))
res = str(int(n) % int(m))

print(n + " entre " +  m + " da un cociente " + coc + " y un resto " + res)