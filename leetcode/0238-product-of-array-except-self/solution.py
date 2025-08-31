class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        for i in range(1, n):#从左往右，index1到n-1，不包含开始
            # if i > 0:
                res[i] = res[i - 1] * nums[i - 1]
                # print(res)
        
        suffix = 1

        for j in range(n - 1, -1, -1):#从右往左，不包含最后一个数
            
            res[j] = res[j] * suffix
            suffix = suffix * nums[j]

 
        return res

