contador=0
palabra= str (input("Introduce una palabra para contar una letra específica: "))
letra=str (input("Introduce una letra: "))

for x in palabra:
    if x == letra:
        contador+=1

print("A la palabra",  palabra, "hay", contador, "letras de", letra)