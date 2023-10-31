from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



def scraper(deal_type, city):
    url = f"https://www.zoopla.co.uk/{deal_type}/property/{city}/"
    # configure webdriver
    options = Options()
    options.headless = True  # hide GUI
    options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
    options.add_argument("start-maximized")  # ensure window is full-screen
    # configure chrome browser to not load images and javascript
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # wait for page to load
    element = WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="regular-listings"]'))
    )

    page_source = driver.page_source
    driver.quit()

    # Now, you can use parsel to extract data from the page source
    selector = Selector(text=page_source)

    # Extract the data as per your requirements, similar to the Scrapy spider
    data_dict = {}

    main_div = selector.css('div[data-testid="regular-listings"]')

    for listing in main_div.css('div[id^="listing_"]'):
        div_id = listing.css('::attr(id)').get()
        price = listing.css('p[data-testid="listing-price"]::text').get()
        name = listing.css('h2[data-testid="listing-title"]::text').get()
        address = listing.css('address::text').get()
        link = listing.css('a::attr(href)').get()

        # Store the data in the dictionary
        data_dict[div_id] = {
            "name": name,
            "price": price,
            "address": address,
            "link": link
        }