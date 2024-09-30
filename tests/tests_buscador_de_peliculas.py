import pytest
from src.buscador_de_peliculas import BuscadorPeliculas

@pytest.fixture
def buscador():
    return BuscadorPeliculas()

def test_agregar_pelicula(buscador):

    buscador.agregar_pelicula('poster', 'titulo', 'sinopsis', 'actores', 'puntuacion', 'genero', 'duracion')
    assert buscador.cantidad_peliculas() == 1

def test_importar_peliculas_desde_archivo(buscador):

    buscador.importar_peliculas('archivo.json')
    assert buscador.cantidad_peliculas() == 2

def test_buscar_pelicula_por_titulo(buscador):

    buscador.agregar_pelicula('poster', 'El secreto de sus ojos', 'sinopsis', 'actores', 'puntuacion', 'genero', 'duracion')
    pelicula = buscador.buscar_pelicula_por_titulo('El secreto de sus ojos')
    assert pelicula.titulo() == 'El secreto de sus ojos'

def test_buscar_pelicula_por_genero(buscador):

    buscador.agregar_pelicula('poster', 'titulo', 'sinopsis', 'actores', 'puntuacion', 'drama', 'duracion')
    pelicula = buscador.buscar_pelicula_por_genero('drama')
    assert pelicula.genero() == 'drama'

def test_buscar_peliculas_comunes_por_actores(buscador):

    buscador.agregar_pelicula('poster', 'El secreto de sus ojos', 'sinopsis', ['Francella', 'Darin'], 'puntuacion', 'genero', 'duracion')
    buscador.agregar_pelicula('poster', 'Nuevo Reinas', 'sinopsis', ['Pauls', 'Darin'], 'puntuacion', 'genero','duracion')
    buscador.agregar_pelicula('poster', 'Granizo', 'sinopsis', ['Francella', 'Peña'], 'puntuacion', 'genero','duracion')
    buscador.agregar_pelicula('poster', 'Esperando la carroza', 'sinopsis', ['Francella', 'Darin'], 'puntuacion','genero', 'duracion')
    peliculas = buscador.buscar_peliculas_comunes_por_actores('Francella', 'Darin')
    assert "El secreto de sus ojos" in peliculas
    assert "Esperando la carroza" in peliculas

def test_buscar_actores(buscador):

    buscador.agregar_pelicula('poster', 'El secreto de sus ojos', 'sinopsis', ['Francella', 'Darin'], 'puntuacion','genero', 'duracion')
    buscador.agregar_pelicula('poster', 'Titanic', 'sinopsis', 'Di Caprio', 'puntuacion','genero', 'duracion')
    actores = buscador.buscar_actores()
    assert 'Francella' in actores
    assert 'Darin' in actores
    assert 'Di Caprio' in actores