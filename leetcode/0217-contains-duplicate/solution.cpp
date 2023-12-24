class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;

        for (int i = 0; i < nums.size(); i++){
            if (s.contains(nums.at(i))){
                return true;
            }
            s.insert(nums.at(i));
           
        }
        
        return false;
    }
};
