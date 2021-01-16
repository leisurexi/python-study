# author: leisurexi
# date: 2021-01-16 15:00
# 第一问：如果让你对一个字典，根据值进行由高到底的排序，该怎么做呢？以下面这段代码为例，你可以思考一下。 d = {'mike': 10, 'lucy': 2, 'ben': 30}


if __name__ == '__main__':
    d = {'mike': 10, 'lucy': 2, 'ben': 30}
    l = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(l)
