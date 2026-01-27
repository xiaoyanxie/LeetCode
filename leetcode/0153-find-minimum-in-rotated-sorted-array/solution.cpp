class Solution {
public:
    int findMin(vector<int>& nums) {
        int s = size(nums);
        if (s == 1) {
            return nums[0];
        }

        int i = 0;
        int j = s - 1;
        int mid = i + (j - i) /2;
        if (nums[i] < nums[j]) {
            return nums[0];
        }

        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (nums[mid] > nums[mid + 1]){
                return nums[mid + 1];
            }
            if (nums[mid] > nums[i]) {
                i = mid;
            }
            else {
                j = mid;
            }
        }
        return nums[mid];
    }
};
