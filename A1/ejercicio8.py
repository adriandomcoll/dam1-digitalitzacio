nombre = int(input("¿Qué numero quieres contar hasta 0?: "))

for i in range(11):
    resultado = i - nombre
    if (resultado >= 0):
        print(resultado)
