from config import *

def listing_count_per_neighborhood_plot(df):
  count_per_neigh = df.groupby(by='neighborhood_name').agg({'id': 'count'}).rename(columns={'id': 'listing_count'}).reset_index()
  plt.figure(figsize=(12, 6))
  plt.bar(count_per_neigh.neighborhood_name, count_per_neigh.listing_count, zorder=2)
  plt.title('Listing count per neighborhood plot')
  plt.xlabel('Neihborhoods')
  plt.ylabel('Number of listings')
  plt.xticks(rotation=40, ha='right')
  plt.subplots_adjust(bottom=0.3)
  plt.grid(True, which='both', axis='y', linewidth=0.5, color='grey', zorder=0)
  plt.show()