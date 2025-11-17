list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
numero_buscar = int(input("Introduce un número: "))

encontrado = False

for num in list_num:
    if num == numero_buscar:
        encontrado = True
        break 

if encontrado:
    print("El número", (numero_buscar), "sí está en la lista.")
else:
    print("El número", (numero_buscar), "no está en la lista.")
