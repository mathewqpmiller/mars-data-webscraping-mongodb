from flask import Flask, render_template
from flask_pymongo import PyMongo

# Initialize Flask app
app = Flask(__name__)

# Set up MongoDB connection (default is localhost)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Define home route
@app.route("/")
def index():
    # Retrieve Mars data from MongoDB
    mars_data = mongo.db.mars_collection.find_one()
    
    # Pass the data to the index.html template
    return render_template("index.html", mars=mars_data)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
