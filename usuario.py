from dataFrameHelper import DataFrameHelper
import pandas as pd

class Usuario:
  
  def __init__(self, id, fecha_alta, ocupacion):
    self.id = id
    self.fecha_alta = fecha_alta
    self.ocupacion = ocupacion


  def __repr__(self):
    # Este método imprime la información de este trabajador.
    return f'ID: {self.id}, Fecha de alta: {self.fecha_alta}, Ocupacion: {self.ocupacion}\n'
    

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
    df["Active Since"] = pd.to_datetime(df["Active Since"], format="%Y-%m-%d %H:%M:%S")
    id_personas = set(df_personas["id"])
    df = df.loc[df["id"].isin(id_personas)]
    return df


  @classmethod    
  def get_from_df(cls, df, id=None, fecha_alta=None, ocupacion=None):
    # Este class method devuelve una lista de objetos 'Usuario' buscando por:
    # 
    # TODO completar comentario y agregar parametros al metodo
    datos_filtrados = df

    if id !=  None:
      datos_filtrados = datos_filtrados[datos_filtrados["id"] == id]
    
    if fecha_alta != None:
      if len(fecha_alta) == 2:
        datos_filtrados = datos_filtrados[(datos_filtrados["Active Since"] >= f'{fecha_alta[0]}') & (datos_filtrados["Active Since"] <= f'{fecha_alta[1]}')]
      else:
        raise ValueError("la lista anios debe tener largo 2")
    
    if ocupacion!= None:
      datos_filtrados = datos_filtrados[datos_filtrados["Occupation"] == ocupacion]
    
    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo_ = fila['id']
      fecha_ = fila['Active Since']
      puesto_ = fila['Occupation']

      usuariox = Usuario(codigo_, fecha_, puesto_)
      lista_respuesta.append(usuariox)
    return lista_respuesta


  def write_df(self, df):
    # Este método recibe el dataframe de usuarios y agrega al usuario
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no lo agrega y devuelve un error.
    new_row = {
      "Occupation": self.ocupacion,
      "Active Since": self.fecha_alta,
    }
    return DataFrameHelper.append_row(df, new_row, self.id)

  
  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    usuarios = self.get_from_df(df, self.id, [self.fecha_alta, self.fecha_alta], self.ocupacion)
    if (len(usuarios) == 1):
      return df[df.id != self.id]
    else:
      raise Exception('El usuario no coincide con ninguno de los existentes en el dataframe.')


  @classmethod
  def get_stats(cls, df, fecha_alta=None, ocupacion=None):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # Año
    # Ocupacion
    # Se devuelve:
    # Id del ususario mas viejo
    # Id del más nuevo
    # Bar plot de ocupacion vs n# usuarios

    datos_filtrados = df
    #Filtrar con funcion
    stats={
      "id_ususario_mas_nuevo": datos_filtrados['id'].iloc[datos_filtrados['Active Since'].argmin()],
      "id_usuario_mas_viejo": datos_filtrados['id'].iloc[datos_filtrados['Active Since'].argmax()], 
      "plots_ocupacion": datos_filtrados['Occupation'].value_counts(sort=False),
    }
    return stats
