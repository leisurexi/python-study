# author: leisurexi
# date: 2021-01-20 23:19

import time
import asyncio


async def crawl_page(url):
    print(f'crawling {url}')
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print(f'OK {url}')


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        # await task
        await asyncio.gather(*tasks)
    # for url in urls:
    #     await crawl_page(url)


if __name__ == '__main__':
    start = time.perf_counter()
    # main(['url_1', 'url_2', 'url_3', 'url_4'])
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
    print(f'函数运行了 {time.perf_counter() - start} s')