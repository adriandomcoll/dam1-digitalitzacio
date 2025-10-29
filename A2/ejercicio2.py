contador=0
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
numero=int((input("Introduce un número:")))

for x in list_num:
    if x == numero:
        contador+=1

print("A la cadena",  list_num, "hay", contador, "numeros de", numero)