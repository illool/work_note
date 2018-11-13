# coding: utf-8

def log1(name):
    def log(fun):  # 高阶函数
        def wrapper(*args, **kwargs):  # 高阶函数 *args, **kwargs 就是fun的参数
            print(fun.__name__ + ' function has been involked ,and the args is ' + str(args) + ' ' + str(kwargs) + name)
            result = fun(*args, **kwargs)
            return result

        return wrapper

    return log


@log1('tom')
def sum(x, y):
    return x + y


@log1('lio')
def max(x, y):
    if x > y:
        return x
    else:
        return y


print(sum(2, 5))
print(max(2, 5))

