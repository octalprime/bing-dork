import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract

def get_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

def search_bing(query, num_results):
    url = 'https://www.bing.com/search'
    params = {'q': query, 'count': num_results}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    urls = [link.get('href') for link in links]
    return urls

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
