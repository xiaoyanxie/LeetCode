class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #n: target k: number of elements in a valid combination
        nums = list(range(1, 10))
        res = []

        def dfs(start, path, remain):
            if len(path) > k:
                return
            if remain < 0:
                return
            if remain == 0:
                if len(path) != k:
                    return
                res.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                
                dfs(i+1, path, remain - nums[i])
                path.pop()

        dfs(0, [], n)
        return res
