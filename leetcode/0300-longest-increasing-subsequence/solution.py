from collections import defaultdict
class Solution:
    def findLIS(self, nums):
        if not nums: return []
        
        # tails[i] stores the index of the smallest tail of all increasing subsequences of length i+1.
        tails_indices = []
        # parent[i] stores the index of the previous element for nums[i] in the LIS
        parent = [-1] * len(nums)
        
        import bisect
        
        # Helper list just for values to do the binary search easily
        tails_values = []
        
        for i, x in enumerate(nums):
            # Use binary search on the values
            idx = bisect.bisect_left(tails_values, x)
            
            # If x is greater than all tails, extend the longest subsequence
            if idx == len(tails_values):
                tails_values.append(x)
                tails_indices.append(i)
            else:
                # Replace the existing tail with x (smaller tail is better)
                tails_values[idx] = x
                tails_indices[idx] = i
            
            # Determine the parent: The element before x in the LIS is the tail of the sequence length idx
            if idx > 0:
                parent[i] = tails_indices[idx - 1]
                
        # Reconstruct the path starting from the last element of the longest subsequence
        # The last element of the LIS is at the end of tails_indices
        curr_idx = tails_indices[-1]
        lis = []
        while curr_idx != -1:
            lis.append(nums[curr_idx])
            curr_idx = parent[curr_idx]
            
        return lis[::-1] # Reverse to get correct order

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [10,9,2,5,3,7,101,6]
                          ^
        Q: 2,3,6,101
        """
        # patsort = []

        # for i in nums:
        #     if not patsort or i > patsort[-1]:
        #         patsort.append(i)
        #     else:
                
        
        # return len(patsort)
        return len(self.findLIS(nums))
