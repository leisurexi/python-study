# author: leisurexi
# date: 2021/1/23
# file name: multi_thread.py
# 多线程版本打印一些网站内容


import concurrent.futures
import requests
import time


def download_one(url):
    resp = requests.get(url)
    print(f'Read {len(resp.content)} from {url}')


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map(download_one, sites)

        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()


def main():
    sites = ['https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.sina.com.cn/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'http://www.ifeng.com/',
             'http://www.ce.cn/',
             'https://news.baidu.com/',
             'http://www.people.com.cn/',
             'http://www.ce.cn/',
             'https://news.163.com/',
             'http://news.sohu.com/',
             'https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.sina.com.cn/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'http://www.ifeng.com/',
             'http://www.ce.cn/',
             'https://news.baidu.com/',
             'http://www.people.com.cn/',
             'http://www.ce.cn/',
             'https://news.163.com/',
             'http://news.sohu.com/',
             'https://www.baidu.com/',
             'https://pypi.org/',
             'https://www.sina.com.cn/',
             'https://www.163.com/',
             'https://news.qq.com/',
             'http://www.ifeng.com/',
             'http://www.ce.cn/',
             'https://news.baidu.com/',
             'http://www.people.com.cn/',
             'http://www.ce.cn/',
             'https://news.163.com/',
             'http://news.sohu.com/'
             ]

    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print(f'Download {len(sites)} sites in {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
