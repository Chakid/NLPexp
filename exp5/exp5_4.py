# 统计每个字出现的次数

f = open("../txt/hlm.txt", "r", encoding='UTF-8')  # 设置文件对象

data = open("exp5_4.txt", 'w+', encoding='utf-8')
str1 = f.read()


def fucalculate_character_numnc(a):
    b = set(a)
    c = {}
    for i in b:
        c[i] = 0
    for i in a:
        c[i] += 1
    return c


if __name__ == '__main__':
    a = str1
    t = fucalculate_character_numnc(a)

    items = list(t.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for item in items:
        word, count = item
        Strs = "{0:<10}{1:>5}".format(word, count)
        print(Strs,file=data)

