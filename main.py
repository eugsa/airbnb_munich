from config import *
from transform import *
from visualization import *

def init():
  listings_df = pd.read_csv(DATASET_PATH + LISTING_FILENAME)
  transform_listings(listings_df)
  clean_df = get_cleaned_df(listings_df)
  return clean_df

def generate_listing_count_per_neighborhood_plot():
  clean_df = init()
  listing_count_per_neighborhood_plot(clean_df)

def generate_host_count_per_listing_amount_plot():
  clean_df = init()
  host_count_per_listing_amount_plot(clean_df)

def generate_bedroom_count_per_price_plot():
  clean_df = init()
  bedroom_count_per_price_plot(clean_df)

def generate_price_plot():
  clean_df = init()
  price_plot(clean_df)