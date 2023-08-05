import matplotlib.pyplot as plt
from trabajador import Trabajador

class StatsTrabajador:

    @classmethod
    def plot_trabajadores_por_puesto(cls, df_trabajadores):
        stats_trabajadores = Trabajador.get_stats(df_trabajadores)
        trabajadores_por_puesto = stats_trabajadores["trabajadores_por_puesto"]
        plt.barh(trabajadores_por_puesto.index, trabajadores_por_puesto.values)
        plt.show()