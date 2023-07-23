import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

from pyshorteners import Shortener

BASE_URL = "https://arbuz.kz/ru/almaty/catalog/cat/225177-frukty#/"
HEADERS = {"User-Agent": UserAgent().random}
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items = soup.find_all("article", {"class": "product-item product-card"})

            for item in items:
                price = item.find("b")
                title = item.find("a", {"class": "product-card__title"})
                link = title.get("href")

                # short_price = Shortener().tinyurl.short(f"https://arbuz.kz{link}")
                # print(short_price)

                #
                # print(f"TITLE: {title.text.strip()} | {price} | {short_price}")



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())