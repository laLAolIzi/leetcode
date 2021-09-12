'''class Solution:
    def reverseLeftWords( s: str, n: int) -> str:
        a=list(s)
        l=len(a)
        while n>0:
            a.append(a[0])
            a=a[1:l+1]

            n-=1

        return ''.join(a)
    print(reverseLeftWords("abcdefg",2))'''
class Solution:
    def reverseLeftWords(s: str, n: int) -> str:
        #不能用.join
        res=""
        for i in range(n,len(s)):
            res+=s[i]

        for i in range(0,n):
            res+=s[i]

        return res

    print(reverseLeftWords("abcdefg", 2))