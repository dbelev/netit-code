import sys
import requests
from bs4 import BeautifulSoup as bs
import re



class Crawler:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        r = requests.get(self.url)
        if r.ok:
            r.encoding = r.apparent_encoding
            return r.text
        else:
            raise Exception('Page was not found')

    def get_page_numbers(self):
            r = requests.get(self.url)
            r.encoding = r.apparent_encoding
            content = r.text
            soup = bs(content, 'html.parser')
            span_element = soup.find_all("span", class_="pageNumbersInfo")
            pattern = re.compile(r'(\d+)<')
            res = pattern.search(str(span_element[1]))
            number_of_pages = res.group(1)
            return number_of_pages

    def get_publication(self):
        pass


    def start(self):
        content  = self.get_html
#		self.get_publication()