import bs4

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and 
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
    </body>
</html>
"""

parsed_html = bs4.BeautifulSoup(html, 'html.parser')

links_text = [link.text for link in parsed_html.select('a')]

print(links_text)