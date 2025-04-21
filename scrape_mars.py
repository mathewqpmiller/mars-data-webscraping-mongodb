import requests
from bs4 import BeautifulSoup

def scrape_nasa_news():
    url = "https://redplanetscience.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send request with custom headers
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve NASA news, status code: {response.status_code}")
        return None

    # Check if there's a redirect
    if response.history:
        print(f"Request was redirected. Final URL: {response.url}")
    
    # Print the raw HTML to verify it's being retrieved
    print(response.text[:1000])  # Print the first 1000 characters to avoid overwhelming output
    
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        article = soup.find("div", class_="list_text")
        title = article.find("div", class_="content_title").get_text()
        paragraph = article.find("div", class_="article_teaser_body").get_text()

        return {"news_title": title, "news_paragraph": paragraph}
    except AttributeError as e:
        print(f"Error parsing NASA news: {e}")
        return None

# Call the function
scrape_nasa_news()