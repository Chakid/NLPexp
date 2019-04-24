# 输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理。
fz = int(input("输入分子: "))
try:
    f = float(fz)
except ValueError:
    print("请输入整数!")
fm = int(input("输入分母: "))
try:
    f = float(fm)
except ValueError:
    print("请输入整数!")

print(fz/fm)