# 使用函数的返回值
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print (f)
# <function sum at 0x02657770>
# lazy_sum(1,2,3,4,5)返回的是一个指向求和的函数的函数名。
# 在调用lazy_sum(1,2,3,4,5)的时候，不立刻求和，而是根据后面代码的需要在计算。
print (f())
# 15
# 用f()调用求和函数，计算出结果。

f1 = lazy_sum(1,2,3,4,5,6)
f2 = lazy_sum(1,2,3,4,5,6)
print (f1 == f2)
# False
# lazy_sum()每调用一次，都会返回一个独一无二的函数地址。