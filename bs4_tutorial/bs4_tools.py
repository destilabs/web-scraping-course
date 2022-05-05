import os

from bs4 import BeautifulSoup

import pandas as pd

from common.helpers import get_element_by_selector
from common.output import print_warning

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), './quotes.html')

    with open(file_path, 'r') as f:
        result = BeautifulSoup(f, 'html.parser')

    quotes = []

    print_warning("Selecting first div with class 'quote'")
    print(next(iter(result.select('div.quote')), None))
    print_warning("Finding first div with class 'quote'")
    print(result.find('div', class_ = 'quote'))

    for quote in result.find_all('div', class_ = 'quote'):
        quote_dict = {}

        quote_dict['text'] = get_element_by_selector(quote, 'span.text')
        quote_dict['author'] = get_element_by_selector(quote, 'small.author')
        quote_dict['tags'] = get_element_by_selector(quote, 'div.tags a.tag')

        quotes.append(quote_dict)

    df = pd.DataFrame(quotes)

    print(df)