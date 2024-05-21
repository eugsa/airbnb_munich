from config import *
import pandas as pd

def transform_listings(df):
  df.dropna(subset=COLUMNS_DROP_NA, inplace=True)
  df.drop(columns=COLUMNS_DROP, inplace=True)
  df.rename(columns=COLUMNS_RENAME, inplace=True)

def get_cleaned_df(df):
  clean_df = df[['id', 'host_id', 'neighborhood_name']]
  return clean_df
