class Solution {
    public int findMin(int[] nums) {
        int s = nums.length;

        if (s == 1) {
            return nums[0];
        }
        if (nums[0] < nums[s-1]) {
            return nums[0];
        }

        int l = 0;
        int r = s - 1;
        int mid = l + (r - l) / 2;

        while(l <= r) {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1]) {
                return nums[mid + 1];
            }
            if (nums[mid] > nums[l]){
                l = mid;
            }
            else {
                r = mid;
            }
        }
        return nums[mid];
    }
}
