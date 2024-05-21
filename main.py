from config import *
from transform import *
from visualization import *

def init():
  listings_df = pd.read_csv(DATASET_PATH + FILENAME)
  transform_listings(listings_df)
  clean_df = get_cleaned_df(listings_df)
  return clean_df

def generate_listing_count_per_neighborhood_plot():
  clean_df = init()
  print(clean_df.sample(n=5))
  listing_count_per_neighborhood_plot(clean_df)