import pandas as pd
from config import *

def transform_listings(df):
  df.dropna(subset=COLUMNS_DROP_NA, inplace=True)
  df.drop(columns=COLUMNS_DROP, inplace=True)
  df.rename(columns=COLUMNS_RENAME, inplace=True)

def get_cleaned_df(df):
  clean_df = df[['id', 'host_id', 'neighborhood_name']]
  return clean_df

listings_df = pd.read_csv(DATASET_PATH + FILENAME)
transform_listings(listings_df)
clean_df = get_cleaned_df(listings_df)

# Manual check
print(clean_df.columns)
print(clean_df.sample(n=10))