# author: leisurexi
# date: 2021/1/23
# file name: single_thread.py
# 单线程版本打印一些网站内容

import requests
import time


def download_one(url):
    resp = requests.get(url)
    print(f'Read {len(resp.content)} from {url}')


def download_all(sites):
    for site in sites:
        download_one(site)


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
