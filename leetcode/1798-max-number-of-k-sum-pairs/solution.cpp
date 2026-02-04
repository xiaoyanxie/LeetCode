class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
    //     sort(nums.begin(), nums.end());
    //     int l = 0;
    //     int r = nums.size() - 1;
    //     int count = 0;
    //     while(l < r) {
    //         if (nums[l] + nums[r] == k) {
    //             l++;
    //             r--;
    //             count++;
    //         }
    //         else if (nums[l] + nums[r] > k) r--;
    //         else if (nums[l] + nums[r] < k) l++;
    //     }
    //     return count;
    
        unordered_map<int, int> hmap;
        int res = 0;
        for (int x: nums) {
            if (hmap[k-x] !=0) {
                hmap[k-x]--;
                res++;
            }
            else {
                hmap[x]++;
            }
        }
        return res;
    }
    
};
