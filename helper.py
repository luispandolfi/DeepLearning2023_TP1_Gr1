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
