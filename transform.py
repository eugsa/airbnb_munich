from config import *
import pandas as pd

def transform_listings(df):
  df.dropna(subset=COLUMNS_DROP_NA, inplace=True)
  df.drop(columns=COLUMNS_DROP, inplace=True)
  df.rename(columns=COLUMNS_RENAME, inplace=True)

def get_cleaned_df(df):
  clean_df = df[['id', 'host_id', 'neighborhood_name']]
  return clean_df

def get_listing_count_per_neighborhood_df(df):
  clean_df = df.groupby(by='neighborhood_name').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  return clean_df

def get_host_count_per_listing_amount_df(df):
  listing_count_per_host_df = df.groupby(by='host_id').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  host_count_per_listing_amount_df = listing_count_per_host_df.groupby(by='listing_count').agg({'host_id': 'count'}).rename(columns={'host_id': 'host_count'}).reset_index()
  host_count_per_listing_amount_df = host_count_per_listing_amount_df.sort_values(by='listing_count', ascending=False)
  return host_count_per_listing_amount_df