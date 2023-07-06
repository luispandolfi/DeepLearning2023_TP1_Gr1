import pytest
from persona import Persona
from datetime import datetime


@pytest.fixture(scope="class")
def df_personas():
  return Persona.create_df_from_csv("./csv_files/personas.csv")


class TestPersona:
  
  def test_write_id_none(self, df_personas):
    cantidad_inicial = len(df_personas.id)
    persona = Persona("Lorem Ipsum", datetime(1970, 6, 29), "F", 12345)
    df = persona.write_df(df_personas)
    # el df original queda incambiado
    assert len(df_personas.id) == cantidad_inicial
    # la persona agregada se almacena en el df resultado
    assert len(df.id) == cantidad_inicial + 1