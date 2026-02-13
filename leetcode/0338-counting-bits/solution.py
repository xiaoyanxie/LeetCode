class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        def count(i):
            cnt = 0
            while i > 0:
                if i & 1 > 0:
                    cnt += 1
                i >>= 1
            return cnt

        for i in range(len(ans)):
            ans[i] = count(i)

        return ans
