import matplotlib.pyplot as plt
from usuario import Usuario

class StatsUsuario:

    @classmethod
    def plot_usuarios_por_ocupacion(cls, df_usuarios, df_personas):
        stats_usuarios = Usuario.get_stats(df_usuarios, df_personas)
        usuarios_por_ocupacion = stats_usuarios["usuarios_por_ocupacion"].sort_values(ascending=True)    
        plt.barh(usuarios_por_ocupacion.index, usuarios_por_ocupacion.values, color="lightseagreen")
        plt.xlabel("#Usuarios")
        plt.ylabel("Ocupación")
        plt.title("Cantidad de usuarios por ocupación")
        plt.show()
    

    @classmethod
    def plot_usuarios_por_anio_nacimiento(cls, df_usuarios, df_personas):
        stats_usuarios = Usuario.get_stats(df_usuarios, df_personas)
        usuarios_por_anio = stats_usuarios["usuarios_por_anio"]
        plt.figure(figsize=(10,5))
        plt.bar(usuarios_por_anio.index, usuarios_por_anio.values, color="lightseagreen")
        plt.xlabel("Año de nacimiento")
        plt.ylabel("#Usuarios")
        plt.title("Cantidad de usuarios por año de nacimiento")
        plt.show()
        pass
