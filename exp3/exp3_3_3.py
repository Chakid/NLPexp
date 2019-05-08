# 列表作为函数的参数

def get_sum(*args):
    res = 0
    for i in args:
        res += i
    print(res)

lista = [1, 2, 3]
get_sum(*lista)

print('-' * 40)


def get_vk(**kwargs):
    for k, v in kwargs.items():
        print('k/v : {0} ==> {1}'.format(k, v))


dicta = {'name': 'Test', 'age': 24, 'email': 'test@qq.com'}

get_vk(**dicta)