from pelicula import Pelicula
from persona import Persona
from trabajador import Trabajador
from usuario import Usuario
import helper


if __name__ == "__main__":
  print("Hola, aca arranco")


#lista_total = helper.load_all("csv_files/personas.csv","csv_files/trabajadores.csv","csv_files/usuarios.csv","csv_files/peliculas.csv","csv_files/scores.csv")
#data_frame_persona = lista_total[0]

#print(data_frame_pelicula)

#lista_respuesta = pelicula.get_from_df(data_frame_pelicula, id=None, nombre = None, anios = None, generos = None):
#lista_respuesta = Pelicula.get_from_df(data_frame_pelicula, anios=['1998-03-10','1998-03-20'])
#lista_respuesta = Pelicula.get_from_df(data_frame_pelicula, generos=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#lista_respuesta = Persona.get_from_df(data_frame_persona, anio_nacimiento=[1978, 1980])

dataframe_all = helper.load_all("csv_files/personas.csv","csv_files/trabajadores.csv","csv_files/usuarios.csv","csv_files/peliculas.csv","csv_files/scores.csv")
data_frame_pelicula = dataframe_all[3]

lista_respuesta = Pelicula.get_from_df(data_frame_pelicula)

# trabajador1 = Trabajador(id=None, fecha_alta='2023-07-15',puesto='IT',categoria='A', horario_trabajo='8-17')
# print(data_frame_trabajador)
# nuevo_dataframe = trabajador1.write_df(data_frame_trabajador)

#usuario1 = Usuario(id=None, fecha_alta='2023-08-07', ocupacion='ingeniero')
#nuevo_dataframe_usuario = usuario1.write_df(data_frame_usuario)

pelicula1 = Pelicula(nombre='Barbie', fecha_estreno='2023-08-01', generos=[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
nuevo_data_frame_pelicula = pelicula1.write_df(data_frame_pelicula)

print(nuevo_data_frame_pelicula)
#print(lista_respuesta)

