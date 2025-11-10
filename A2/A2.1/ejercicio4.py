list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

mayor = list_num[0]
menor = list_num[0]

for num in list_num:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print("El número más grande es:", mayor)
print("El número más pequeño es:", menor)