from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import csv
import time

def save_company_links_to_csv_selenium(keyword, num_links, filename='output_files/companies_links_japan.csv', driver_path='C:/path/to/chromedriver.exe'):
    # Configura Selenium con el path al ChromeDriver
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    
    # Construye la URL de búsqueda
    search_query = f"{keyword} company or factory"
    base_url = "https://www.google.com/search?q="
    search_url = base_url + search_query.replace(" ", "+")
    
    # Accede a la página de búsqueda
    driver.get(search_url)
    
    # Espera inicial para que la página cargue completamente
    time.sleep(3)
    
    links_collected = []
    while len(links_collected) < num_links:
        # Encuentra los resultados de la búsqueda actuales en la página
        result_divs = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result_div in result_divs:
            anchor = result_div.find_elements(By.CSS_SELECTOR, "a")
            if anchor:
                link = anchor[0].get_attribute("href")
                if link not in links_collected:
                    links_collected.append(link)
                    if len(links_collected) >= num_links:
                        break
        # Desplaza hacia abajo
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        # Espera para que carguen más resultados
        time.sleep(2)
    
    # Escribe los enlaces en el archivo CSV, sobrescribiendo el archivo existente
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyword', 'URL'])  # Escribe los encabezados de las columnas
        for link in links_collected[:num_links]:
            writer.writerow([keyword, link])
    
    # Cierra el navegador
    driver.quit()

# Ejemplo de uso
keyword = "hardware"
num_links = 1000
driver_path = 'ignore_files/chromedriver'  # Asegúrate de ajustar esto a la ubicación de tu ChromeDriver

save_company_links_to_csv_selenium(keyword, num_links, driver_path=driver_path)
