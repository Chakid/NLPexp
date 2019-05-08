# 可变长参数
def foo(arg1,*tupleArg,**dictArg):
    print ("arg1=",arg1)
    print ("tupleArg=",tupleArg)
    print ("dictArg=",dictArg)
foo("formal_args")