class Solution:
    def validIPAddress(self, IP: str) -> str:#判断ipv4
        resn='Neither'
        res4='IPv4'
        #IPv4
        num4=IP.split('.')
        for i in range(4):
            cnum4i=''.join(num4[i])
            if cnum4i[0]=='0':return resn
            for j in range(len(cnum4i)):
                if cnum4i[j]>'0' and cnum4i[j]<'9':
                    continue
                else:
                    return resn
            if int(num4[i]) > 255: return resn
        return res4

test=Solution()
res=test.validIPAddress('172.16.254.266')
print(res)
