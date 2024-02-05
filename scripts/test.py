from googlesearch import search
import csv

def save_company_links_to_csv(keyword, num_links, filename='companies_links_japan.csv'):
    # Converts the keyword to a search query in Japanese, focusing on companies and factories in Japan
    search_query = f'{keyword} の会社 や 工場 -最高 -トップ -ランキング -ウィキペディア -クオラ -リンクトイン -グラスドア -インディード -イェルプ -ブルームバーグ -フォーブス -フォーチュン -マネー -インク -ビジネスインサイダー -クランチベース -ズームインフォ -クラフト'

    # Initializes a counter for the results
    count = 0

    # Opens the CSV file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Writes the column headers
        writer.writerow(['Keyword', 'URL'])

        # Performs the search on Google with Japanese preferences
        for url in search(search_query, stop=num_links, lang='ja', country='JP'):
            # Writes the result into the CSV file
            writer.writerow([keyword, url])
            # Increments the counter
            count += 1
            # Checks if the desired number of links has been reached
            if count >= num_links:
                break

# Example of use
keyword = "PC ハードウェア"  # "PC hardware" in Japanese
num_links = 5

save_company_links_to_csv(keyword, num_links)
