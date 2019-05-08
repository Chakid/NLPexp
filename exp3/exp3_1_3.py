# 局部变量和全局变量
a = '我是真正的全局变量'

def showvariable():
    b = '我一直都是局部变量'
    print(a)
    print(b)

showvariable()