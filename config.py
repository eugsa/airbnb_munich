import pandas as pd
import matplotlib.pyplot as plt

# Source files
DATASET_PATH = '../data/'
FILENAME = 'listings.csv'

# Data cleaning
COLUMNS_DROP_NA = ['host_name']
COLUMNS_DROP = [
  'neighbourhood',
  'neighbourhood_group_cleansed',
  'host_neighbourhood',
  'amenities',
  'scrape_id',
  'last_scraped',
  'source',
  'picture_url'
]
COLUMNS_RENAME = {
  'neighborhood_overview': 'neighborhood_description',
  'neighbourhood_cleansed': 'neighborhood_name'
}