# airbnb_munich
In this project, I want to look at the AirBnB data for the city of Munich: how present are AirBnB apartments in Munich, how many people do it recreationally and how many do it more professionally (amount of listing per host), and how the prices are influenced and distributed.

I perform data exploration in a Jupyter notebook (`airbnb_munich.ipynb`), and implement a data pipeline to clean the data and extract the data. I implemented Makefile commands so that the visualizations can be reupdated with new data if needed. Makefile commands are listed below for each plot.

Example:
`make generate_listing_count_per_neighborhood_plot`

When you use a command, the plot will be generated from the data through ETL, and will save the plot as a file in the `figures/` folder. When executing the command, the complete path will be printed in the terminal.

## Data
The data comes from the website https://insideairbnb.com/ which is a project scraping the data from Airbnb to make it available, and show the impact of the company on the local communities.

The data on the website is already split per city, and for this project, I'm focusing on the data for Munich.

## Plots

### Listing count per neighborhood
Command: `make generate_listing_count_per_neighborhood_plot`

Questions:
- How many listing are per neighborhood?
- What are the neighborhood with the most Airbnbs? And those with the least?

![listing_count_per_neighborhood_plot](https://github.com/eugsa/airbnb_munich/blob/main/figures/listing_count_per_neighborhood_plot.png)

### Host count per listing amount
Command: `make generate_host_count_per_listing_amount_plot`

Questions:
- What is the tendency in terms of how many listings hosts have? What is the average?
- What are the highest count of listings hosts have?

![host_count_per_listing_amount_plot](https://github.com/eugsa/airbnb_munich/blob/main/figures/host_count_per_listing_amount_plot.png)

### Bedroom count per price
Command: `make generate_bedroom_count_per_price_plot`

Questions:
- How is the distribution of beds according to the price? Is there a correlation? 

![bedroom_count_per_price_plot](https://github.com/eugsa/airbnb_munich/blob/main/figures/bedroom_count_per_price_plot.png)

### Price distribution
Command: `make generate_price_plot`

Questions:
- How are the prices distributed? Given bins of 50$, and having a maximum of 400+$
- In which bin lie the most prices in?

![price_plot](https://github.com/eugsa/airbnb_munich/blob/main/figures/price_plot.png)

### Price per neigborhood
Command: `make generate_price_per_neigborhood_plot`

Questions:
- What would be the distribution of prices per neighborhood? Given bins of 50$, and having a maximum of 400+$
- What neighborhood have the most expensive prices? And the least expensive prices?

![price_per_neigborhood_plot](https://github.com/eugsa/airbnb_munich/blob/main/figures/price_per_neigborhood_plot.png)