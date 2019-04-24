#练习使用try-except语句.
name = [1, 2, 3]
try:
    name[3]  # 不存在3这个下标值
except IndexError as e:  # 抓取 IndexError 这个异常
    print(e)  # e是错误的详细信息
