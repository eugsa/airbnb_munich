# airbnb_munich
Cleaning, tranformation and visualization exercise with python and pandas. Parallel exploration of the data through a Jupyter notebook.

How to generate the plots: refer to the Makefile or read the documentation below.
Example:
`make generate_listing_count_per_neighborhood_plot`

When you use a command, the plot will be generated from the data through ETL, and will save the plot as a file in the `figures/` folder. When executing the command, the complete path will be printed in the terminal.

## Data
The data comes from the website https://insideairbnb.com/ which is a project scraping the data from Airbnb to make it available, and show the impact of the company on the local communities.

The data on the website is already split per city, and for this project, I'm focusing on the data for Munich.

## Goals
In this present project, the data is explored in the Jupyter notebook (`airbnb_munich.ipynb`). After that, the results of interesting findings are reported in the code via a simple ETL process.

The main goal is to understand the scope of the presence of Airbnb in the city of Munich.

## Plots

### Listing count per neighborhood
Command: `make generate_listing_count_per_neighborhood_plot`

Questions:
- How many listing are per neighborhood?
- What are the neighborhood with the most Airbnbs? And those with the least?

### Host count per listing amount
Command: `make generate_host_count_per_listing_amount_plot`

Questions:
- What is the tendency in terms of how many listings hosts have? What is the average?
- What are the highest count of listings hosts have?

### Bedroom count per price
Command: `make generate_bedroom_count_per_price_plot`

Questions:
- How is the distribution of beds according to the price? Is there a correlation? 

### Price distribution
Command: `make generate_price_plot`

Questions:
- How are the prices distributed? Given bins of 50$, and having a maximum of 400+$
- In which bin lie the most prices in?

### Price per neigborhood
Command: `make generate_price_per_neigborhood_plot`

Questions:
- What would be the distribution of prices per neighborhood? Given bins of 50$, and having a maximum of 400+$
- What neighborhood have the most expensive prices? And the least expensive prices?