numero=input("Pon número ")

if(numero.isnumeric()):
    reste = int(numero) % 2
    print ("Es par.")
    if reste == 0:
        print ("Es inpar.")
else:
    print ("No era un número")