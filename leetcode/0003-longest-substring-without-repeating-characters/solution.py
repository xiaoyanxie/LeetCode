class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #check the current one in visited ones or not
        #not in, count +1
        # in, count vs longest and update longest, clear set, move right
        
        # longest = 0
        # n = len(s)
        # if n == 1 and s == " ":
        #     return 1
        # if n == 0:
        #     return 0
        # for i in range(n):
        #     container = set()
        #     count = 0
        #     for ele in range(i, n):
        #         if s[ele] not in container:
        #             container.add(s[ele])
        #             count = count + 1
        #         else:
        #             longest = max(longest, count)
        #             break
        #     else:
        #         longest = max(longest, count)
        # return longest
        left = 0
        n = len(s)
        seen = set()
        longest = 0
        for right, val in enumerate(s):   
            while val in seen:
                seen.remove(s[left])
                left += 1

            seen.add(val)
            longest = max(longest, right - left + 1)
        return longest



