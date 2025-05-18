from scrape_mars import scrape
from pymongo import MongoClient

def load_to_mongo():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.mars_db  # Create/use a database called 'mars_db'
    collection = db.mars_collection  # Create/use a collection called 'mars_data'

    # Clear existing data to prevent duplicates
    collection.delete_many({})

    # Scrape fresh data
    mars_data = scrape()

    # Insert the scraped data
    collection.insert_one(mars_data)

    print("Data loaded into MongoDB successfully.")

if __name__ == "__main__":
    load_to_mongo()
