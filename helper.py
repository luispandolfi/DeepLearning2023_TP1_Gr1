import pandas as pd
from datetime import datetime

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