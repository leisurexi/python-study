# author: leisurexi
# date: 2021/1/26
# file name: with.py
# 巧用上下文管理器和 with 语句

class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()


class Foo:
    def __init__(self):
        print('__init__ called')

    def __enter__(self):
        print('__enter__ called')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ called')
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_val: {exc_val}')
            print(f'exc_tb: {exc_tb}')
            print('exception handled')
        return True


if __name__ == '__main__':
    with FileManager('test.txt', 'w') as f:
        f.write('hello world')

    with Foo() as obj:
        raise Exception('exception raised').with_traceback(None)
