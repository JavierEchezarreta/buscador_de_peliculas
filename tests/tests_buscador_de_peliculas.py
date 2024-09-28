import pytest
from src.buscador_de_peliculas import BuscadorPeliculas

@pytest.fixture
def buscador():
    return BuscadorPeliculas()

def test_agregar_pelicula_al_catalogo(buscador):
    pass

def test_agregar_pelicula_al_catalogo_desde_archivo_externo(buscador):
    pass

def test_buscar_pelicula_por_titulo(buscador):
    pass

def test_buscar_pelicula_por_anio_de_lanzamiento(buscador):
    pass

def test_buscar_pelicula_por_genero(buscador):
    pass

def test_buscar_peliculas_comunes_a_dos_actores(buscador):
    pass

def test_mostrar_informacion_de_la_pelicula(buscador):
    pass

def test_buscar_actores(buscador):
    pass




