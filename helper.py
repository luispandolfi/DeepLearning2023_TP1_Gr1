from persona import Persona
from usuario import Usuario
from trabajador import Trabajador
from pelicula import Pelicula
from score import Score


def load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores):
  df_personas = Persona.create_df_from_csv(file_personas)
  df_trabajadores = Trabajador.create_df_from_csv(file_trabajadores, df_personas)
  df_usuarios = Usuario.create_df_from_csv(file_usuarios, df_personas)
  df_peliculas = Pelicula.create_df_from_csv(file_peliculas)
  df_scores = Score.create_df_from_csv(file_scores, df_usuarios, df_peliculas)
  return df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores


def load_to_dfstore(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores):
  dfs = load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores)
  return DataFrameStore(dfs[0], dfs[1], dfs[2], dfs[3], dfs[4])


class DataFrameStore:

  def __init__(self, personas, trabajadores, usuarios, peliculas, scores):
    self.personas = personas
    self.trabajadores = trabajadores
    self.usuarios = usuarios
    self.peliculas = peliculas
    self.scores = scores

def save_dfs(df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores, file_personas="csv_files/personas.csv", file_trabajadores="csv_files/trabajadores.csv", file_usuarios="csv_files/usuarios.csv", file_peliculas="csv_files/peliculas.csv", file_scores="csv_files/scores.csv"):
    #
    # Guarda los dataframes en archivos CSVs
    #
    try:
        df_personas.to_csv(file_personas, index=False)
        df_trabajadores.to_csv(file_trabajadores, index=False)
        df_usuarios.to_csv(file_usuarios, index=False)
        df_peliculas.to_csv(file_peliculas, index=False)
        df_scores.to_csv(file_scores, index=False)
        print("CSVs guardados exitosamente")
        return 0
    except:
        print("Error en el guardado de CSVs")
        return -1

