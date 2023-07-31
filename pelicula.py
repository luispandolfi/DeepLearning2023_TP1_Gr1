from dataFrameHelper import DataFrameHelper
import pandas as pd
import matplotlib.pyplot as plt


class Pelicula:

  def __init__(self, nombre, fecha_estreno, generos, id = None):
    self.nombre = nombre
    self.fecha_estreno = fecha_estreno
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
  def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
    # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
    # id: id
    # nombre: nombre de la película
    # anios: [desde_año, hasta_año]
    # generos: [generos]
    
    # Validar el campo antes de filtrar
    #datos_filtrados = df_mov[(df_mov["Release Date"] > '1997-03-10')&(df_mov["Release Date"] < '1998-03-20')]

    datos_filtrados = df_mov
    
    if anios != None:
      if len(anios) == 2:
        datos_filtrados = datos_filtrados[datos_filtrados["Release Date"] >= f'{anios[0]}' & datos_filtrados["Release Date"] <= f'{anios[1]}']
      else:
        raise ValueError("la lista anios debe tener largo 2")
      
    if nombre != None:
      datos_filtrados = datos_filtrados[datos_filtrados['Name'].str.contains(nombre,case=False)]

    if id !=  None:
      datos_filtrados = datos_filtrados[(datos_filtrados["id"] == id)]

    if generos!= None and len(generos) == 19:
      aux = 0
      lista_generos = ['unknown','Action','Adventure','Animation',"Children's",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
      for num in generos:
        datos_filtrados = datos_filtrados.query(f'{lista_generos[aux]} == {num}')
        aux += 1

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
      "name": self.nombre,
      "Release Date": self.fecha_estreno,
    }
    for key in df.keys()[-19:]:
      if key in self.generos:
        new_row[f"{key}"] = 1
      else:
        new_row[f"{key}"] = 0

    return DataFrameHelper.append_row(df, new_row, self.id)


  def remove_from_df(self, df):
    # Borra del DataFrame el objeto contenido en esta clase.
    # Para realizar el borrado todas las propiedades del objeto deben coincidir
    # con la entrada en el DF. Caso contrario imprime un error.
    peliculas = self.get_from_df(df, self.id, self.nombre, [self.fecha_estreno, None], self.generos)
    if (len(peliculas) > 0):
      return df[df.id != self.id]
    else:
      raise Exception('La película no coincide con ninguna de las existentes en el dataframe.')


  @classmethod
  def get_stats(cls, df_mov, anios=None, generos=None):
    # Este class method imprime una serie de estadísticas calculadas sobre
    # los resultados de una consulta al DataFrame df_mov. 
    # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
    # anios: [desde_año, hasta_año]
    # generos: [generos]
    # Las estadísticas son:
    # - Datos película más vieja
    # - Datos película más nueva
    # - Bar plots con la cantidad de películas por año/género.
    
    
    """
    print("La pelicula más vieja es ", df_mov['Name'].iloc[df_mov['Release Date'].argmin()])
    print("La pelicula más nueva es ", df_mov['Name'].iloc[df_mov['Release Date'].argmax()])
    
    fig, ax = plt.subplots()
    df_mov = df_mov.sort_values('Release Date')
    df_aux=df_mov['Release Date'].dt.year.value_counts(sort=False)
    df_aux.plot(ax=ax, kind='bar', xlabel='año', ylabel='# peliculas')
    
    fig2, ax2 = plt.subplots()
    df_aux2=df_mov.sum(axis=0, numeric_only=True )[-19:]
    df_aux2=df_aux2.sort_values()
    print(df_aux2)
    df_aux2.plot(ax=ax2, kind='bar', xlabel='genero', ylabel='# peliculas')
    plt.show()
    """
    datos_filtrados = df_mov
    #filtrar con funcion
     
    stats={
      
      "pelicula_mas_vieja": datos_filtrados['Name'].iloc[datos_filtrados['Release Date'].argmin()],
      "pelicula_mas_nueva": datos_filtrados['Name'].iloc[datos_filtrados['Release Date'].argmax()], 
      "relase_date_plots": datos_filtrados['Release Date'].dt.year.value_counts(sort=False),
      "gender_plots": datos_filtrados.sum(axis=0, numeric_only=True )[-19:]

    }
    return stats