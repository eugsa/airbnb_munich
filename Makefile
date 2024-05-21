clean:
	rm ./figures/*.png

generate_listing_count_per_neighborhood_plot:
	python -c "from main import generate_listing_count_per_neighborhood_plot; generate_listing_count_per_neighborhood_plot()"