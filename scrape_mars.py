# Load All Dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape():
    # --- Part 1: NASA Mars News ---
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode if you don't need GUI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    news_title = ""
    news_p = ""

    try:
        url = "https://mars.nasa.gov/news/"
        driver.get(url)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hds-content-item-inner"))
        )

        articles = driver.find_elements(By.CLASS_NAME, "hds-content-item-inner")
        if articles:
            first_article = articles[0]
            news_title = first_article.find_element(By.CLASS_NAME, "hds-a11y-heading-22").text
            news_p = first_article.find_element(By.CLASS_NAME, "margin-top-0").text
    except Exception as e:
        print(f"Error scraping NASA Mars News: {e}")
    finally:
        driver.quit()

     # --- Part 2: JPL Featured Image ---
    featured_image_url = ""
    try:
        options = Options()
        options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        
        jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
        browser.get(jpl_url)

        html = browser.page_source
        page_soup = soup(html, 'html.parser')

        relative_image_path = page_soup.find('img', class_='headerimage fade-in')['src']
        base_url = jpl_url.rsplit('/', 1)[0]
        featured_image_url = f'{base_url}/{relative_image_path}'

        browser.quit()
    except Exception as e:
        print(f"Error scraping JPL image: {e}")
        if browser:
            browser.quit()

    # --- Part 3: Mars Facts ---
    html_table = ""
    try:
        url = 'https://space-facts.com/mars/'
        tables = pd.read_html(url)

        mars_df = tables[0]
        mars_df.columns = ['Description', 'Value']
        mars_df.set_index('Description', inplace=True)

        html_table = mars_df.to_html(classes="table table-striped", border=0)
    except Exception as e:
        print(f"Error scraping Mars facts: {e}")

  # --- Part 4: Mars Hemisphere Images ---
    hemisphere_data = []

    urls = [
        "https://astrogeology.usgs.gov/search/map/valles_marineris_hemisphere_enhanced",
        "https://astrogeology.usgs.gov/search/map/syrtis_major_hemisphere_enhanced",
        "https://astrogeology.usgs.gov/search/map/cerberus_hemisphere_enhanced",
        "https://astrogeology.usgs.gov/search/map/schiaparelli_hemisphere_enhanced"
    ]

    def get_hemisphere_data(url, driver):
        try:
            driver.get(url)
            time.sleep(3)
            title_element = driver.find_element(By.CLASS_NAME, "title")
            title = title_element.text.strip()
            image_element = driver.find_element(By.CLASS_NAME, "wide-image")
            relative_url = image_element.get_attribute("src")
            base_url = "https://astrogeology.usgs.gov"
            image_url = base_url + relative_url if relative_url.startswith("/") else relative_url

            return title, image_url
        except Exception as e:
            print(f"Error extracting data from {url}: {e}")
            return None, None

    # Reopen driver for hemisphere scraping
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for url in urls:
        print(f"Visiting: {url}")
        title, img_url = get_hemisphere_data(url, driver)
        if title and img_url:
            hemisphere_data.append({"title": title, "image_url": img_url})
        else:
            print(f"Failed to retrieve data from {url}")

    driver.quit()

    # --- Final Return ---
    return {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": html_table,
        "hemispheres": hemisphere_data
    }
    
if __name__ == "__main__":
    result = scrape()
    for key, value in result.items():
        print(f"\n{key}:\n{value}\n")
