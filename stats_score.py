import matplotlib.pyplot as plt
from score import Score

class StatsScore:

    @classmethod
    def plot_puntuacion_promedio_usuarios_por_anio_pelicula(cls, df_scores, df_peliculas, rango_anio_pelicula=None):
        stats = Score.get_stats_puntuacion_promedio_usuarios_por_anio_pelicula(df_scores, df_peliculas, rango_anio_pelicula=rango_anio_pelicula)
        puntuacion_promedio = stats["puntuacion_promedio"]
        plt.bar(puntuacion_promedio.index, puntuacion_promedio.values)
        plt.xlabel("Año de estreno")
        plt.ylabel("Puntuación promedio")
        plt.title("Puntuación promedio de usuarios por año de estreno de películas")
        plt.show()


    @classmethod
    def plot_puntuacion_promedio_usuarios_por_genero_pelicula(cls, df_scores, df_peliculas, generos_pelicula=None):
        pass
    

    @classmethod
    def plot_puntuacion_promedio_peliculas_por_ocupacion(cls, df_scores, df_usuarios):
        stats = Score.get_stats_puntuacion_promedio_peliculas_por_ocupacion(df_scores, df_usuarios)
        puntuacion_promedio = stats["puntuacion_promedio"]
        plt.barh(puntuacion_promedio.index, puntuacion_promedio.values)
        plt.xlabel("Puntuación promedio")
        plt.ylabel("Ocupación")
        plt.title("Puntuación promedio de películas por ocupación")
        plt.show()
    

    @classmethod
    def plot_puntuacion_promedio_peliculas_por_genero_usuario(cls, df_scores, df_usuarios, df_personas):
        stats = Score.get_stats_puntuacion_promedio_peliculas_por_genero_usuario(df_scores, df_usuarios, df_personas)
        puntuacion_promedio = stats["puntuacion_promedio"]
        plt.bar(puntuacion_promedio.index, puntuacion_promedio.values)
        plt.xlabel("Género")
        plt.ylabel("Puntuación promedio")
        plt.title("Puntuación promedio de películas por género de usuario")
        plt.show()


    @classmethod
    def plot_puntuacion_promedio_peliculas_por_rangos_edad(cls, df_scores, df_usuarios, rangos_edad):
        pass