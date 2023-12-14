int solution(const vector<int> &a, const vector<int> &b) {
    const int n = a.size();
    vector<int> dp = {1, 1};
    int r = 1;
    for (int i = 1; i < n; ++i) {
        dp = {max(a[i] >= a[i - 1] ? (dp[0] + 1) : 1, a[i] >= b[i - 1] ? (dp[1] + 1) : 1),
              max(b[i] >= a[i - 1] ? (dp[0] + 1) : 1, b[i] >= b[i - 1] ? (dp[1] + 1) : 1)};
        r = max(r, max(dp[0], dp[1]));
    }
    return r;
}
                  
int main() {
    cout << solution({5, 2, 4, 1}, {3, 6, 2, 2}) << endl;
    return 0;
}

// https://leetcode.com/discuss/interview-question/3852465/Citadel-OA