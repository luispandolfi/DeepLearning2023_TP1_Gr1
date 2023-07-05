from pelicula import Pelicula
import helper


if __name__ == "__main__":
  print("Hola, aca arranco")


lista_total = helper.load_all("csv_files/personas.csv","csv_files/trabajadores.csv","csv_files/usuarios.csv","csv_files/peliculas.csv","csv_files/scores.csv")
data_frame_pelicula = lista_total[3]

#print(data_frame_pelicula)

#lista_respuesta = pelicula.get_from_df(data_frame_pelicula, id=None, nombre = None, anios = None, generos = None):
#lista_respuesta = Pelicula.get_from_df(data_frame_pelicula, anios=['1998-03-10','1998-03-20'])
lista_respuesta = Pelicula.get_from_df(data_frame_pelicula, generos=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


print(lista_respuesta)

