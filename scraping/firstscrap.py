import requests
from parsel import Selector

class Scrap:
    URL = 'https://knews.kg/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    XPATH = '//div[@class="td-module-thumb"]/a/@href'

    def parse_data(self):
        text = requests.get(url=self.URL,headers=self.HEADERS).text
        tree = Selector(text=text)
        links = tree.xpath(self.XPATH).extract()
        return links

if __name__ == '__main__':
    scrapper = Scrap()
    scrapper.parse_data()