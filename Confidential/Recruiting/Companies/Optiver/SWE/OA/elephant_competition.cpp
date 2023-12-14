#include <bits/stdc++.h>
 
using namespace std;
 
struct NameAndHeight {
    string name;
    int height;
 
    NameAndHeight(const string& name, int height): name(name), height(height) {}
};
 
struct Schedule {
    string name;
    int in, out;
    Schedule(const string &name, int in, int out) : name(name), in(in), out(out) {}
};
 
//  Functions must be called in increasing order of time.
class ElephantCompetition {
    unordered_map<string, int> height;
    set<pair<int, string>> have;
    map<pair<int, int>, vector<string>> in, out;
    map<int, int> others;
 
    public:
       ElephantCompetition(const vector<NameAndHeight> &names, const vector<Schedule> &schedule) {
           for (const auto& v : names) {
               height[v.name] = v.height;
           }
           for (const auto& v : schedule) {
               in[{v.in, height[v.name]}].push_back(v.name);
               out[{v.out, height[v.name]}].push_back(v.name);
           }
       }
 
       void elephantEntered(int t, int h) {
           if (in.count({t, h})) {
               have.insert({h, in[{t, h}].back()});
               in[{t, h}].pop_back();
               if (in[{t, h}].empty()) {
                   in.erase({t, h});
               }
           } else {
               ++others[h];
           }
       }
 
       void elephantLeft(int t, int h) {
           if (out.count({t, h})) {
               have.erase({h, out[{t, h}].back()});
               out[{t, h}].pop_back();
               if (out[{t, h}].empty()) {
                   out.erase({t, h});
               }
           } else if (--others[h] <= 0) {
               others.erase(h);
           }
       }
 
       vector<string> getBiggestElephants(int t) {
           // No other teams?
           if (others.empty()) {
               return {};
           }
           vector<string> r;
           for (auto t = have.lower_bound({others.rbegin()->first, ""}); t != have.end(); ++t) {
               r.push_back(t->second);
           }
           sort(r.begin(), r.end());
           return r;
 
       }
};
 
void print(const vector<string> &v) {
    cout << v.size() << endl;
    if (!v.empty()) {
        for (const auto& name : v) {
            cout << name << " ";
        }
        cout << endl;
    }
}
 
int main() {
    ElephantCompetition e({{"marry", 300}, {"rob", 250}}, {{"marry", 10, 15}, {"rob", 13, 20}});
    e.elephantEntered(8, 200);
    e.elephantEntered(10, 310);
    e.elephantEntered(10, 300);
    print(e.getBiggestElephants(11));
    e.elephantEntered(13, 250);
    e.elephantLeft(13, 310);
    print(e.getBiggestElephants(13));
    e.elephantLeft(15, 300);
    print(e.getBiggestElephants(16));
    e.elephantLeft(16, 200);
    e.elephantEntered(17, 250);
    print(e.getBiggestElephants(17));
    e.elephantEntered(18, 251);
    print(e.getBiggestElephants(19));
    e.elephantLeft(20, 250);
    e.elephantLeft(20, 250);
    e.elephantLeft(20, 251);
    return 0;
}