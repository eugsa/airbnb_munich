import pandas as pd
import matplotlib.pyplot as plt
from config import *

def transform_listings(df):
  df.dropna(subset=COLUMNS_DROP_NA, inplace=True)
  df.drop(columns=COLUMNS_DROP, inplace=True)
  df.rename(columns=COLUMNS_RENAME, inplace=True)

def get_cleaned_df(df):
  clean_df = df[['id', 'host_id', 'neighborhood_name']]
  return clean_df

# Visualization
def listing_count_per_neighborhood_plot(df):
  count_per_neigh = df.groupby(by='neighborhood_name').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  print(count_per_neigh.sample(n=10))
  plt.bar(count_per_neigh.neighborhood_name, count_per_neigh.listing_count)
  plt.xticks(rotation=90)
  plt.show()

listings_df = pd.read_csv(DATASET_PATH + FILENAME)
transform_listings(listings_df)
clean_df = get_cleaned_df(listings_df)

listing_count_per_neighborhood_plot(clean_df)

# Manual check
# print(clean_df.columns)
# print(clean_df.sample(n=10))
