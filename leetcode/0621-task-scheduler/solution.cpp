class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        priority_queue<int> pq;

        for (char t: tasks) {
            freq[t]++;
        }
        
        for(const auto &[c, cnt]: freq) {
            pq.push(cnt);
        }

        int res = 0;
        while (!pq.empty()) {
            int used = 0;

            vector<int> temp;
            for(int i = 0; i < n + 1; i++) {
                if (pq.empty()) {
                    break;
                }
                else {
                    int x = pq.top();
                    pq.pop();  
                    x--;
                    used++;
                    if (x > 0) {
                        temp.push_back(x);
                    }                         
                }
            }
            for (int t: temp) {
                pq.push(t);
            }
            if (pq.empty()) {
                res += used;
            }
            else {
                res += n + 1;
            }

        }
        return res;
    }
};

