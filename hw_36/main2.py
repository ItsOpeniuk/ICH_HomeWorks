import requests
from bs4 import BeautifulSoup

def find_title(url: str, title_level: str):
    try:
        page = requests.get(url)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, 'html.parser')
        if title_level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            titles = soup.find_all(title_level)
            return titles
        else:
            raise ValueError('Invalid title level!')
    except requests.ConnectionError:
        print('Connection failed!')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    url = input('Enter the url: ')
    title = input('Enter title level (h1, h2, h3, h4, h5, h6): ')
    print(find_title(url, title))
