import matplotlib.pyplot as plt
from trabajador import Trabajador

class StatsTrabajador:

    @classmethod
    def plot_trabajadores_por_puesto(cls, df_trabajadores, df_personas):
        stats_trabajadores = Trabajador.get_stats(df_trabajadores, df_personas)
        trabajadores_por_puesto = stats_trabajadores["trabajadores_por_puesto"].sort_values(ascending=True)   
        plt.barh(trabajadores_por_puesto.index, trabajadores_por_puesto.values)
        plt.xlabel("#Trabajadores")
        plt.ylabel("Puesto")
        plt.title("Cantidad de trabajadores por puesto")
        plt.show()
    

    @classmethod
    def plot_trabajadores_por_anio_nacimiento(cls, df_trabajadores, df_personas):
        stats_trabajadores = Trabajador.get_stats(df_trabajadores, df_personas)
        trabajadores_por_anio = stats_trabajadores["trabajadores_por_anio"]
        plt.bar(trabajadores_por_anio.index, trabajadores_por_anio.values)
        plt.xlabel("Año de nacimiento")
        plt.ylabel("#Trabajadores")
        plt.title("Cantidad de trabajadores por año de nacimiento")
        plt.show()