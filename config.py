import pandas as pd
import matplotlib.pyplot as plt
import inspect
import os
import re
import math
import numpy as np

# Source files
DATASET_PATH = '../data/'
LISTING_FILENAME = 'listings.csv'

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
    'picture_url',
    'bathrooms',
    'bedrooms',
    'bathrooms_text'
]
COLUMNS_RENAME = {
    'neighborhood_overview': 'neighborhood_description',
    'neighbourhood_cleansed': 'neighborhood_name'
}

# Output files
FIGURES_PATH = './figures/'