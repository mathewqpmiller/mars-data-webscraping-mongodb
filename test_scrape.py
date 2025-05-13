from scrape_mars import scrape

if __name__ == "__main__":
    data = scrape()
    for key, value in data.items():
        print(f"{key}:\n{value}\n")
