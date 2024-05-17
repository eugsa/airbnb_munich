import pandas as pd

dataset_path = '../data/'
filename = 'listings.csv'
listings_df = pd.read_csv(dataset_path + filename)
print(listings_df.columns)