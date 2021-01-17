# author: leisurexi
# date: 2021-01-17 23:27
# python 装饰器

def get_message(message):
    return f'Got a message {message}'


def root_call(func, message):
    print(func(message))


# 嵌套函数
def func(message):
    def get_message(message):
        print(f'Got a message {message}')

    return get_message(message)


# 闭包
def func_closure():
    def get_message(message):
        print(f'Got a message {message}')

    return get_message


# 装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


# 自定义参数表示装饰器内部函数被执行的次数
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


# @my_decorator
@repeat(4)
def greet(message):
    print(message)


# 类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of calls is: {self.num_calls}')
        return self.func(*args, **kwargs)


@Count
def class_decorator_example():
    print('class_decorator_example')


if __name__ == '__main__':
    # send_message = get_message
    # send_message('hello world')

    root_call(get_message, 'hello world')

    func('hello world')

    send_message = func_closure()
    send_message('hello world')

    # greet = my_decorator(greet)
    # greet()

    greet('hello world')

    class_decorator_example()
    class_decorator_example()
