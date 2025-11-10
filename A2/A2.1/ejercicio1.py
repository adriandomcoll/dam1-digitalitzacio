lista_numeros = [[1], 2, 3, 4, 5]
lista_numeros[0].append(10) 

print(lista_numeros)

lista_compra = ["pomes", "pa", "oli", "llet"]
lista_compra[2] = ""
print(lista_compra[0])
print(lista_compra[3])

cont=0
while cont < len(lista_compra):
    print("He de comprar "+lista_compra[cont])
    cont+=1

print("Elementos lista números:", len(lista_numeros), "   Elementos lista compra:", len(lista_compra))