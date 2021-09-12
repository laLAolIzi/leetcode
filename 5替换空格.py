#字符串不是可迭代对象

class Solution:
    def replaceSpace(self, s: str) -> str:
        lists=list(s)
        for i in range(len(lists)):
            if lists[i]==' ':
                lists.pop(i)
                lists.insert(i,'%20')
        res=''.join(lists)
        return res

#在 Python 和 Java 等语言中，字符串都被设计成「不可变」的类型，即无法直接修改字符串的某一位字符，需要新建一个字符串实现。(leetcode
#新建一个字符串列表，遍历s，遇到c直接append(c)，遇到空格append(%20)