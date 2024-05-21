from config import *

def listing_count_per_neighborhood_plot(df):
  count_per_neigh = df.groupby(by='neighborhood_name').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  print(count_per_neigh.sample(n=10))
  plt.bar(count_per_neigh.neighborhood_name, count_per_neigh.listing_count)
  plt.xticks(rotation=90)
  plt.show()