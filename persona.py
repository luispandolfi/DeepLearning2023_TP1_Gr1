from dataFrameHelper import DataFrameHelper
import pandas as pd


class Persona:
  
  def __init__(self, nombre_completo, anio_nacimiento, genero, codigo_postal, id = None):
    self.nombre_completo = nombre_completo
    self.anio_nacimiento = anio_nacimiento
    self.genero = genero
    self.codigo_postal = codigo_postal
    self.id = id


  def __repr__(self):
    # Este método imprime la información de esta persona.
    return f'Nombre: {self.nombre_completo}, Fecha de nacimiento: {self.anio_nacimiento}, Genero: {self.genero}, Codigo Postal: {self.codigo_postal}, ID: {self.id}\n'
    #pass


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
  def __filter_df__(cls, df, id=None, nombre_completo=None, anio_nacimiento=None, genero=None, codigo_postal=None):
    datos_filtrados = df
    
    if anio_nacimiento != None:
      if len(anio_nacimiento) == 2:
        datos_filtrados = datos_filtrados[(datos_filtrados["year of birth"] >= anio_nacimiento[0]) & (datos_filtrados["year of birth"] <= anio_nacimiento[1])]
      else:
        raise ValueError("El parámetro anio_nacimiento debe ser una lista de largo 2")
    
    if nombre_completo != None:
      datos_filtrados = datos_filtrados[datos_filtrados['Full Name'].str.contains(nombre_completo,case=False)]

    if id !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["id"] == id)]

    if genero!= None:
      datos_filtrados = datos_filtrados[(datos_filtrados["Gender"] == genero)]
    
    if codigo_postal != None:
      datos_filtrados = datos_filtrados[(datos_filtrados["Zip Code"] == codigo_postal)]
    
    return datos_filtrados


  @classmethod    
  def get_from_df(cls, df, id=None, nombre_completo=None, anio_nacimiento=None, genero=None, codigo_postal=None):
    # Este class method devuelve una lista de objetos 'Persona' buscando por:
    # - id: id
    # - nombre_completo: nombre completo
    # - anio_nacimiento: [desde_año, hasta_año]
    # - genero: genero (M o F)
    # - codigo_postal: codigo postal
    
    datos_filtrados = Persona.__filter_df__(df, id, nombre_completo, anio_nacimiento, genero, codigo_postal)

    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo = fila['id']
      nombre = fila['Full Name']
      fecha_nac = fila['year of birth']
      perso_genero = fila['Gender']
      cod_postal = fila['Zip Code']
      personax = Persona(nombre_completo=nombre, anio_nacimiento=fecha_nac, genero=perso_genero, codigo_postal=cod_postal, id=codigo)
      lista_respuesta.append(personax)
    return lista_respuesta


  def write_df(self, df): 
    # Este método recibe el dataframe de personas y agrega la persona
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no la agrega y devuelve un error.
    new_row = {
      "Full Name": self.nombre_completo,
      "year of birth": self.anio_nacimiento,
      "Gender": self.genero,
      "Zip Code": self.codigo_postal,
    }
    return DataFrameHelper.append_row(df, new_row, self.id)


  def remove_from_df(self, df, df_usuarios, df_trabajadores):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Realiza el borrado si:
    # - Todas las propiedades del objeto coinciden con la entrada en el DF. Caso contrario levanta un excepción.
    # - No existe un usuario para la persona a borrar. Caso contrario levanta un excepción.
    # - No existe un trabajador para la persona a borrar. Caso contrario levanta un excepción.
    
    if (self.id in df_usuarios["id"].values):
      raise Exception('Existe un usuario para la persona a borrar.')
    
    if (self.id in df_trabajadores["id"].values):
      raise Exception('Existe un trabajador para la persona a borrar.')
    
    # mediante el get aseguramos que coincidan los valores de las propiedades, salvo nombre_completo que utiliza un contains
    personas = self.get_from_df(df, self.id, self.nombre_completo, [self.anio_nacimiento, self.anio_nacimiento], self.genero, self.codigo_postal)
    for persona in personas:
      if persona.nombre_completo == self.nombre_completo:
        return df[df.id != self.id]
    
    # no hay coincidencia entre todas las propiedades
    raise Exception('La persona no coincide con ninguna de las existentes en el dataframe.')


  @classmethod
  def get_stats(cls, df, anio_nacimiento=None, genero=None, codigo_postal=None):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # - fecha de nacimiento
    # - generos
    # - codigo postal
    # Las estadísticas son:
    # - Persona más vieja
    # - Persona más joven
    # - Total de personas
    # - Cantidad de personas por año de nacimiento
    # - Cantidad de personas por género
    
    datos_filtrados = Persona.__filter_df__(df, anio_nacimiento=anio_nacimiento, genero=genero, codigo_postal=codigo_postal)

    stats = {  
      "persona_mas_vieja": datos_filtrados['Full Name'].iloc[datos_filtrados['year of birth'].argmin()],
      "persona_mas_joven": datos_filtrados['Full Name'].iloc[datos_filtrados['year of birth'].argmax()],
      "total_personas": len(datos_filtrados.index),
      "personas_por_anio": datos_filtrados.groupby('year of birth').size(),
      "personas_por_genero": datos_filtrados.groupby('Gender').size()
    }
    return stats

