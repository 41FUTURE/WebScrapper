
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import itertools
import sys

# Adjust the path to your actual path
chrome_driver_path = "Path to your chromedriver.exe"

# Initializing the webdriver
driver = webdriver.Chrome(chrome_driver_path)

# URL to scrape
url = "https://www.amazon.co.jp/s?k=Pokemon+Fit+Plush&language=ja_JP&currency=JPY"

driver.get(url)

# Create or open a CSV file
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'ASIN', 'URL'])  

    # Simple text-based animation
    animation_frames = ['(^_^)', '(-_-)', '(^_^)', '(-_-)']
    frame_iterator = itertools.cycle(animation_frames)

    # Loop to go through multiple pages
    while True:
        # Print Pokemon animation frame
        sys.stdout.write(next(frame_iterator))
        sys.stdout.flush()
        sys.stdout.write('\r')
        
        # Extract product details
        products = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, "span.a-text-normal").text
                asin = product.get_attribute("data-asin")
                url = product.find_element(By.CSS_SELECTOR, "a.a-link-normal").get_attribute("href")  # Extracted the URL
                writer.writerow([title, asin, url]) 
                print(f"\nFound product: {title}, {asin}, {url}")  
            except NoSuchElementException:
                print("An error occurred while extracting product details")

        # Check if the "Next" button is available
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            next_button.click()
            time.sleep(2)  # Adjust the sleep time as needed
        except NoSuchElementException:
            print("No more pages left")
            break

# Close the Chrome window
driver.quit()
