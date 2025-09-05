class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # ht = {}
        # for i in s:
        #     # ht[i] = ht.get(i,0) + 1
        #     #ht.get取i的value，如果没有就返回0
        #     # + 1 累加次数
        #     #ht[i]更新当前value
        #     if i in ht:
        #         ht[i] += 1
        #     else:
        #         ht[i] = 1
        # for n in t:
        #     val = ht.get(n)
        #     if val == 0 or val == None:
        #         return False
        #     else:
        #         ht[n] -= 1
        # return True  
        return Counter(s) == Counter(t)
