from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import csv
import time

def save_company_links_to_csv_selenium(keyword, num_links, filename='output_files/companies_links_japan.csv', driver_path='C:/path/to/chromedriver.exe'):
    # Configura Selenium con el path al ChromeDriver
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    
    # Construye la URL de búsqueda
    # Construye la URL de búsqueda incluyendo los parámetros para desactivar el filtrado y la personalización
    search_query = f"{keyword} company or factory"
    base_url = "https://www.google.com/search?q="
    # Añade &filter=0&num=100&pws=0 para incluir resultados omitidos y desactivar personalización
    search_url = base_url + search_query.replace(" ", "+") + "&filter=0&num=100&pws=0"

    
    # Accede a la página de búsqueda
    driver.get(search_url)
    
    # Espera inicial para que la página cargue completamente
    time.sleep(0.5)
    
    links_collected = []
    attempts = 0

    while len(links_collected) < num_links and attempts < 10:
        # Encuentra y almacena los enlaces actuales
        result_divs = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result_div in result_divs:
            anchor = result_div.find_elements(By.CSS_SELECTOR, "a")
            if anchor:
                link = anchor[0].get_attribute("href")
                if link not in links_collected:
                    links_collected.append(link)
                    if len(links_collected) >= num_links:
                        break
        
        # Desplazamiento hacia abajo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)  # Espera a que carguen más resultados
        
        # Intenta hacer clic en el botón "Más resultados" si está presente
        try:
            more_results_button = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Más resultados')]")
            driver.execute_script("arguments[0].click();", more_results_button)
            time.sleep(0.2)  # Espera a que carguen los resultados adicionales
        except (NoSuchElementException, ElementClickInterceptedException):
            print("No se encontró el botón 'Más resultados' o no se pudo hacer clic en él, intentando de nuevo...")
            attempts += 1
        
    # Escribe los enlaces en el archivo CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyword', 'URL'])
        for link in links_collected:
            writer.writerow([keyword, link])
    
    # Cierra el navegador
    driver.quit()





# Ejemplo de uso
keyword = "clean"
num_links = 100
driver_path = 'ignore_files/chromedriver'  # Asegúrate de ajustar esto a la ubicación de tu ChromeDriver

start_time = time.time()
save_company_links_to_csv_selenium(keyword, num_links, driver_path=driver_path)
end_time = time.time()
total_time = end_time - start_time
print(f"Tiempo total de ejecución: {total_time} segundos.")
