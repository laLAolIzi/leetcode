#数学模块常用

def func1(func):
    def func2(x,y):
        x+=5
        y+=5
        return func(x,y)
    return func2
@func1
def mysun(a,b):
    print(a+b)

mysun(1,2)