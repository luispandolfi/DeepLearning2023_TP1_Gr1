import pandas as pd

class Persona:
  
  def __init__(self, nombreCompleto, fechaNacimiento, genero, codigoPostal, id = None):
    self.nombreCompleto = nombreCompleto
    self.fechaNacimiento = fechaNacimiento
    self.genero = genero
    self.codigoPostal = codigoPostal
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
  def get_from_df(cls, df, id=None, nombreCompleto=None, fechaNacimiento=None, genero=None, codigoPostal=None):
    # Este class method devuelve una lista de objetos 'Persona' buscando por:
    # id: id
    # nombreCompleto: nombre completo
    # fechaNacimiento: fecha de nacimiento
    # genero: genero (M o F)
    # codigoPostal: codigo postal
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
    pass
  
  @classmethod
  def get_stats(cls, df):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass