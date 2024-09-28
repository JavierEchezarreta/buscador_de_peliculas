class Pelicula:
    def __init__(self, poster, titulo, sinopsis, actores, puntacion, genero, duracion):
        self.poster = poster
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.actores = actores
        self.puntacion = puntacion
        self.genero = genero
        self.duracion = duracion

class BuscadorPeliculas:
    def __init__(self):
        self.catalogo = []

