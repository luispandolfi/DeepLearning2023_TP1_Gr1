import matplotlib.pyplot as plt
from pelicula import Pelicula

class StatsPelicula:

    @classmethod
    def plot_peliculas_por_anio_estreno(cls, df_peliculas):
        stats_peliculas = Pelicula.get_stats(df_peliculas)
        peliculas_por_anio = stats_peliculas["peliculas_por_anio"]
        plt.bar(peliculas_por_anio.index, peliculas_por_anio.values)
        plt.yscale("log") # escala logaritmica para el eje y
        plt.show()
    

    @classmethod
    def plot_peliculas_por_genero(cls, df_peliculas):
        stats_peliculas = Pelicula.get_stats(df_peliculas)
        peliculas_por_genero = stats_peliculas["peliculas_por_genero"]
        plt.barh(peliculas_por_genero.index, peliculas_por_genero.values)
        plt.show()