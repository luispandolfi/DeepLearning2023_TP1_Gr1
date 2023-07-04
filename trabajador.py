from persona import Persona
import pandas as pd

class Trabajador(Persona):
  
  def __init__(self, fecha_alta, puesto, categoria, horario_trabajo):
    self.fecha_alta = fecha_alta
    self.puesto = puesto
    self.categoria = categoria
    self.horario_trabajo = horario_trabajo

  def __repr__(self):
    # Este método imprime la información de este trabajador.
    pass

  @classmethod
  def create_df_from_csv(cls, filename, df_personas):
    # Este class method recibe el nombre de un archivo csv, valida su 
    # estructura y devuelve un DataFrame con la información cargada del
    # archivo 'filename'.
    df = pd.read_csv(filename)
    df = cls.clean_df(df, df_personas)
    return df
  
  @classmethod
  def clean_df(cls, df, df_personas):
    df = df.dropna()
    df["Start Date"] = pd.to_datetime(df["Start Date"], format="%Y-%m-%d")
    id_personas = set(df_personas["id"])
    df = df.loc[df["id"].isin(id_personas)]
    return df

  @classmethod    
  def get_from_df(cls, df, id=None):
    # Este class method devuelve una lista de objetos 'Trabajador' buscando por:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass

  def write_df(self, df): 
    # Este método recibe el dataframe de trabajadores y agrega al trabajador
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no lo agrega y devuelve un error.
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