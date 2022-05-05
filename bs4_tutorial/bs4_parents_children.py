import os

from bs4 import BeautifulSoup

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), './quotes.html')

    with open(file_path, 'r') as f:
        result = BeautifulSoup(f, 'html.parser')

    quotes = []

    for quote in result.select('div.quote'):
        print([e.string for e in quote.children if e.string not in ['\n', None]])