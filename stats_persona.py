import matplotlib.pyplot as plt
from persona import Persona

class StatsPersona:

    @classmethod
    def plot_personas_por_anio_nacimiento(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_anio = stats_personas["personas_por_anio"]
        plt.bar(personas_por_anio.index, personas_por_anio.values)
        plt.show()


    @classmethod
    def plot_personas_por_genero(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_genero = stats_personas["personas_por_genero"]
        plt.bar(personas_por_genero.index, personas_por_genero.values)
        plt.show()
        

    @classmethod
    def plot_personas_por_anio_nacimiento_y_genero(cls):
        pass