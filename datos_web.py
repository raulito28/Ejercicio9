import requests
from lxml import html

class GetWebData:
    def __init__(self, url):
        self.url = url
    def get_data(self, parser):
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        data = tree.xpath(parser)
        return data
