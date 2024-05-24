from config import *
from transform import *

def get_filepath(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, FIGURES_PATH + filename)
    return filepath

def saving_figure(plt, filename):
    filepath = get_filepath(filename)
    plt.savefig(filepath)
    print(f"See saved figure as { filepath }.")
    plt.close()

def listing_count_per_neighborhood_plot(df):
  listing_count_per_neighborhood_df = get_listing_count_per_neighborhood_df(df)
  
  plt.figure(figsize=(12, 6))
  plt.bar(listing_count_per_neighborhood_df.neighborhood_name, listing_count_per_neighborhood_df.listing_count, zorder=2)
  plt.title('Listing count per neighborhood plot')
  plt.xlabel('Neihborhoods')
  plt.ylabel('Number of listings')
  plt.xticks(rotation=40, ha='right')
  plt.subplots_adjust(bottom=0.3)
  plt.grid(True, which='both', axis='y', linewidth=0.5, color='grey', zorder=0)

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)

def host_count_per_listing_amount_plot(df):
  host_count_per_listing_amount_df = get_host_count_per_listing_amount_df(df)

  plt.bar(host_count_per_listing_amount_df.listing_count, host_count_per_listing_amount_df.host_count)
  plt.yscale('log')
  plt.title('Host count per listing amount')
  plt.xlabel('Amount of listings')
  plt.ylabel('Number of hosts')
  
  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)

def bedroom_count_per_price_plot(df):
  bedroom_count_per_price_df = get_bedroom_count_per_price_df(df)

  plt.scatter(
    bedroom_count_per_price_df.price,
    bedroom_count_per_price_df.bedroom_count
  )
  plt.xscale('log')
  plt.title('Bedroom count per price plot')
  plt.xlabel('Bedroom count')
  plt.ylabel('Price')

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)
