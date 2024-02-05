# SearchToCSVExporter

This repository contains a Python script designed to search for companies or factories related to a specified keyword in Japan. It focuses on extracting URLs from Google search results and saving them to a CSV file. The search queries are customized to filter out common non-company related results, ensuring a more targeted retrieval of company links.

## Features

- Search for company-related URLs using keywords.
- Customize the number of results you want to retrieve.
- Results are focused on Japanese companies and factories.
- Exclude common non-relevant sites from the search results to improve relevancy.
- Save the search results (URLs) to a CSV file for easy access and analysis.

## Requirements

To run this script, you will need Python installed on your system along with the following Python libraries:
- `googlesearch-python`
- `csv`

You can install the required library using pip:

```bash
pip install google
```
## Usage

To use this script, simply call the scripts.search_companies.py function with the desired keyword, number of links, and optionally, a filename for the CSV output.
```
keyword = "desired keyword in Japanese"
num_links = number_of_links_you_want_to_retrieve
save_company_links_to_csv(keyword, num_links, 'output_filename.csv')
```

### Example
```python
save_company_links_to_csv("PC ハードウェア", 5)
```
This will search for "PC hardware" related companies in Japan and save the first 5 results to companies_links_japan.csv.

## Customization

You can customize the search query by modifying the search_query variable in the script. The current configuration excludes several common domains to focus the search results on companies and factories in Japan.

## License
This project is open-sourced under the MIT license. See the LICENSE file for more details.