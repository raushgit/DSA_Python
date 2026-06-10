// Solution 



class Solution {
private:
    void buildTree(vector<int>& nums, vector<pair<int, int>>& sg, int s, int e,
                   int index) {
        if (s == e) {
            sg[index].first = nums[s];
            sg[index].second = nums[e];
            return;
        }

        int mid = s + (e - s) / 2;
        buildTree(nums, sg, s, mid, 2 * index + 1);
        buildTree(nums, sg, mid + 1, e, 2 * index + 2);

        sg[index].first = max(sg[2 * index + 1].first, sg[2 * index + 2].first);
        sg[index].second =
            min(sg[2 * index + 1].second, sg[2 * index + 2].second);
    }

    pair<int, int> Query(vector<pair<int, int>>& sg, int l, int r, int s, int e,
                         int index) {

        // Completely outside
        if (e < l || s > r)
            return {INT_MIN, INT_MAX};

        // Completely inside
        if (l <= s && e <= r)
            return sg[index];

        int mid = s + (e - s) / 2;

        auto left = Query(sg, l, r, s, mid, 2 * index + 1);
        auto right = Query(sg, l, r, mid + 1, e, 2 * index + 2);

        return {max(left.first, right.first), min(left.second, right.second)};
    }

public:
    long long maxTotalValue(vector<int>& nums, int k) {

        int n = nums.size();
        vector<pair<int, int>> sg(4 * n, {INT_MIN, INT_MAX});
        buildTree(nums, sg, 0, n - 1, 0);

        set<pair<int, int>> st; // index , index (basically range (l -> r))

        priority_queue<pair<long long, pair<int, int>>> q; // {val , {range}}
        auto temp = Query(sg, 0, n - 1, 0, n - 1, 0);
        q.push({temp.first - temp.second, {0, n - 1}});
        st.insert({0, n - 1});

        long long ans = 0;
        while (!q.empty() && k > 0) {
            auto top = q.top();
            q.pop();
            int val = top.first;
            cout << val << " ";
            int l = top.second.first;
            int r = top.second.second;
            k--;
            ans += val;

            if (l + 1 <= r && !st.count({l + 1, r})) {
                auto t = Query(sg, l + 1, r, 0, n - 1, 0);
                st.insert({l + 1, r});
                q.push({(long long)t.first - t.second, {l + 1, r}});
            }

            if (r - 1 >= l && !st.count({l, r - 1})) {
                auto t = Query(sg, l, r - 1, 0, n - 1, 0);
                st.insert({l, r - 1});
                q.push({(long long)t.first - t.second, {l, r - 1}});
            }
        }
        return ans;
    }
};