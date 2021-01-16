# author: leisurexi
# date: 2021-01-16 14:30
# python 函数示例

# 闭包，外部函数返回的是一个函数，而不是一个具体的值。返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


if __name__ == '__main__':
    # 计算一个数的平方
    square = nth_power(2)
    # 计算一个数的立方
    cube = nth_power(3)

    print(square)
    print(cube)

    print(square(2))
    print(cube(3))
