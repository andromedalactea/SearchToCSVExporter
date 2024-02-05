from googlesearch import search
import csv

def save_company_links_to_csv(keyword, num_links, filename='companies_links.csv'):
    # Adds 'company' to the keyword
    search_query = f'company or factories of {keyword} -best -top -ranking -wikipedia -quora -linkedin -glassdoor -indeed -yelp -bloomberg -forbes -fortune -money -inc -businessinsider -crunchbase -zoominfo -craft'    

    # Initializes a counter for the results
    count = 0

    # Opens the CSV file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Writes the column headers
        writer.writerow(['Keyword', 'URL'])

        # Performs the search on Google
        for url in search(search_query, stop=num_links):
            # Writes the result into the CSV file
            writer.writerow([keyword, url])
            # Increments the counter
            count += 1
            # Checks if the desired number of links has been reached
            if count >= num_links:
                break

# Example of use
keyword = "hardware for pc"
num_links = 5

save_company_links_to_csv(keyword, num_links)
