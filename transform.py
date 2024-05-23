from config import *
import pandas as pd

def get_bathroom_count(bathroom_text):
    if isinstance(bathroom_text, float):
      return 0.0
    elif (len(bathroom_text.split(' ')) == 1 and bathroom_text.split(' ')[0].lower() == 'half-bath') or (len(bathroom_text.split(' ')) > 1 and bathroom_text.split(' ')[1].lower() == 'half-bath'):
      return 0.5
    return float(bathroom_text.split(' ')[0])

def get_bedroom_count(text):
  pattern = r'(\d+)\s*bedroom'
  match = re.search(pattern, text)
  if match:
    return int(match.group(1))
  else:
    return None

def get_bed_count(text):
  pattern = r'(\d+)\s*bed'
  match = re.search(pattern, text)
  if match:
    return int(match.group(1))
  else:
    return None

def extract_data_from_name(df):
  df['bathroom_count'] = df.bathrooms_text.apply(get_bathroom_count)
  df['bedroom_count'] = df.name.apply(get_bedroom_count)
  df.fillna({'bedroom_count': 1}, inplace=True)
  df['bed_count'] = df.name.apply(get_bed_count)
  df.fillna({'bed_count': 1}, inplace=True)
  return df

def transform_listings(df):
  df = extract_data_from_name(df)
  df.dropna(subset=COLUMNS_DROP_NA, inplace=True)
  df.drop(columns=COLUMNS_DROP, inplace=True)
  df.rename(columns=COLUMNS_RENAME, inplace=True)

def get_cleaned_df(df):
  columns = [
    'id', 'host_id', 'neighborhood_name',
    'bathroom_count', 'bedroom_count', 'bed_count'
  ]
  clean_df = df[columns]
  return clean_df

def get_listing_count_per_neighborhood_df(df):
  clean_df = df.groupby(by='neighborhood_name').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  return clean_df

def get_host_count_per_listing_amount_df(df):
  listing_count_per_host_df = df.groupby(by='host_id').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  host_count_per_listing_amount_df = listing_count_per_host_df.groupby(by='listing_count').agg({'host_id': 'count'}).rename(columns={'host_id': 'host_count'}).reset_index()
  host_count_per_listing_amount_df = host_count_per_listing_amount_df.sort_values(by='listing_count', ascending=False)
  return host_count_per_listing_amount_df