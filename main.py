import pandas as pd

dataset_path = '../data/'
filename = 'listings.csv'

def transform_listings(df):
  columns_drop_na = ['host_name']
  columns_drop = ['neighbourhood', 'neighbourhood_group_cleansed', 'host_neighbourhood']
  columns_rename = {
  'neighborhood_overview': 'neighborhood_description',
  'neighbourhood_cleansed': 'neighborhood_name'
  }

  df.dropna(subset=columns_drop_na, inplace=True)
  df.drop(columns=columns_drop, inplace=True)
  df.rename(columns=columns_rename, inplace=True)

listings_df = pd.read_csv(dataset_path + filename)
transform_listings(listings_df)