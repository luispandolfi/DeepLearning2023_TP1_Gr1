import matplotlib.pyplot as plt
from persona import Persona
import pandas as pd

class StatsPersona:

    @classmethod
    def plot_personas_por_anio_nacimiento(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_anio = stats_personas["personas_por_anio"]
        plt.bar(personas_por_anio.index, personas_por_anio.values)
        plt.xlabel("Año de nacimiento")
        plt.ylabel("#Personas")
        plt.title("Cantidad de personas por año de nacimiento")
        plt.show()


    @classmethod
    def plot_personas_por_genero(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_genero = stats_personas["personas_por_genero"]
        plt.bar(personas_por_genero.index, personas_por_genero.values)
        plt.xlabel("Género")
        plt.ylabel("#Personas")
        plt.title("Cantidad de personas por género")
        plt.show()
        

    @classmethod
    def plot_personas_por_anio_nacimiento_y_genero(cls, df_personas):
        auxiliar_df = df_personas.groupby(['year of birth','Gender'])['id'].count().reset_index().rename(columns={'id':'Count'})
        pivot = pd.pivot_table(data=auxiliar_df, index=['year of birth'], columns=['Gender'], values=['Count'])
        ax = pivot.plot.bar(stacked=True, color =['lightseagreen', 'tomato'], figsize=(8,6))
        ax.set_title('Personas por año separadas por genero', fontsize=20)
        plt.show()
        pass