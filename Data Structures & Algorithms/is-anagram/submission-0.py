class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        a1,a2 = {},{}

        for i in range(len(s)):
            a1[s[i]] = 1 + a1.get(s[i],0)
            a2[t[i]] = 1 + a2.get(t[i],0)
        return a1 == a2



        