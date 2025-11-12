contador = 0
cadena1 = str(input("Introduce la primera cadena: "))
cadena2 = str(input("Introduce la segunda cadena: "))

longitud = min(len(cadena1), len(cadena2))

for x in range(longitud):
    if cadena1[x] == cadena2[x]:
        contador += 1

print("Las cadenas", cadena1, "y", cadena2, "tienen", contador, "caracteres iguales en la misma posición.")