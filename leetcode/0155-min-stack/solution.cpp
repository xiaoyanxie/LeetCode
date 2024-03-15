class MinStack {
public:
    MinStack() {    
    }

    void push(int val) {
        if (s1.empty()) {
            minimum = val;
        } else if (val < s1.top().minEle) {
            minimum = val;
        } else {
            minimum = s1.top().minEle;
        }
        s1.push(Node(val, minimum));
    }

    void pop() { s1.pop(); }

    int top() { return s1.top().value; }

    int getMin() { return s1.top().minEle; }

private:
    struct Node {
        int value;
        int minEle;
        Node(int v, int m): value(v), minEle(m) {}
    };
    stack<Node> s1;
    int minimum;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
