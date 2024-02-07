from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from fake_useragent import UserAgent
import csv
import time
import random

def save_company_links_to_csv_selenium(keyword, num_links, filename='output_files/companies_links.csv', driver_path='C:/path/to/chromedriver.exe'):
    # Generates a random User-Agent
    ua = UserAgent()
    user_agent = ua.random
    
    # Sets Selenium options to use the generated User-Agent
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")
    
    # Configures Selenium with the path to ChromeDriver and the defined options
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    # Builds the search URL including parameters to disable personalization and filtering
    search_query = f"{keyword} companies or factories"
    base_url = "https://www.google.com/search?q="
    search_url = base_url + search_query.replace(" ", "+") + "&filter=0&num=2000&pws=0"
    
    # Accesses the search page
    driver.get(search_url)
    
    # Initial wait for the page to fully load
    # time.sleep(0.2)
    
    links_collected = []
    attempts = 0

    while len(links_collected) < num_links and attempts < 10:
        # Finds and stores the current links
        result_divs = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result_div in result_divs:
            anchor = result_div.find_elements(By.CSS_SELECTOR, "a")
            if anchor:
                link = anchor[0].get_attribute("href")
                if link not in links_collected:
                    links_collected.append(link)
                    if len(links_collected) >= num_links:
                        break
        
        # Scrolls down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(0.1)  # Waits for more results to load
        
        # Attempts to click the "More results" button if present
        try:
            more_results_button = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'More results')]")
            driver.execute_script("arguments[0].click();", more_results_button)
            # time.sleep(0.1)  # Waits for additional results to load
        except (NoSuchElementException, ElementClickInterceptedException):
            print("Trying again...")
            attempts += 1
        
    # Writes the links to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyword', 'URL'])
        for link in links_collected:
            writer.writerow([keyword, link])
    
    # Closes the browser
    driver.quit()

# Example usage
keyword = "clean"
num_links = 100
driver_path = 'ignore_files/chromedriver'  # Make sure to adjust this to your ChromeDriver location

start_time = time.time()
save_company_links_to_csv_selenium(keyword, num_links, driver_path=driver_path)
end_time = time.time()
total_time = end_time - start_time
print(f"Total execution time: {total_time} seconds.")
