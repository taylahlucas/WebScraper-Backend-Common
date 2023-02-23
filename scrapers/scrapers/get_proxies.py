import time
from os.path import exists
import json
from spiders.proxy_spider import ProxySpider
from scrapy.crawler import CrawlerProcess
from user_agents import get_ua

# Runs the proxy spider and generates a list of usable proxies
def crawl_proxy_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': get_ua(),
        'ROBOTSTXT_OBEY': True,
        'LOG_LEVEL': 'INFO'
    })
    process.crawl(ProxySpider)
    process.start()


def get_proxies():
    crawl_proxy_spider()

    while not exists('ip_addresses.json'):
        time.sleep(1)

    with open('ip_addresses.json', 'r') as file:
        ip_addresses = json.load(file)

    # IP addresses contains list of proxies ready to use


if __name__ == '__main__':
    get_proxies()
