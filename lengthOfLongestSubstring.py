class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        string=set()
        right=0#最长子串结尾
        maxlen=0
        n=len(s)
        for i in range(n):
            if i!=0:
                string.remove(s[i])
            while right<n and s[right]  not in string:
                string.add(s[right])
                right+=1
            maxlen= right-i if right-i>maxlen else maxlen
        return maxlen
    print(lengthOfLongestSubstring("pwwkew"))