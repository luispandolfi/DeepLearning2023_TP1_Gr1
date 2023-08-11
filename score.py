from dataFrameHelper import DataFrameHelper
import pandas as pd
from pelicula import Pelicula
from usuario import Usuario
import datetime

class Score:
  
  def __init__(self, id_usuario, id_pelicula, puntuacion, fecha, id=None):
    self.id_usuario = id_usuario
    self.id_pelicula = id_pelicula
    self.puntuacion = puntuacion
    self.fecha = pd.to_datetime(fecha, format="%Y-%m-%d")
    self.id = id


  def __repr__(self):
    # Este método imprime la información de este puntaje.
    return f'ID: {self.id}, ID Usuario: {self.id_usuario}, ID Pelicula: {self.id_pelicula}, Puntuacion: {self.puntuacion}, Fecha: {self.fecha}\n'
    


  @classmethod
  def create_df_from_csv(cls, filename, df_usuarios, df_peliculas):
    # Este class method recibe el nombre de un archivo csv, valida su 
    # estructura y devuelve un DataFrame con la información cargada del
    # archivo 'filename'.
    df = pd.read_csv(filename)
    df = cls.clean_df(df, df_usuarios, df_peliculas)
    return df


  @classmethod
  def clean_df(cls, df, df_usuarios, df_peliculas):
    df = df.dropna()
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %H:%M:%S")
    # el user_id exista en usuarios
    id_usuarios = set(df_usuarios["id"])
    df = df.loc[df["user_id"].isin(id_usuarios)]
    # el movie_id exista en peliculas
    id_peliculas = set(df_peliculas["id"])
    df = df.loc[df["movie_id"].isin(id_peliculas)]
    # rating entre 1 y 5
    df = df.loc[df["rating"].isin([1,2,3,4,5])]
    return df


  @classmethod
  def __filter_df__(cls, df, id=None, id_usuario=None, id_pelicula=None, puntuacion=None, fecha_score=None):
    datos_filtrados = df
    
    if fecha_score != None:
      if len(fecha_score) == 2:
        datos_filtrados = datos_filtrados[(datos_filtrados["Date"] >= fecha_score[0]) & (datos_filtrados["Date"] <= fecha_score[1])]
      else:
        raise ValueError("El parámetro fecha_score debe ser una lista de largo 2")
    
    if  id !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["id"] == id)]

    if id_usuario !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["user_id"] == id_usuario)]

    if id_pelicula !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["movie_id"] == id_pelicula)]

    if puntuacion !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["rating"] == puntuacion)]
    
    return datos_filtrados


  @classmethod    
  def get_from_df(cls, df, id=None, id_usuario=None, id_pelicula=None, puntuacion=None, fecha=None):
    # Este class method devuelve una lista de objetos 'Score' buscando por:

    datos_filtrados = Score.__filter_df__(df, id, id_usuario, id_pelicula, puntuacion, fecha)

    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo = fila['id']
      userid = fila['user_id']
      movieid = fila['movie_id']
      puntaje = fila['rating']
      fecha_calificacion = fila['Date']
      scorex = Score(id=codigo, id_usuario=userid, id_pelicula=movieid,puntuacion=puntaje,fecha=fecha_calificacion)
      lista_respuesta.append(scorex)
    return lista_respuesta


  def write_df(self, df, df_usuarios, df_peliculas): 
    # Este método recibe el dataframe de scores y agrega el puntaje.
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no lo agrega y devuelve un error.
    new_row = {
      "user_id": self.id_usuario,
      "movie_id": self.id_pelicula,
      "rating": self.puntuacion,
      "Date": self.fecha,
    }

    df_is_usuario_exist = df_usuarios[df_usuarios['id']== self.id_usuario]
    df_is_movie_exist = df_peliculas[df_peliculas['id']== self.id_pelicula]

    if df_is_usuario_exist.empty or df_is_movie_exist.empty:
      raise Exception('Error al guardar calificacion, no existe usuario o pelicula.')
    else:
      return DataFrameHelper.append_row(df, new_row, self.id)


  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    scores = self.get_from_df(df, self.id, self.id_usuario, self.id_pelicula, self.puntuacion, [self.fecha, self.fecha])
    if (len(scores) == 1):
      return df[df.id != scores[0].id]
    else:
      raise Exception('El score no coincide con ninguno de los existentes en el dataframe.')


  @classmethod
  def get_stats_puntuacion_promedio_usuarios_por_anio_pelicula(cls, df_scores, df_peliculas, rango_anio_pelicula=None):
    # filtro películas por año
    filtered_peliculas = Pelicula.__filter_df__(df_peliculas, anios=rango_anio_pelicula)
    
    # join de scores con películas
    joined = pd.merge(df_scores, filtered_peliculas, how='inner', left_on='movie_id', right_on='id')

    stats = {
      "puntuacion_promedio": joined.groupby(joined['Release Date'].dt.year)['rating'].mean()
    }
    return stats
  
  
  @classmethod
  def get_stats_puntuacion_promedio_usuarios_por_genero_pelicula(cls, df_scores, df_peliculas, generos):
    # join de scores con películas
    joined = pd.merge(df_scores, df_peliculas, how='inner', left_on='movie_id', right_on='id')
    
    # calculo el promedio para cada género
    promedios = []
    for genero in generos:
      promedios.append(joined[joined[genero] == 1]['rating'].mean())
    
    serie = pd.Series(promedios, generos)
    stats = {
      "puntuacion_promedio": serie
    }
    return stats


  @classmethod
  def get_stats_puntuacion_promedio_peliculas_por_ocupacion(cls, df_scores, df_usuarios):
    # join de scores con usuarios
    joined = pd.merge(df_scores, df_usuarios, how='inner', left_on='user_id', right_on='id')

    stats = {
      "puntuacion_promedio": joined.groupby('Occupation')['rating'].mean()
    }
    return stats
  

  @classmethod
  def get_stats_puntuacion_promedio_peliculas_por_genero_usuario(cls, df_scores, df_usuarios, df_personas):
    # join de usuarios con personas
    usuarios_personas = pd.merge(df_usuarios, df_personas, how='inner', left_on='id', right_on='id')
    
    # join con scores
    joined = pd.merge(df_scores, usuarios_personas, how='inner', left_on='user_id', right_on='id')

    stats = {
      "puntuacion_promedio": joined.groupby('Gender')['rating'].mean()
    }
    return stats
  

  @classmethod
  def get_stats_puntuacion_promedio_peliculas_por_grupo_etareo(cls, df_scores, df_usuarios, df_personas):
    # join de usuarios con personas
    usuarios_personas = pd.merge(df_usuarios, df_personas, how='inner', left_on='id', right_on='id')
    # para cada usuario calculo su grupo etáreo
    usuarios_personas["grupo etareo"] = usuarios_personas.apply(Score.__grupo_etareo__, axis=1)
    # join con scores
    joined = pd.merge(df_scores, usuarios_personas, how='inner', left_on='user_id', right_on='id')

    stats = {
      "puntuacion_promedio": joined.groupby('grupo etareo')['rating'].mean()
    }
    return stats
  

  @classmethod
  def __grupo_etareo__(cls, df_personas_row):
    anio_nacimiento = df_personas_row["year of birth"]
    edad = datetime.date.today().year - anio_nacimiento
    rangos = [[0,6], [7,12], [13,24], [25,36], [37,48], [49,60], [60, 999]]
    for rango in rangos:
      if (rango[0] <= edad & edad <= rango[1]):
        if (rango[1] == 999):
          return f'> {rango[0]}'
        else:
          return f'{rango[0]} - {rango[1]}'
    return "no definido"