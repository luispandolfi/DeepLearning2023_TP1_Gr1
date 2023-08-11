import matplotlib.pyplot as plt
from persona import Persona
import pandas as pd
from matplotlib.ticker import MultipleLocator

class StatsPersona:

    @classmethod
    def plot_personas_por_anio_nacimiento(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_anio = stats_personas["personas_por_anio"]
        plt.figure(figsize=(10,5))
        plt.bar(personas_por_anio.index, personas_por_anio.values, color="lightseagreen")
        plt.xlabel("Año de nacimiento")
        plt.ylabel("#Personas")
        plt.title("Cantidad de personas por año de nacimiento")
        plt.show()


    @classmethod
    def plot_personas_por_genero(cls, df_personas):
        stats_personas = Persona.get_stats(df_personas)
        personas_por_genero = stats_personas["personas_por_genero"]
        plt.bar(personas_por_genero.index, personas_por_genero.values, color="lightseagreen")
        plt.xlabel("Género")
        plt.ylabel("#Personas")
        plt.title("Cantidad de personas por género")
        plt.show()
        

    @classmethod
    def plot_personas_por_anio_nacimiento_y_genero(cls, df_personas):
        pivot = df_personas.pivot_table(index='year of birth', columns='Gender', aggfunc='size', fill_value=0)
        
        # Reindex con un rango completo de años, completando los missing con ceros
        all_years = range(min(pivot.index), max(pivot.index) + 1)
        pivot = pivot.reindex(all_years, fill_value=0)
        
        # Crea el plot
        ax = pivot.plot.bar(stacked=True, color =['lightseagreen', 'tomato'], figsize=(10,5))

        # Configura eje x
        #ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.xaxis.set_major_locator(MultipleLocator(10))
        plt.xticks(rotation=0)
        
        #Configura el legend
        handles, _ = ax.get_legend_handles_labels()
        ax.legend(handles[::], ['F', 'M'], title='Género',loc='upper left')

        ax.set_title("Cantidad de personas por género y año")
        plt.show()