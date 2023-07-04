import pandas as pd

class Persona:
  
  def __init__(self, nombre_completo, fecha_nacimiento, genero, codigo_postal, id = None):
    self.nombre_completo = nombre_completo
    self.fecha_nacimiento = fecha_nacimiento
    self.genero = genero
    self.codigo_postal = codigo_postal
    self.id = id

  def __repr__(self):
    # Este método imprime la información de esta persona.
    pass

  @classmethod
  def create_df_from_csv(cls, filename):
    # Este class method recibe el nombre de un archivo csv, valida su 
    # estructura y devuelve un DataFrame con la información cargada del
    # archivo 'filename'.
    df = pd.read_csv(filename)
    df = cls.clean_df(df)
    return df
  
  @classmethod
  def clean_df(cls, df):
    df = df.dropna()
    df = df.drop_duplicates(subset = ["id"])
    df = df.loc[df["Gender"].isin(["M", "F"])]
    return df
  
  @classmethod    
  def get_from_df(cls, df, id=None, nombre_completo=None, fecha_nacimiento=None, genero=None, codigo_postal=None):
    # Este class method devuelve una lista de objetos 'Persona' buscando por:
    # id: id
    # nombre_completo: nombre completo
    # fecha_nacimiento: fecha de nacimiento
    # genero: genero (M o F)
    # codigo_postal: codigo postal
    pass

  def write_df(self, df): 
    # Este método recibe el dataframe de personas y agrega la persona
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no la agrega y devuelve un error.
    pass
  
  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    personas = self.get_from_df(df, self.id, self.nombre_completo, self.fecha_nacimiento, self.genero, self.codigo_postal)
    if (len(personas) > 0):
      return df[df.id != self.id]
    else:
      raise Exception('La persona no coincide con ninguna de las existentes en el dataframe.')
  
  @classmethod
  def get_stats(cls, df):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass