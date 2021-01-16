# author: leisurexi
# date: 2021-01-15 21:43
# 练习1：你能否把 NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），
# 而 output.txt 不会很大（意味着重复的单词数量很多）。提示：你可能需要每次读取一定长度的字符串，进行处理，然后再读取下一次的。
# 但是如果单纯按照长度划分，你可能会把一个单词隔断开，所以需要细心处理这种边界情况。

import re


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
    text = ''
    with open('in.txt', 'r') as fin:
        text += fin.readline()

    word_and_freq = parse(text)

    with open('out.txt', 'w') as fout:
        for word, freq in word_and_freq:
            fout.write(f'{word} {freq}\n')
