import json

class Pelicula:
    def __init__(self, poster, titulo, sinopsis, actores, puntuacion, genero, duracion):
        self.__poster = poster
        self.__titulo = titulo
        self.__sinopsis = sinopsis
        self.__actores = actores
        self.__puntacion = puntuacion
        self.__genero = genero
        self.__duracion = duracion

    def titulo(self):
        return self.__titulo

    def genero(self):
        return self.__genero

    def actores(self):
        return self.__actores

class BuscadorPeliculas:
    def __init__(self):
        self.__catalogo = []

    def agregar_pelicula(self, poster, titulo, sinopsis, actores, puntuacion, genero, duracion):
        self.__catalogo.append(Pelicula(poster, titulo, sinopsis, actores, puntuacion, genero, duracion))

    def cantidad_peliculas(self):
        return len(self.__catalogo)

    def importar_peliculas(self, archivo):
        try:
            with open(archivo, 'r') as archivo_json:
                datos = json.load(archivo_json)
                for pelicula in datos:
                    poster = pelicula['poster']
                    titulo = pelicula['titulo']
                    sinopsis = pelicula['sinopsis']
                    actores = pelicula['actores']
                    puntuacion = pelicula['puntuacion']
                    genero = pelicula['genero']
                    duracion = pelicula['duracion']
                    self.agregar_pelicula(poster, titulo, sinopsis, actores, puntuacion, genero, duracion)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al importar el archivo: {e}")

    def buscar_pelicula_por_titulo(self, titulo):
        for pelicula in self.__catalogo:
            if pelicula.titulo() == titulo:
                return pelicula

    def buscar_pelicula_por_genero(self, genero):
        for pelicula in self.__catalogo:
            if pelicula.genero() == genero:
                return pelicula

    def buscar_peliculas_comunes_por_actores(self, actor1, actor2):
        peliculas = []
        for pelicula in self.__catalogo:
            if actor1 in pelicula.actores() and actor2 in pelicula.actores():
                peliculas.append(pelicula.titulo())
        return peliculas

    def buscar_actores(self):
        actores = set()
        for pelicula in self.__catalogo:
            actores_pelicula = pelicula.actores()
            if isinstance(actores_pelicula, list):
                actores.update(actores_pelicula)
            elif isinstance(actores_pelicula, str):
                actores.add(actores_pelicula)
        return list(actores)