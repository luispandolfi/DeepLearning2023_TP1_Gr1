import pytest
from persona import Persona
from usuario import Usuario
from datetime import datetime


@pytest.fixture(scope="class")
def df_usuarios():
  df_personas = Persona.create_df_from_csv("./csv_files/personas.csv")
  return Usuario.create_df_from_csv("./csv_files/usuarios.csv", df_personas)


class TestUsuario:

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