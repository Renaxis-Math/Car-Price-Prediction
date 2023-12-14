// # https://leetcode.com/discuss/interview-question/3829548/Optiver-Online-Assessment-Internship

#include<iostream>
#include<vector>

using namespace std;
typedef unsigned long long ull;

int go(int last, const vector<char> &v, const vector<int> &ind) {
    for (; last < v.size() && v[ind[last]] != '-'; ++last)
    ;
    return last;
}

vector<string> solution(const vector<ull>& ids, const vector<char>& v) {
    const int n = ids.size();
    vector<int> ind(n);
    for (int i = 0; i < n; ++i) {
        ind[i] = i;
    }
    sort(ind.begin(), ind.end(), [&](int x, int y) {
        return ids[x] < ids[y];
    });
    vector<vector<int>> all;
    for (int last = go(0, v, ind); last < n;) {
        const int now = go(last + 1, v, ind);
        if (now >= n) {
            break;
        }
        int i = last + 1, t = 0;
        for (; i <= now && ids[ind[i - 1]] == ids[ind[i]] - 1; t = max(t, ind[i++]));
        ;
        if (i > now) {
            all.push_back({last, now, t});
        }
        last = now;
    }
    sort(all.begin(), all.end(), [&](const vector<int> &a, const vector<int> &b) {
        return (a[2] < b[2]) || (a[2] == b[2] && ids[ind[a[1]]] > ids[ind[b[1]]]);
    });
    ull max_id = 0;
    int t = -1;
    vector<string> r;
    for (const auto& p : all) {
        if (p[2] > t && ids[ind[p[0]]] >= max_id) {
            max_id = ids[ind[p[1]]];
            t = p[2];
            string temp;
            for (int i = ind[p[0]] + 1; i < ind[p[1]]; ++i) {
                temp.push_back(v[i]);
            }
            r.push_back(temp);
        }
    }
    return r; 
}

void print(const vector<string> &v) {
    for (const string &s : v) {
        cout << s << endl;
    }
}
int main() {
    print(solution({1, 2, 3, 4, 5, 6, 7, 8}, {'-', 'h', 'e', 'l', 'l', 'o', '-', 'b'}));
    print(solution({1, 2, 3, 5, 6, 7, 8, 4}, {'-', 'b', 'y', '-', 'h', 'i', '-', 'e'}));
    print(solution({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'-', 'h', 'e', 'l', 'l', 'o', '-', 'b', 'y', 'e', '-'}));
    return 0;
   
}