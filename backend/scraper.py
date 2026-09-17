from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
def scrape_website(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(separator="\n", strip=True)

        return text

    finally:
        driver.quit()