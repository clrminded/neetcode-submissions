class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // map frequencies
        unordered_map<int,int> count;
        for(const auto& num : nums) {
            count[num]++;
        }

        // heap
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> heap;

        for(const auto& entry : count) {
            heap.push({entry.second, entry.first});
            if(heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;
        for(int i = 0; i < k; i++) {
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;
    }
};
