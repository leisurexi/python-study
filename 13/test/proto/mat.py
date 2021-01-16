# author: leisurexi
# date: 2021-01-16 22:15

class Matrix(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])
