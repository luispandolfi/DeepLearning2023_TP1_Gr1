import matplotlib.pyplot as plt
from usuario import Usuario

class StatsUsuario:

    @classmethod
    def plot_usuarios_por_ocupacion(cls, df_usuarios):
        stats_usuarios = Usuario.get_stats(df_usuarios)
        usuarios_por_ocupacion = stats_usuarios["usuarios_por_ocupacion"]
        plt.barh(usuarios_por_ocupacion.index, usuarios_por_ocupacion.values)
        plt.show()
