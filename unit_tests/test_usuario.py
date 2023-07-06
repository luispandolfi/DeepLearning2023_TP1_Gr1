import pytest
from usuario import Usuario


@pytest.fixture(scope="class")
def df_usuarios():
  return Usuario.create_df_from_csv("../csv_files/usuarios.csv")

class TestUsuario:

    def test_get_solo_id(self, df_usuarios):
        usuarios = Usuario.get_from_df(df_usuarios, 17)
        assert len(usuarios) == 1
        usuario = usuarios[0]
        assert usuario.id == 17
        assert usuario.ocupacion == "programmer"
        assert usuario.fecha_alta == "1998-01-18 23:20:19"