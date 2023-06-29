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
  def create_df_from_csv(cls, filename):
    # Este class method recibe el nombre de un archivo csv, valida su 
    # estructura y devuelve un DataFrame con la información cargada del
    # archivo 'filename'.
    pass
  
  @classmethod    
  def get_from_df(cls, df, id=None):
    # Este class method devuelve una lista de objetos 'Score' buscando por:
    # 
    # TODO completar comentario y agregar parametros al metodo
    pass

  def write_df(self, df): 
    # Este método recibe el dataframe de scores y agrega el puntaje.
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