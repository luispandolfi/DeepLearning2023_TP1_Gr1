import pytest
from persona import Persona
from usuario import Usuario


@pytest.fixture(scope="class")
def df_usuarios():
  df_personas = Persona.create_df_from_csv("./csv_files/personas.csv")
  return Usuario.create_df_from_csv("./csv_files/usuarios.csv", df_personas)

class TestUsuario:

    def test_get_solo_id(self, df_usuarios):
        usuarios = Usuario.get_from_df(df_usuarios, 17)
        assert len(usuarios) == 1
        usuario = usuarios[0]
        assert usuario.id == 17
        assert usuario.ocupacion == "programmer"
        assert usuario.fecha_alta.strftime("%Y-%m-%d %H:%M:%S") == "1998-01-18 23:20:19"