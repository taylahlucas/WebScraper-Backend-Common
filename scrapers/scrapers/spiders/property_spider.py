import scrapy
from bs4 import BeautifulSoup
from ..user_agents import get_ua
 # TODO: Can't import scrapers
class PropertySpider(scrapy.Spider):
    name = 'properties'
    allowed_domains = ["onthemarket.com"]
    current_company = ''

    # handle_httpstatus_list = [403]
    # user_agent = get_ua()

    headers = {
        'User-Agent': get_ua(),
        'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    }
    # url = 'https://au.finance.yahoo.com/quote/MQG.AX?p=MQG.AX'
    url = 'https://www.onthemarket.com/for-sale/property/manchester-city-centre/?view=grid'
    # url = 'https://www.zoopla.co.uk/for-sale/property/manchester/?q=Manchester&search_source=home&chain_free=true&added='

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        yield scrapy.http.Request(self.url, headers=self.headers)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        [x.extract() for x in soup.find_all('script')]
        [x.extract() for x in soup.find_all('style')]
        [x.extract() for x in soup.find_all('meta')]
        [x.extract() for x in soup.find_all('noscript')]

        # TODO: Use xpath builder response.xpath
        print("HERE: ", str(soup.find('mb-0 text-lg font-bold text-denim price')))

        # with open('results.html', 'w') as f:
        #     f.write(str(soup.find_all('price'))

        return None