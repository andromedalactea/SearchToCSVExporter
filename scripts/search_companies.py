from googlesearch import search
import csv

def save_company_links_to_csv(keyword, num_links, filename='companies_links.csv'):
    # Agrega ' company' a la palabra clave
    search_query = f'company or factories of {keyword} -mejores -top -ranking -wikipedia -quora -linkedin -glassdoor -indeed -yelp -bloomberg -forbes -fortune -money -inc -businessinsider -crunchbase -zoominfo -craft'    

    # Inicializa un contador para los resultados
    count = 0

    # Abre el archivo CSV en modo de escritura
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribe los encabezados de las columnas
        writer.writerow(['Keyword', 'URL'])

        # Realiza la búsqueda en Google
        for url in search(search_query, stop=num_links):
            # Escribe el resultado en el archivo CSV
            writer.writerow([keyword, url])
            # Incrementa el contador
            count += 1
            # Verifica si se ha alcanzado el número deseado de links
            if count >= num_links:
                break

# Ejemplo de uso
keyword = "hardware for pc"
num_links = 5

save_company_links_to_csv(keyword, num_links)