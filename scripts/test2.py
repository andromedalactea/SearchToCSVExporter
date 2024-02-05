from googlesearch import search
import csv

# Define la palabra clave para la búsqueda
keyword = "clean company"

# Inicia la búsqueda en Google y guarda solo el primer resultado
first_company_url = None
for url in search(keyword, stop=5):
    first_company_url = url
    print(url)
    #break  # Sal del bucle después de obtener el primer resultado

# Verifica si se encontró una URL
if first_company_url:
    # Define el nombre del archivo CSV donde se guardarán los resultados
    filename = "company_urls.csv"
    
    # Abre el archivo CSV en modo de escritura
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribe los encabezados de las columnas
        writer.writerow(['Keyword', 'URL'])
        # Escribe la palabra clave y la URL encontrada en el archivo
        writer.writerow([keyword, first_company_url])
    
    print(f"URL '{first_company_url}' for keyword '{keyword}' saved to {filename}")
else:
    print(f"No URL found for keyword '{keyword}'.")
