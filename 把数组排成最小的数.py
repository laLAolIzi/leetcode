class Solution:
    def minNumber(self, nums ) -> str:
        nums=[str(x) for x in nums]###
        s=''.join(nums)

        n=len(s)
        a=[]
        i=0
        for c in s:
            a.append(int(c))###
            i+=1
        a.sort()
        j=0
        if a[0]==0:
            while a[j]==0: j+=1
        if j ==n:return 0
        else:
            a[j],a[0]=a[0],a[j]
            a1 = [str(x) for x in a]
            return ''.join(a1)
t=Solution()
res=t.minNumber([3,30,34,5,9])
print(res)