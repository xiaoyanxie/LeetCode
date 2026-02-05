class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int lastMin = -1;
        int lastMax = -1;
        int bad = -1;
        long long res = 0;

        for(int i = 0; i < nums.size(); i++) {
            if (nums[i] == minK) lastMin = i;
            if (nums[i] == maxK) lastMax = i;
            if (nums[i] > maxK || nums[i] < minK) bad = i;

            //count if the interval valid
            int limit = min(lastMin, lastMax);
            if (bad < limit) {
                res += (long long)(limit - bad);
            }
        }
        return res;
    }
};
