import httpx
import asyncio
from parsel import Selector

class Asyncscrap:
    URL = 'https://knews.kg/'
    HEADERS={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    XPATH='//div[@class="td-module-thumb"]/a/@href'

    async def get_page(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            response = await client.get(url=self.URL)
            links=await self.result(response=response)
            l=links
            return l

    async def result(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.XPATH).extract()
        # for link in links:
        #     print(link)
        return links


if __name__ == "__main__":
    scraper = Asyncscrap()
    asyncio.run(scraper.get_page())