capital_pais = {"Espanya": "Madrid","França": "París","Itàlia": "Roma"}

paisBuscar = input("Introdueix un país: ")

if paisBuscar in capital_pais:
    print(f"La capital de {paisBuscar} és {capital_pais[paisBuscar]}.")
else:
    print(f"{paisBuscar} no es troba al diccionari.")