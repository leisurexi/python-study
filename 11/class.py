# author: leisurexi
# date: 2021-01-16 15:23
# 面向对象

class Document:
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    # 对象初始化函数，类似于构造函数
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        # __ 开头的属性是私有属性
        self.__content = context

    # 成员函数
    def get_context_length(self):
        return len(self.__content)

    # 成员函数
    def intercept_context(self, length):
        self.__content = self.__content[:length]

    # 成员函数
    def get_context(self):
        return self.__content

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title, author, 'nothing')

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


if __name__ == '__main__':
    # harry_potter_book = Document('Harry Potter', 'J. K. Rowling',
    #                              '... Forever Do not believe any thing is capable of thinking independently ...')
    # print(harry_potter_book.title)
    # print(harry_potter_book.author)
    # print(harry_potter_book.get_context_length())
    #
    # harry_potter_book.intercept_context(10)
    # print(harry_potter_book.get_context_length())
    # print(harry_potter_book.get_context())

    empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')
    print(empty_book.get_context_length())
    print(empty_book.get_welcome('indeed nothing'))





