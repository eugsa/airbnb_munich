from config import *
from transform import *

def get_filepath(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, FIGURES_PATH + filename)
    return filepath

def saving_figure(plt, filename):
    filepath = get_filepath(filename)
    plt.savefig(filepath)
    print(f"See saved figure as { filepath }.png")
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
    bedroom_count_per_price_df = drop_price_na(df)

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

def price_plot(df):
    df = drop_price_na(df)
    df = get_price_range(df)

    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)
    plt.title('Price categories plot')
    plt.xlabel('Bins')
    plt.ylabel('Amount')

    filename = inspect.stack()[0][3]
    saving_figure(plt, filename)

def calculate_percentage(row, df):
    total_count = df[df['neighborhood_name'] == row['neighborhood_name']].shape[0]
    range_count = df[(df['neighborhood_name'] == row['neighborhood_name']) & (df['price_range'] == row['price_range'])].shape[0]
    return (range_count / total_count) * 100

def price_per_neigborhood_plot(df):
    df = drop_price_na(df)
    df = get_price_range(df)

    grouped = df.groupby(['neighborhood_name', 'price_range'], observed=True).size().unstack(fill_value=0)
    percentage_df = grouped.div(grouped.sum(axis=1), axis=0) * 100
    percentage_df.plot(kind='barh', stacked=True)
    plt.title('Price per neighborhood plot')
    plt.xlabel('Percentage of prices')
    plt.ylabel('Neighborhoods')
    plt.subplots_adjust(left=0.4)

    filename = inspect.stack()[0][3]
    saving_figure(plt, filename)
