import pytest
from persona import Persona
from usuario import Usuario
from datetime import datetime


@pytest.fixture(scope="class")
def df_usuarios():
  df_personas = Persona.create_df_from_csv("./csv_files/personas.csv")
  return Usuario.create_df_from_csv("./csv_files/usuarios.csv", df_personas)


class TestUsuario:

  # TODO Revisar este caso, agregar un usuario con id None no deberia permitirse,
  # pues no hay forma de verificar que exista en personas
  def test_write_id_none(self, df_usuarios):
    cantidad_inicial = len(df_usuarios.id)
    usuario = Usuario(None, datetime(2023, 7, 9), "student")
    df = usuario.write_df(df_usuarios)
    # el df original queda incambiado
    assert len(df_usuarios.id) == cantidad_inicial
    # la persona agregada se almacena en el df resultado
    assert len(df.id) == cantidad_inicial + 1


  # TODO Revisar este caso, el write debe verificar que el id del usuario exista en personas
  def test_write_id_no_existente(self, df_usuarios):
    cantidad_inicial = len(df_usuarios.id)
    usuario = Usuario(None, datetime(2023, 7, 9), "student")
    df = usuario.write_df(df_usuarios)
    # el df original queda incambiado
    assert len(df_usuarios.id) == cantidad_inicial
    # la persona agregada se almacena en el df resultado
    assert len(df.id) == cantidad_inicial + 1


  def test_write_id_existente(self, df_usuarios):
    usuario = Usuario(11, datetime(2023, 7, 9), "student")
    with pytest.raises(ValueError):
      df = usuario.write_df(df_usuarios)


  def test_get_por_id(self, df_usuarios):
    usuarios = Usuario.get_from_df(df_usuarios, 17)
    assert len(usuarios) == 1
    usuario = usuarios[0]
    assert usuario.id == 17
    assert usuario.ocupacion == "programmer"
    assert usuario.fecha_alta.strftime("%Y-%m-%d %H:%M:%S") == "1998-01-18 23:20:19"


  def test_get_por_fecha(self, df_usuarios):
    fecha1 = datetime(1998, 1, 6, 0, 0, 0)
    fecha2 = datetime(1998, 1, 6, 23, 59, 59)
    usuarios = Usuario.get_from_df(df_usuarios, None, [fecha1, fecha2])
    assert len(usuarios) == 10
    for usuario in usuarios:
      assert usuario.fecha_alta.year == 1998
      assert usuario.fecha_alta.month == 1
      assert usuario.fecha_alta.day == 6