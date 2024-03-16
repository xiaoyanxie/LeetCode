class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> output;
        for (int i = 1, j = 0; i < n + 1, j < target.size(); i++, j++) {
            while (i != target[j]) {
                output.push_back("Push");
                output.push_back("Pop");
                i++;
            }
            output.push_back("Push");
        }
        return output;
    }
};
