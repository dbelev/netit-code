import sys
import requests
from bs4 import BeautifulSoup as bs
from lib import crawler



base_url='https://www.imot.bg/pcgi/imot.cgi?act=3&slink=84mcel&f1='

parsed = crawler.Crawler(base_url + '1' )

number_of_pages = parsed.get_page_numbers()

print(number_of_pages)
