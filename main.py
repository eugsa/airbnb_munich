import pandas as pd
import config
import transform
import visualization as vis

def init():
    listings_df = pd.read_csv(config.DATASET_PATH + config.LISTING_FILENAME)
    transform.transform_listings(listings_df)
    clean_df = transform.get_cleaned_df(listings_df)
    return clean_df

def generate_all_plots():
    clean_df = init()
    vis.listing_count_per_neighborhood_plot(clean_df)
    vis.host_count_per_listing_amount_plot(clean_df)
    vis.bedroom_count_per_price_plot(clean_df)
    vis.price_plot(clean_df)
    vis.price_per_neigborhood_plot(clean_df)

def generate_listing_count_per_neighborhood_plot():
    clean_df = init()
    vis.listing_count_per_neighborhood_plot(clean_df)

def generate_host_count_per_listing_amount_plot():
    clean_df = init()
    vis.host_count_per_listing_amount_plot(clean_df)

def generate_bedroom_count_per_price_plot():
    clean_df = init()
    vis.bedroom_count_per_price_plot(clean_df)

def generate_price_plot():
    clean_df = init()
    vis.price_plot(clean_df)

def generate_price_per_neigborhood_plot():
    clean_df = init()
    vis.price_per_neigborhood_plot(clean_df)
