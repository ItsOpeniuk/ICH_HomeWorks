import requests
from bs4 import BeautifulSoup

def get_html(url):
    link_list = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.attrs.get('href')
                if href and href.startswith('http'):
                    link_list.append(href)
        else:
            print('Error:', response.status_code)
    except requests.ConnectionError:
        print('Connection Error')
    return link_list

if __name__ == '__main__':
    link = input('Enter your web site: ')
    links = get_html(link)
    print(links)
