# author: leisurexi
# date: 2021-01-15 21:02
# 标准输入示例

import re
import json


def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]', ' ', text)
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 取出空白单词
    word_list = filter(None, word_list)
    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] = 1
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt


if __name__ == '__main__':
    '''
    # 输入
    name = input('your name:')
    gender = input('you are a boy?(y/n)')

    welcome_str = 'Welcome to the matrix {prefix} {name}.'
    welcome_dic = {
        'prefix': 'Mr.' if gender == 'y' else 'Mrs',
        'name': name
    }

    print("authorizing...")
    print(welcome_str.format(**welcome_dic))

    # 类型转换
    a = input()
    b = input()
    print(f'a + b = {a + b}')
    print(f'type of a is {type(a)}, type of b is {type(b)}')
    print(f'a + b = {int(a) + int(b)}')
    '''

    # 文件输入与输出
    # with open('in.txt', 'r') as fin:
    #     text = fin.read()
    #
    # word_and_freq = parse(text)
    #
    # with open('out.txt', 'w') as fout:
    #     for word, freq in word_and_freq:
    #         fout.write(f'{word} {freq}\n')

    # json 示例
    params = {
        'symbol': '123456',
        'type': 'limit',
        'price': 123.4,
        'amount': 23
    }

    params_str = json.dumps(params)
    print('after json serialization')
    print(f'type of params_str = {type(params_str)}, params_str = {params}')

    original_params = json.loads(params_str)
    print('after json deserialization')
    print(f'type of original_params = {type(original_params)}， original_params = {original_params}')

    # 创建20个5M大小的文件
    # m =  5 * 1024 * 1024
    # for i in range(0, 20):
    #     with open(f'E:/tmp/{i + 1}.txt', 'w') as fout:
    #        for i in range(0, m):
    #            fout.write("a")

