class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        #sort by frequency
        num_list = list(freq.keys())
        num_list.sort(key=lambda x: -freq[x])
        #default sort is acsending
        return num_list[:k]
        


    #First get the frequency of each number
    #Second get the sort 
