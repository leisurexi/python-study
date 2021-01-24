# author: leisurexi
# date: 2021/1/24
# file name: async_io.py
# Asyncio 示例

import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            print(f'Read {resp.content_length} from {url}')


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = ['https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'https://www.ifeng.com/',
             'https://www.ce.cn/',
             'https://news.baidu.com/',
             'https://www.people.com.cn/',
             'https://www.ce.cn/',
             'https://news.163.com/',
             'https://news.sohu.com/',
             'https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'https://www.ifeng.com/',
             'https://www.ce.cn/',
             'https://news.baidu.com/',
             'https://www.people.com.cn/',
             'https://www.ce.cn/',
             'https://news.163.com/',
             'https://news.sohu.com/',
             'https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'https://www.ifeng.com/',
             'https://www.ce.cn/',
             'https://news.baidu.com/',
             'https://www.people.com.cn/',
             'https://www.ce.cn/',
             'https://news.163.com/',
             'https://news.sohu.com/'
             ]

    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print(f'Download {len(sites)} sites in {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
