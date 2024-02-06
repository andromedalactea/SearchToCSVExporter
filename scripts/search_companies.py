from googlesearch import search
import csv

def save_company_links_to_csv(keyword, num_links, filename='output_fiiles/companies_links_japan.csv'):
    # Converts the keyword to a search query in Japanese, focusing on companies and factories in Japan
    search_query = f'{keyword} company or factory'

    # Initializes a counter for the results
    count = 0

    # Opens the CSV file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Writes the column headers
        writer.writerow(['Keyword', 'URL'])

        # Performs the search on Google with Japanese preferences
        for url in search(search_query, stop=num_links):
            # Writes the result into the CSV file
            writer.writerow([keyword, url])
            # Increments the counter
            count += 1
            # Checks if the desired number of links has been reached
            if count >= num_links:
                break

# Example of use
keyword = "hardware"  # "PC hardware" in Japanese
num_links = 10

save_company_links_to_csv(keyword, num_links)
