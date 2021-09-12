'''中文可以做变量名
1.函数内的东西只有在函数运行期间存活，函数结束其中的东西也就没了

'''
def test(name):
    def test_in():
        print(name)
    return test_in

func = test('whyz')
func()