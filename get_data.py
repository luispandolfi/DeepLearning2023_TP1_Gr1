import pandas as pd
from datetime import datetime

###########################
#   CARGA DE DATOS        # 
###########################

def load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores):
  #Código de Carga
  df_personas = pd.read_csv(file_personas)
  df_trabajadores = pd.read_csv(file_trabajadores)
  df_usuarios = pd.read_csv(file_usuarios)
  df_peliculas = pd.read_csv(file_peliculas)
  df_scores = pd.read_csv(file_scores)
  
  #correcciones de datos
  df_personas = clean_personas(df_personas)
  df_trabajadores = clean_trabajadores(df_trabajadores, df_personas)
  df_usuarios = clean_usuarios(df_usuarios, df_personas)
  df_peliculas = clean_peliculas(df_peliculas)
  df_scores = clean_scores(df_scores, df_usuarios, df_peliculas)
  
  return df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores

def clean_personas(df):
  df = df.dropna()
  df = df.drop_duplicates(subset = ["id"])
  df = df.loc[df["Gender"].isin(["M", "F"])]
  return df

def clean_trabajadores(df, df_personas):
  df = df.dropna()
  df["Start Date"] = pd.to_datetime(df["Start Date"], format="%Y-%m-%d")
  id_personas = set(df_personas["id"])
  df = df.loc[df["id"].isin(id_personas)]
  return df

def clean_usuarios(df, df_personas):
  df = df.dropna()
  df["Active Since"] = pd.to_datetime(df["Active Since"], format="%Y-%m-%d %H:%M:%S")
  id_personas = set(df_personas["id"])
  df = df.loc[df["id"].isin(id_personas)]
  return df

def clean_peliculas(df):
  df = df.dropna()
  df["Release Date"] = pd.to_datetime(df["Release Date"], format="%d-%b-%Y")
  return df

def clean_scores(df, df_usuarios, df_peliculas):
  df = df.dropna()
  df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %H:%M:%S")
  #el user_id exista en usuarios
  id_usuarios = set(df_usuarios["id"])
  df = df.loc[df["user_id"].isin(id_usuarios)]
  #el movie_id exista en peliculas
  id_peliculas = set(df_peliculas["id"])
  df = df.loc[df["movie_id"].isin(id_peliculas)]
  #rating entre 1 y 5
  df = df.loc[df["rating"].isin([1,2,3,4,5])]
  return df

###########################
#      CLASE PELICULA     # 
###########################
class Pelicula:
    def __init__(self, nombre, fecha_estreno, generos, id = None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
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
    def write_df(self, df_mov, overwrite = False):
        pass
        # Este método recibe el dataframe de películas y agrega la película
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
        # id ya existe, no la agrega y devuelve un error, salvo que overwrite esté 
        # en True, en cuyo caso, sobreescribe.
    @classmethod
    def create_df_from_csv(cls, filename):
        df_mov = pd.read_csv(filename)
        df_mov["Release Date"] = df_mov["Release Date"].fillna('1-Jan-1900')
        df_mov["Release Date"] = df_mov["Release Date"].apply(lambda x: datetime.strptime(x, '%d-%b-%Y'))
        # Este class method recibe el nombre de un archivo csv, valida su 
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        ###
        #Código
        ###
        return df_mov

    @classmethod    
    def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
        df_mod.query('')
        pass
        # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
        # id: id
        # nombre: nombre de la película
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        return lista_peliculas

    def get_stats(cls,df_mov, anios=None, generos=None):
        pass
        # Este class method imprime una serie de estadísticas calculadas sobre
        # los resultados de una consulta al DataFrame df_mov. 
        # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        # Las estadísticas son:
        # - Datos película más vieja
        # - Datos película más nueva
        # - Bar plots con la cantidad de películas por año/género.
    def remove_from_df(self, df_mov):
        pass
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.




###########################
#   COMIENZA MI PROGRAMA  # 
###########################

if __name__ == "__main__":
  print("Hola, aca arranco")


lista_total = load_all("personas.csv","trabajadores.csv","usuarios.csv","peliculas.csv","scores.csv")
data_frame_pelicula = lista_total[3]
#print(data_frame_pelicula.head(3))
#print(data_frame_pelicula[['Name','Release Date']])

datos_filtrados = data_frame_pelicula[(data_frame_pelicula["Release Date"] > '1997-03-10')&(data_frame_pelicula["Release Date"] < '1998-03-20')]
datos_filtrados = datos_filtrados[datos_filtrados['Name'].str.contains('on',case=False)]


x = 0
lista_respuesta = []
list_genero = []
for indice, fila in datos_filtrados.iterrows():
   peliculax = 'pelicula' + str(x)
   print(fila['id'],fila['Name'],fila["Release Date"])
   codigo = fila['id']
   nombre = fila['Name']
   fecha = fila['Release Date']
   list_genero = [fila['unknown'],fila['Action'],fila['Adventure'],fila['Animation'],fila["Children's"],fila['Comedy'],fila['Crime'],fila['Documentary'],fila['Drama'],fila['Fantasy'],fila['Film-Noir'],fila['Horror'],fila['Musical'],fila['Mystery'],fila['Romance'],fila['Sci-Fi'],fila['Thriller'],fila['War'],fila['Western']]
   
   peliculax = Pelicula(nombre,fecha,list_genero,codigo)
   lista_respuesta.append(peliculax)


print("-----------------------")
print("Voy a imprimir la lista respuesta")
print(lista_respuesta)
