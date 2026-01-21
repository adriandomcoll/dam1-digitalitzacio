
# ESTO ESTA MAL, ES OTRO EJERCICIO

from datetime import date


class Artista:
    def __init__(self, id: int, nom: str):
        self.id = id
        self.nom = nom
        self.albums = [] 

    def afegir_album(self, album):
        self.albums.append(album)


class Album:
    def __init__(self, id: int, titol: str, data_llançament: date, artista: Artista):
        self.id = id
        self.titol = titol
        self.data_llançament = data_llançament
        self.artista = artista     
        self.cancons = []           
        artista.afegir_album(self)

    def afegir_canco(self, canco):
        self.cancons.append(canco)


class Canco:
    def __init__(self, id: int, titol: str, durada: float, album: Album):
        self.id = id
        self.titol = titol
        self.durada = durada
        self.album = album
        album.afegir_canco(self)


# Creando los objetos
# Crear artista
artista = Artista(1, "Dub Inc")

# Crear álbum
album = Album(
    1,
    "Paradise",
    date(2008, 6, 1),
    artista
)

# Crear canciones
c1 = Canco(1, "Better Run", 4.5, album)
c2 = Canco(2, "Rude Boy", 3.8, album)

# Comprobaciones
print(artista.nom)
print(len(artista.albums))        # para ver la canço 1
print(album.titol)
print(len(album.cancons))         # para ver la canó 2
print(c1.album.titol)
