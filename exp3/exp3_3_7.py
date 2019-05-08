# 默认参数

def f(x = []):
    print(id(x))
    x.append(1)
    print(x)
    print(id(x))