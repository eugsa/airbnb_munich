clean:
	rm ./figures/*.png

generate_all_plots:
	python -c "from main import generate_all_plots; generate_all_plots()"

generate_listing_count_per_neighborhood_plot:
	python -c "from main import generate_listing_count_per_neighborhood_plot; generate_listing_count_per_neighborhood_plot()"

generate_host_count_per_listing_amount_plot:
	python -c "from main import generate_host_count_per_listing_amount_plot; generate_host_count_per_listing_amount_plot()"

generate_bedroom_count_per_price_plot:
	python -c "from main import generate_bedroom_count_per_price_plot; generate_bedroom_count_per_price_plot()"

generate_price_plot:
	python -c "from main import generate_price_plot; generate_price_plot()"