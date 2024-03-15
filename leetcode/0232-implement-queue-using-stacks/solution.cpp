class MyQueue {
public:
    MyQueue() {}

    void push(int x) {
        while (!s1.empty()) {
            int temp = s1.top();
            s2.emplace(temp);
            s1.pop();
        }
        s2.emplace(x);

        while (!s2.empty()) {
            int temp = s2.top();
            s1.emplace(temp);
            s2.pop();
        }
    }

    int pop() {
        int top;
        top = s1.top();
        s1.pop();
        return top;
    }

    int peek() { return s1.top(); }

    bool empty() {
        if (s1.empty()) {
            return true;
        }
        return false;
    }

private:
    stack<int> s1;
    stack<int> s2;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
