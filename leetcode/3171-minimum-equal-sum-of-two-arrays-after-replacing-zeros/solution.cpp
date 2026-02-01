class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long count1 = 0;
        long count2 = 0;
        long sums1 = 0;
        long sums2 = 0;
        
        for(int i: nums1) {
            sums1 += i;
            if (i == 0) {
                count1++;
            }
        }

        for(int i: nums2) {
            sums2 += i;
            if (i == 0) {
                count2++;
            }
        }

        long min1 = sums1 + count1;
        long min2 = sums2 + count2;

        if (count1 == 0 && min2 > min1) {
            return -1;
        }
        if (count2 == 0 && min1 > min2) {
            return -1;
        }

        return max(min1, min2);
    }
};
