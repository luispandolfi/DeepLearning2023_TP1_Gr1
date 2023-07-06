import pandas as pd


class Score:
  
  def __init__(self, id_usuario, id_pelicula, puntuacion, fecha, id=None):
    self.id_usuario = id_usuario
    self.id_pelicula = id_pelicula
    self.puntuacion = puntuacion
    self.fecha = fecha
    self.id = id


  def __repr__(self):
    # Este método imprime la información de este puntaje.
    pass


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
  def get_from_df(cls, df, id=None, id_usuario=None, id_pelicula=None, puntuacion=None, fecha=None):
    # Este class method devuelve una lista de objetos 'Score' buscando por:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass


  def write_df(self, df): 
    # Este método recibe el dataframe de scores y agrega el puntaje.
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no lo agrega y devuelve un error.
    new_row = {
      "Occupation": self.ocupacion,
      "Active Since": self.fecha_alta,
    }
    if self.id == None:
      new_row["id"] = df.id.max() + 1
    elif self.id in df.id.values:
      raise ValueError("Id no válido, ya se encuentra en el DataFrame")
    else:
      new_row["id"] = self.id
    
    df = pd.append(new_row, ignore_index = True)
    return df


  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    scores = self.get_from_df(df, self.id, self.id_usuario, self.id_pelicula, self.puntuacion, [self.fecha, self.fecha])
    if (len(scores) == 1):
      return df[df.id != self.id]
    else:
      raise Exception('El score no coincide con ninguno de los existentes en el dataframe.')


  @classmethod
  def get_stats(cls, df):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass