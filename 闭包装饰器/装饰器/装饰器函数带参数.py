'''
如果装饰器函数带有参数，在外函数的外层再包装一层，这里接受func
之前是某个人肚子里有某个人，以下是某人肚子里有某人，肚子里又有某人
'''
def arg_func(sex):
    def func1(b_func):
        def func2():
            if sex=='man':
                print('你不可以生娃')
            if sex=='woman':
                print('你可以生娃')
            return b_func()
        return  func2
    return func1

#arg_func(sex='man')()()>func1
#func1()>func2
#func2>('你不可以生娃') or ('你可以生娃') b_func()

@arg_func(sex='man')
def man():
    print('干重活')

@arg_func(sex='woman')
def woman():
    print('干轻活')

man()