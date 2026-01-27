class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int cnt0 = 0;
        int cnt1 = 0;
        int s = students.size();

        for(int i = 0; i < s; i++) {
            if (students[i] == 0) {
                cnt0++;
            } 
            else {
                cnt1++;
            }
        }
        for(int i = 0; i < s; i++) {
            if ((sandwiches[i] == 0 and cnt0 == 0) or (sandwiches[i] == 1 and cnt1 == 0)){
                return s - i;
            }
            if (sandwiches[i] == 0) {
                cnt0--;
            }
            else {
                cnt1--;
            }
        }
        return 0;
        

    }
};
