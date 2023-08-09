from dataFrameHelper import DataFrameHelper
import pandas as pd
from persona import Persona

class Trabajador:
  
  def __init__(self, id, fecha_alta, puesto, categoria, horario_trabajo):
    self.id = id
    self.fecha_alta = pd.to_datetime(fecha_alta, format="%Y-%m-%d")
    self.puesto = puesto
    self.categoria = categoria
    self.horario_trabajo = horario_trabajo


  def __repr__(self):
    # Este método imprime la información de este trabajador.
    return f'ID: {self.id}, Fecha de alta: {self.fecha_alta}, Puesto: {self.puesto}, Categoria: {self.categoria}, Horario laboral: {self.horario_trabajo}\n'
    

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
  def __filter_df__(cls, df, id=None, fecha_alta=None, puesto=None, categoria=None, horario_trabajo=None):
    datos_filtrados = df

    if id != None:
      datos_filtrados = datos_filtrados[(datos_filtrados["id"] == id)]
    
    if fecha_alta != None:
      if len(fecha_alta) == 2:
        datos_filtrados = datos_filtrados[(datos_filtrados["Start Date"] >= f'{fecha_alta[0]}') & (datos_filtrados["Start Date"] <= f'{fecha_alta[1]}')]
      else:
        raise ValueError("La lista fecha_alta debe tener largo 2")
    
    if puesto != None:
      datos_filtrados = datos_filtrados[datos_filtrados["Position"].str.contains(puesto, case=False)]      #datos_filtrados[datos_filtrados['Name'].str.contains(nombre,case=False)]
    
    if categoria != None:
      datos_filtrados = datos_filtrados[datos_filtrados["Category"].str.contains(categoria, case=False)]

    if horario_trabajo != None:
      datos_filtrados = datos_filtrados[(datos_filtrados["Working Hours"] == horario_trabajo)]
    
    return datos_filtrados


  @classmethod
  def get_from_df(cls, df, id=None, fecha_alta=None, puesto=None, categoria=None, horario_trabajo=None):
    # Este class method devuelve una lista de objetos 'Trabajador' buscando por:
    # - id: id
    # - fecha_alta: [fecha_desde, fecha_hasta]
    # - puesto: puesto
    # - categoria: categoria
    # - horario_trabajo: horario de trabajo

    datos_filtrados = Trabajador.__filter_df__(df, id, fecha_alta, puesto, categoria, horario_trabajo)

    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo_ = fila['id']
      fecha_ = fila['Start Date']
      puesto_ = fila['Position']

      categoria_ = fila['Category']
      horario_ = fila['Working Hours']
      trabajadorx = Trabajador(codigo_, fecha_, puesto_, categoria_, horario_)
      lista_respuesta.append(trabajadorx)
    return lista_respuesta


  def write_df(self, df, df_personas): 
    # Este método recibe el dataframe de trabajadores y agrega al trabajador
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no lo agrega y devuelve un error.
    new_row = {
      "Position": self.puesto,
      "Category": self.categoria,
      "Working Hours": self.horario_trabajo,
      "Start Date": self.fecha_alta,
    }

    df_is_persona_exist = df_personas[df_personas['id']== self.id]
    if (df_is_persona_exist.empty):
      raise Exception('Error al guardar un trabajador no dado de alta como persona.')
    else:
      return DataFrameHelper.append_row(df, new_row, self.id)



  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    trabajadores = self.get_from_df(df, self.id, [self.fecha_alta, self.fecha_alta], self.puesto, self.categoria, self.horario_trabajo)
    if (len(trabajadores) == 1):
      return df[df.id != self.id]
    else:
      raise Exception('El trabajador no coincide con ninguno de los existentes en el dataframe.')


  @classmethod
  def get_stats(cls, df_trabajadores, df_personas, anio_nacimiento=None, puesto=None):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta a los data frames.
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # - Año de nacimiento: [desde, hasta]
    # - Puesto
    # Se devuelve:
    # - Total de trabajadores
    # - Cantidad de trabajadores por año de nacimiento
    # - Cantidad de trabajadores por puesto

    # filtro trabajadores por puesto
    df_trabajadores = Trabajador.__filter_df__(df_trabajadores, puesto=puesto)

    # filtro personas por año de nacimiento
    df_personas = Persona.__filter_df__(df_personas, anio_nacimiento=anio_nacimiento)
    
    # join de ambos resultados
    joined = pd.merge(df_trabajadores, df_personas, how='inner', on='id')

    stats = {
      "total_trabajadores": len(joined.index),
      "trabajadores_por_anio": joined.groupby('year of birth').size(),
      "trabajadores_por_puesto": joined.groupby('Position').size()
    }

    return stats