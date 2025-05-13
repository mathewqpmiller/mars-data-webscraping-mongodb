from scrape_mars import scrape

mars_data = scrape()
for key, value in mars_data.items():
    print(f"\n{key.upper()}:\n{value}")
