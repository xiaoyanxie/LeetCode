
class Solution {
public:
    string removeStars(string s) {
        string newString;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '*') {
                newString += s[i];
            } else {
                newString.pop_back();
            }
        }
        return newString;
    }
};
