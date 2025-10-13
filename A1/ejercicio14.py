paraula = input("Escriu una paraula: ")
inversa = ""

for lletra in paraula:
    inversa = lletra + inversa   # vas construint la cadena al revés

print("La paraula invertida és:", inversa)