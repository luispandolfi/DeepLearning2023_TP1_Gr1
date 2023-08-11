import matplotlib.pyplot as plt
from pelicula import Pelicula

class StatsPelicula:

    @classmethod
    def plot_peliculas_por_anio_estreno(cls, df_peliculas):
        stats_peliculas = Pelicula.get_stats(df_peliculas)
        peliculas_por_anio = stats_peliculas["peliculas_por_anio"]
        plt.figure(figsize=(10,5))
        plt.bar(peliculas_por_anio.index, peliculas_por_anio.values, color="lightseagreen")
        plt.yscale("log") # escala logaritmica para el eje y
        plt.xlabel("Año de estreno")
        plt.ylabel("#Películas (esc. log)")
        plt.title("Cantidad de películas por año de estreno")
        plt.show()
    

    @classmethod
    def plot_peliculas_por_genero(cls, df_peliculas):
        stats_peliculas = Pelicula.get_stats(df_peliculas)
        peliculas_por_genero = stats_peliculas["peliculas_por_genero"].sort_values(ascending=True)   
        plt.barh(peliculas_por_genero.index, peliculas_por_genero.values, color="lightseagreen")
        plt.xlabel("#Películas")
        plt.ylabel("Género")
        plt.title("Cantidad de películas por género")
        plt.show()