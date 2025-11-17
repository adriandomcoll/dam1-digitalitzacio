list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
ordenada = []

while list_num:
    minimo = min(list_num)
    ordenada.append(minimo)
    list_num.remove(minimo)

print(ordenada)


#Metodo selection_sort
def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print(selection_sort(list_num))


#Metodo insertion_sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = actual
    
    return lista

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print(insertion_sort(list_num))
