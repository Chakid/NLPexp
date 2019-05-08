# 函数中修改列表参数
t_list = ['m1', 'm2', 'm3']
def show_maagicians(L):
    for i in t_list:
        print(i)
    return

show_maagicians(t_list)

def make_great(L):
    for i in range(len(L)):
        L[i] = 'the Great ' + L[i]
    return

make_great(t_list)
show_maagicians(t_list)