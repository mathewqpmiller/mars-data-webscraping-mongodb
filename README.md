
<p align="center">
  <img src="BrandingImages/MongoDB_Readme_CoverImage2.png" alt="Project Cover" width="1200" height="auto"/>
</p>


This project demonstrates the use of web scraping techniques to collect and analyze data from various Mars-related sources, leveraging MongoDB for data storage. The project was built using Python libraries like BeautifulSoup, Splinter, and Pandas to scrape key information about Mars.

## What to Look For in a Good Web Scraping Target:
Publicly accessible (no login required)
Stable HTML structure
No major anti-scraping protection (e.g., heavy JavaScript rendering)
Content-rich (articles, datasets, tables, etc.)

### Popular Alternatives for Web Scraping Projects:
Here are a few beginner-friendly sites that are often used for scraping practice:
#### Books to Scrape
Great for scraping product listings, prices, and ratings.
No JavaScript, clean layout.
Popular for e-commerce-style scraping.
#### Quotes to Scrape
Simple layout with quotes and authors.
Designed for practice.
Easy pagination and search functions.
#### IMDB (Top 250 Movies)
You can scrape movie titles, ranks, ratings.
More challenging due to structure but doable.
Use with care; follow IMDB’s robots.txt.
#### Real Python Blog
Can scrape recent articles, titles, and summaries.
Good for educational content and blog-style structure.
#### Hacker News
Lightweight and perfect for scraping tech headlines and vote counts.
Static site with minimal styling.

1. Markdown Cells: Use markdown cells to write descriptions, explanations, and comments as you progress through the project. This helps make your notebook more readable and organized.
2. Testing and Debugging: You can test different parts of the project in separate cells. For example, test the request, check for redirects, inspect the raw HTML, etc. Then, debug it step by step.
3. Visualizing Data: Once you extract and clean your data, you can use libraries like matplotlib, seaborn, or plotly to visualize any data or trends. You can create different cells for the visualization portion of the project.
4. Creating the Web App: Once your scraping is working fine, you can use frameworks like Flask or Dash to build your web app within the same notebook environment.

Example Notebook Structure:
Cell 1: Import Libraries (requests, BeautifulSoup)
Cell 2: Define the scrape_nasa_news() function
Cell 3: Call the function to scrape and display the data
Cell 4: Process or Clean the scraped data if needed
Cell 5: Visualize or perform additional analyses
Cell 6: Add Flask/Dash code for the web app (when ready)

By structuring your project in Jupyter Notebook this way, you can keep the workflow smooth and easy to debug.

Part 1: Scraping
Write and test scraping code for:
NASA Mars News – news_title, news_p
JPL Featured Image – featured_image_url
Mars Facts – convert table to HTML string
Mars Hemispheres – list of dicts: {"title": ..., "img_url": ...}
Use Splinter, BeautifulSoup, and Pandas in a Jupyter Notebook.

## Step 1: Scraping the Latest NASA Mars News

To begin this project, I used web scraping techniques to collect the most recent Mars-related news from [NASA’s Mars News site](https://redplanetscience.com). The goal of this step was to extract both the **headline** and a **teaser paragraph** from the top article on the homepage.

### Tools Used
- Python
- BeautifulSoup for parsing HTML
- Selenium for browser automation
- ChromeDriver to simulate browser interactions

### Key Steps
1. Launched a browser session using Selenium.
2. Navigated to the NASA Mars News site.
3. Waited for the content to fully load.
4. Parsed the HTML with BeautifulSoup.
5. Located the first news title and paragraph using class selectors.

### Outcome
The scraper successfully returns:
- The **latest news title** (e.g., *NASA's Perseverance Rover Begins the Hunt for Ancient Life*).
- A short **teaser summary** of the article.

This scraped content becomes the first component of the unified Mars data dictionary later inserted into MongoDB and rendered in the final Flask web app.

## Step 2: JPL Featured Mars Image

In this step, I scraped the **current featured Mars image** from the [Jet Propulsion Laboratory (JPL) Space Images site](https://spaceimages-mars.com/). The objective was to retrieve the full-resolution URL of the featured image that is visually highlighted on the homepage.

### Tools Used
- Python
- BeautifulSoup
- Splinter (browser automation layer built on top of Selenium)

### Key Steps
1. Launched a browser session using Splinter.
2. Visited the JPL Mars Space Images site.
3. Parsed the HTML content using BeautifulSoup.
4. Located the featured image thumbnail within a specific `img` tag.
5. Extracted the `src` attribute and constructed the absolute URL.

### Outcome
The scraper returns the **full URL** of the currently featured Mars image. This image is later used as a key visual asset in the final web dashboard.

## Step 3: Mars Facts Table

This step involved scraping a comparative facts table about Mars and Earth from the [Galaxy Facts website](https://galaxyfacts-mars.com/). The goal was to transform tabular data into an HTML format for embedding later in the Flask app.

### Tools Used
- Python
- Pandas
- BeautifulSoup (implicitly, via `read_html`)

### Key Steps
1. Utilized Pandas’ `read_html()` method to scrape all HTML tables from the site.
2. Selected the first table, which compares Mars and Earth data.
3. Renamed columns and set the description column as the index.
4. Converted the cleaned DataFrame into an HTML table string using `.to_html()`.

### Outcome
The final output is a clean, responsive HTML string of the Mars–Earth comparison table, ready to be stored in MongoDB and rendered dynamically via Flask.

## Step 4: Mars Hemispheres

This step focused on scraping **high-resolution images and titles** for each of Mars' four hemispheres from the [USGS Astrogeology site](https://marshemispheres.com/).

### Tools Used
- Python
- BeautifulSoup
- Splinter

### Key Steps
1. Visited the main page and extracted links to each hemisphere’s detail page.
2. Iterated through the pages using Splinter.
3. On each page, parsed the HTML with BeautifulSoup.
4. Retrieved the title and full-resolution image URL from the downloads section.
5. Stored each hemisphere’s data in a dictionary and appended to a list.

### Outcome
The final output is a list of dictionaries containing:
- `title`: Name of the hemisphere
- `img_url`: Link to the high-resolution image

This data is later stored in MongoDB and integrated into the dashboard interface.


Part 2: Web App with Flask + MongoDB
Move scraping logic into a Python script scrape_mars.py with a function called scrape().
Set up Flask app with:
/scrape route → runs the function and saves to MongoDB
/ route → loads data from Mongo and renders index.html
Display all data in your HTML template.

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Make sure your template will display a page even if the data is empty. Use the following as a guide for what the final product should look like, but feel free to create your own design. 

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:
1. The Jupyter Notebook containing the scraping code used.
2. Screenshots of your final application.
3. Submit the link to your new repository to BootCampSpot.
4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.
* Use Bootstrap to structure your HTML template.
=======
<p align="center">
  <img src="BrandingImages/MongDB_Readme_CoverImage2.png" alt="Project Cover" width="700"/>
</p>

This project demonstrates the use of web scraping techniques to collect and analyze data from various Mars-related sources, leveraging MongoDB for data storage. The project was built using Python libraries like BeautifulSoup, Splinter, and Pandas to scrape key information about Mars.

## What to Look For in a Good Web Scraping Target:
Publicly accessible (no login required)
Stable HTML structure
No major anti-scraping protection (e.g., heavy JavaScript rendering)
Content-rich (articles, datasets, tables, etc.)

### Popular Alternatives for Web Scraping Projects:
Here are a few beginner-friendly sites that are often used for scraping practice:
#### Books to Scrape
Great for scraping product listings, prices, and ratings.
No JavaScript, clean layout.
Popular for e-commerce-style scraping.
#### Quotes to Scrape
Simple layout with quotes and authors.
Designed for practice.
Easy pagination and search functions.
#### IMDB (Top 250 Movies)
You can scrape movie titles, ranks, ratings.
More challenging due to structure but doable.
Use with care; follow IMDB’s robots.txt.
#### Real Python Blog
Can scrape recent articles, titles, and summaries.
Good for educational content and blog-style structure.
#### Hacker News
Lightweight and perfect for scraping tech headlines and vote counts.
Static site with minimal styling.

1. Markdown Cells: Use markdown cells to write descriptions, explanations, and comments as you progress through the project. This helps make your notebook more readable and organized.
2. Testing and Debugging: You can test different parts of the project in separate cells. For example, test the request, check for redirects, inspect the raw HTML, etc. Then, debug it step by step.
3. Visualizing Data: Once you extract and clean your data, you can use libraries like matplotlib, seaborn, or plotly to visualize any data or trends. You can create different cells for the visualization portion of the project.
4. Creating the Web App: Once your scraping is working fine, you can use frameworks like Flask or Dash to build your web app within the same notebook environment.

Example Notebook Structure:
Cell 1: Import Libraries (requests, BeautifulSoup)
Cell 2: Define the scrape_nasa_news() function
Cell 3: Call the function to scrape and display the data
Cell 4: Process or Clean the scraped data if needed
Cell 5: Visualize or perform additional analyses
Cell 6: Add Flask/Dash code for the web app (when ready)

By structuring your project in Jupyter Notebook this way, you can keep the workflow smooth and easy to debug.

Part 1: Scraping
Write and test scraping code for:
NASA Mars News – news_title, news_p
JPL Featured Image – featured_image_url
Mars Facts – convert table to HTML string
Mars Hemispheres – list of dicts: {"title": ..., "img_url": ...}
Use Splinter, BeautifulSoup, and Pandas in a Jupyter Notebook.

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
```

### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},

    https://astrogeology.usgs.gov/search/map/valles_marineris_hemisphere_enhanced
    https://astrogeology.usgs.gov/search/map/cerberus_hemisphere_enhanced
    https://astrogeology.usgs.gov/search/map/schiaparelli_hemisphere_enhanced
    https://astrogeology.usgs.gov/search/map/syrtis_major_hemisphere_enhanced

    # The Actual Website Where the Images Reside
    https://astrogeology.usgs.gov/search/map/mars-viking-global-products
]
```

Part 2: Web App with Flask + MongoDB
Move scraping logic into a Python script scrape_mars.py with a function called scrape().
Set up Flask app with:
/scrape route → runs the function and saves to MongoDB
/ route → loads data from Mongo and renders index.html
Display all data in your HTML template.

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Make sure your template will display a page even if the data is empty. Use the following as a guide for what the final product should look like, but feel free to create your own design. 

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:
1. The Jupyter Notebook containing the scraping code used.
2. Screenshots of your final application.
3. Submit the link to your new repository to BootCampSpot.
4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.
* Use Bootstrap to structure your HTML template.
>>>>>>> refs/remotes/origin/main
