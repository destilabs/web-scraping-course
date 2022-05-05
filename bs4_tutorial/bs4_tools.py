import os

from bs4 import BeautifulSoup

import pandas as pd

from common.helpers import get_element_by_selector

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), './quotes.html')

    with open(file_path, 'r') as f:
        result = BeautifulSoup(f, 'html.parser')

    quotes = []

    for quote in result.select('div.quote'):
        quote_dict = {}

        quote_dict['text'] = get_element_by_selector(quote, 'span.text')
        quote_dict['author'] = get_element_by_selector(quote, 'small.author')
        quote_dict['tags'] = get_element_by_selector(quote, 'div.tags a.tag')

        quotes.append(quote_dict)

    df = pd.DataFrame(quotes)

    print(df)