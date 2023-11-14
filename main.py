import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract

def get_domain(url):
    scheme = urlparse(url).scheme
    result = tldextract.extract(url)
    return f"{scheme}://{result.domain}.{result.suffix}"

def search_bing(query, num_results):
    url = 'https://www.bing.com/search'
    urls = []
    for i in range(0, num_results, 25):
        params = {'q': query, 'first': i+1}
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        page_urls = [link.get('href') for link in links if link.get('href') and link.get('href').startswith('http')]
        urls.extend(page_urls)
    return urls[:num_results]

def save_to_file(urls, filename):
    with open(filename, 'w') as f:
        for url in urls:
            f.write(f"{url}\n")

def main():
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results you want: "))
    urls = search_bing(query, num_results)
    domains = [get_domain(url) for url in urls]
    save_to_file(domains, 'results.txt')

if __name__ == "__main__":
    main()
