'''https://www.cnblogs.com/whyaza/p/9505205.html
比如我们拿到了别人不可修改的API，但是他写的有些简陋，我们想添加功能，这时可以使用装饰器
语法@func1
意义：不影响原有函数的功能，还会添加新的功能
>@func1
>def myprint():
myprint()==func2()+myprint
普通装饰器 zsq(bzs)()
装饰器函数带参数：dczsq(cs='man')(bzs)() 多一层包装来接收装饰器的参数
被装饰的函数带参数：只需要在最内部函数传入参数即可

'''
def func1(func):#装饰器必须要有参数用来接受函数
    def func2():
        print('aabb')
        return func()
    return func2
#TypeError: func1() takes 0 positional arguments but 1 was given

#func1(myprint)()接受被装饰的函数作为参数，且再执行一次调用()
#工作流程func2()->print('aaabbb)->return func()/myprint()->print("你好，我是print")
@func1
def myprint():#装饰器意义：当执行func（）时，会限制性func1内容
    print('你好，我是print')

myprint()#func1(myprint)()