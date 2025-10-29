numero1= int(input("Di un número: "))
numero2= int(input("Di un número: "))
numero3= int(input("Di un número: "))

if numero1 > numero2 and numero1 > numero3:
    print(numero1, "es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(numero2, "es el mayor")
else:
    print(numero3, "es el mayor")