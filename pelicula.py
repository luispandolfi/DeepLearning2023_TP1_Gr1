import pandas as pd


class Pelicula:
  def __init__(self, nombre, anio, generos, id = None):
      self.nombre = nombre
      self.anio = anio
      self.generos = generos
      self.id = id
  def __repr__(self):
      strings = list()
      strings.append(f'Nombre: {self.nombre}')
      strings.append(f'Fecha de estreno: {self.fecha_estreno}')
      strings.append(f'Géneros: {self.generos}')
      strings.append(f'ID: {self.id}')
      return "\n".join(strings)
        # Este método debe imprimir la información de esta película.  

  @classmethod    
  def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
  # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
  # id: id
  # nombre: nombre de la película
  # anios: [desde_año, hasta_año]
  # generos: [generos]
  # Validar el campo antes de filtrar
    #datos_filtrados = df_mov[(df_mov["Release Date"] > '1997-03-10')&(df_mov["Release Date"] < '1998-03-20')]
    datos_filtrados = df_mov[(df_mov["Release Date"] > f'{anios[0]}') & (df_mov["Release Date"] < f'{anios[1]}')]
    datos_filtrados = datos_filtrados[datos_filtrados['Name'].str.contains(nombre,case=False)]

    lista_respuesta = []
    for indice, fila in datos_filtrados.iterrows():
      codigo = fila['id']
      nombre = fila['Name']
      fecha = fila['Release Date']
      list_genero = [fila['unknown'],fila['Action'],fila['Adventure'],fila['Animation'],fila["Children's"],fila['Comedy'],fila['Crime'],fila['Documentary'],fila['Drama'],fila['Fantasy'],fila['Film-Noir'],fila['Horror'],fila['Musical'],fila['Mystery'],fila['Romance'],fila['Sci-Fi'],fila['Thriller'],fila['War'],fila['Western']]
      
      peliculax = Pelicula(nombre,fecha,list_genero,codigo)
      lista_respuesta.append(peliculax)
    return lista_respuesta
  


  def write_df(self, df_mov): 
    # Este método recibe el dataframe de películas y agrega la película
    # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
    # id ya existe, no la agrega y devuelve un error.
    new_row={
      "name": self.nombre,
      "Release Date": self.anio,
    }
    
    if self.id==None:
      new_row["id"]=df_mov.id.max() +1
    elif self.id in df_mov.id.values:
      ex = ValueError()
      ex.strerror="Id no válido, ya se encuentra en el DataFrame"
      raise ex
    else:
      new_row["id"]=self.id
      
    for key in df_mov.keys()[-19:]:
      if key in self.generos:
        new_row[f"{key}"]=1
      else:
        new_row[f"{key}"]=0

    df_dictionary = pd.DataFrame([new_row])
    df_mov = pd.concat([df_mov, df_dictionary], ignore_index=True)
    return df_mov