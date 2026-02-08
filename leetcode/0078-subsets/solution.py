class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []

        # def dfs(i, path):
        #     if i == len(nums):
        #         res.append(path.copy()) 
        #         return 

        #     path.append(nums[i])
        #     dfs(i + 1, path)
        #     path.pop()
        #     dfs(i + 1, path)
            
        # dfs(0, [])
        # return res
        #nums[1,2]->res[[],[1],[1,2],[2]]
        # i =0 start = 0
        # i = 1 start = 1
        #path = [1] []
        #i = 1 start = 1
        res = []
        def dfs(path, start):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, i+1)
                path.pop()

        dfs([], 0)
        return res
