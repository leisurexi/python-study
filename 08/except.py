# author: leisurexi
# date: 2021-01-16 13:49
# 异常处理示例


# 自定义异常类型
class MyInputError(Exception):
    # 自定义异常类型的初始化
    def __init__(self, value):
        self.value = value

    # 自定义异常类型的 string 表达形式
    def __str__(self):
        return f'{repr(self.value)} is invalid input'


if __name__ == '__main__':
    # try:
    #     s = input('please enter two numbers separated by comma: ')
    #     num1 = int(s.split(',')[0].strip())
    #     num2 = int(s.split(',')[1].strip())
    # except ValueError as err:
    #     print(f'Value Error: {err}')
    # except IndexError as err:
    #     print(f'Index Error: {err}')
    # except Exception as err:
    #     print(f'Exception: {err}')

    try:
        raise MyInputError(1)
    except MyInputError as err:
        print(f'error: {err}')
