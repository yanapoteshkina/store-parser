import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


BASE_URL = "https://arbuz.kz/ru/almaty/catalog/cat/225172-kofe_i_kakao#/"
HEADERS = {"User-Agent": UserAgent().random}
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items = soup.find_all("article", {"class": "product-item product-card"})

            for item in items:
                price = item.find("b").text.strip()
                title = item.find("a", {"class": "product-card__title"})
                link = title.get("href")


                print(f"Название: {title.text.strip()} \nЦена: {price} \nИсточник: https://arbuz.kz{link} \n \n \n")



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())