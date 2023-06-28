import pandas as pd


class Pelicula:
  def __init__(self, nombre, anio, generos, id = None):
      self.nombre = nombre
      self.anio = anio
      self.generos = generos
      self.id = id
    
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