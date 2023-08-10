from dataFrameHelper import DataFrameHelper
import pandas as pd


class Pelicula:

  GENEROS = ['unknown','Action','Adventure','Animation',"Children's",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']

  def __init__(self, nombre, fecha_estreno, generos, id = None):
    self.nombre = nombre
    self.fecha_estreno = pd.to_datetime(fecha_estreno, format="%Y-%m-%d")
    self.generos = generos
    self.id = id


  def __repr__(self):
    # Este método debe imprimir la información de esta película.

    return f'Nombre: {self.nombre}, Fecha de estreno: {self.fecha_estreno}, Genero: {self.generos}, ID: {self.id}\n'
    # strings = list()
    # strings.append(f'Nombre: {self.nombre}')
    # strings.append(f'Fecha de estreno: {self.fecha_estreno}')
    # strings.append(f'Géneros: {self.generos}')
    # strings.append(f'ID: {self.id}')
    # return "\n".join(strings)
  


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
    df["Release Date"] = pd.to_datetime(df["Release Date"], format="%d-%b-%Y")
    return df


  @classmethod
  def __filter_df__(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
    datos_filtrados = df_mov
    
    if anios != None:
      if len(anios) == 2:
        datos_filtrados = datos_filtrados[(datos_filtrados["Release Date"] >= f'{anios[0]}') & (datos_filtrados["Release Date"] <= f'{anios[1]}')]
      else:
        raise ValueError("la lista anios debe tener largo 2")
      
    if nombre != None:
      datos_filtrados = datos_filtrados[datos_filtrados['Name'].str.contains(nombre,case=False)]

    if id !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["id"] == id)]

    if generos!= None:
      for i in range(len(generos)):
        aux = 0
        lista_generos = ['unknown','Action','Adventure','Animation',"Children's",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
        for num in lista_generos:
          if generos[i].lower() == lista_generos[aux].lower():
            datos_filtrados = datos_filtrados[(datos_filtrados[lista_generos[aux]] == 1)]
          aux += 1
    return datos_filtrados


  @classmethod
  def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
    # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
    # - id: id
    # - nombre: nombre de la película
    # - anios: [desde_año, hasta_año]
    # - generos: lista de géneros
    
    datos_filtrados = Pelicula.__filter_df__(df_mov, id, nombre, anios, generos)

    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo = fila['id']
      nombre = fila['Name']
      fecha = fila['Release Date']
      list_genero = [fila['unknown'],fila['Action'],fila['Adventure'],fila['Animation'],fila["Children's"],fila['Comedy'],fila['Crime'],fila['Documentary'],fila['Drama'],fila['Fantasy'],fila['Film-Noir'],fila['Horror'],fila['Musical'],fila['Mystery'],fila['Romance'],fila['Sci-Fi'],fila['Thriller'],fila['War'],fila['Western']]
      
      peliculax = Pelicula(nombre,fecha,list_genero,codigo)
      lista_respuesta.append(peliculax)
    return lista_respuesta


  def write_df(self, df): 
    # Este método recibe el dataframe de películas y agrega la película
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no la agrega y devuelve un error.
    new_row = {
      "Name": self.nombre,
      "Release Date": self.fecha_estreno,
    }
    for key in df.keys()[-19:]:
      if key in self.generos:
        new_row[f"{key}"] = 1
      else:
        new_row[f"{key}"] = 0

    return DataFrameHelper.append_row(df, new_row, self.id)


  def remove_from_df(self, df, df_scores):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Realiza el borrado si:
    # - Todas las propiedades del objeto coinciden con la entrada en el DF. Caso contrario levanta un excepción.
    # - No existe un score para la pelicula a borrar. Caso contrario levanta un excepción.

    peliculas = self.get_from_df(df, self.id, self.nombre, [self.fecha_estreno, None], self.generos)
    if (len(peliculas) == 0):
      raise Exception('La película no coincide con ninguna de las existentes en el dataframe.')
    
    if (self.id in df_scores["movie_id"].values):
      raise Exception('Existen scores para la película a borrar.')
    
    return df[df.id != self.id]


  @classmethod
  def get_stats(cls, df, anios=None, generos=None):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # - anios: [desde_año, hasta_año]
    # - generos: lista de generos
    # Las estadísticas son:
    # - Película más vieja
    # - Película más nueva
    # - Total de películas
    # - Cantidad de películas por año de estreno
    # - Cantidad de películas por género
    
    datos_filtrados = Pelicula.__filter_df__(df, anios=anios, generos=generos)
     
    stats = {
      "pelicula_mas_vieja": datos_filtrados['Name'].iloc[datos_filtrados['Release Date'].argmin()],
      "pelicula_mas_nueva": datos_filtrados['Name'].iloc[datos_filtrados['Release Date'].argmax()],
      "total_peliculas": len(datos_filtrados.index),
      "peliculas_por_anio": datos_filtrados.groupby(datos_filtrados['Release Date'].dt.year).size(),
      "peliculas_por_genero": datos_filtrados.sum(axis=0, numeric_only=True )[-19:]
    }
    return stats