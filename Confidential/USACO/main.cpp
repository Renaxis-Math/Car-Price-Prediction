#include<iostream>
#include<string>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define FOR(i, a, b) for(int i = a; i < b; i += 1)
#define FOR(i, a, b, c) for(int i = a; i < b; i += c)
#define NEG_FOR(i, a, b) for(int i = a; i > b; i -= 1)
#define NEG_FOR(i, a, b, c) for(int i = a; i > b; i -= c)
#define FOR_EACH(i, a, b) for(auto& a : b)

const int MOD = (int)1e9 + 7;

// the argument is the input filename without the extension
void setIO(string s) {
    string path_to_file = "./fileIO/";
    freopen((path_to_file + s + ".in").c_str(), "r", stdin);
    freopen((path_to_file + s + ".out").c_str(), "w", stdout);
}

int solve(int n, int x, vi& skills, int best_skill, int worst_skill) {
    
    



    return 0;
}

int main() {
    setIO("main"); // Comment out if not File IO
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, x;
    cin >> n >> x;

    vi skills(n);
    FOR(0, n) { cin >> skills[i]; }

    int answer = solve(n, x, skills);
    cout << answer;

    return 0;
}