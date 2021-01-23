# author: leisurexi
# date: 2021/1/22
# file name: sync_crawl.py
# 同步爬虫实现

import requests
import time
from bs4 import BeautifulSoup


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Referer': 'https://time.geekbang.org/column/article/101855',
        'Connection': 'keep-alive'
    }
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url, headers=headers).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = all_movies.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=headers).content
        soup_item = BeautifulSoup(response_item, 'lxml')

        img_tag = soup_item.find('img')

        print(f'{movie_name} {movie_date} {img_tag["src"]}')


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f'函数运行了 {time.perf_counter() - start} s')
