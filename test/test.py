import requests

URL = 'https://www.zoopla.co.uk/for-sale/details/63546508/?search_identifier=2016d1527d0c31dd9c6419d281c597d8'
page = requests.get(URL)

with open('result.html', 'w') as f:
    f.write(page.text)