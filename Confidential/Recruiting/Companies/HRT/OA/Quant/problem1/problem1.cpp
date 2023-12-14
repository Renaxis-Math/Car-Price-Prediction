#include <cmath>
#include <map>
#include <cassert>
#include <iostream>

long long solve(int binDigit_i, long long cur_num, long long n, std::map<std::pair<long long, long long>, long long>& memo) {
    std::pair<long long, long long> key = std::make_pair(binDigit_i, cur_num);
    if (memo.find(key) != memo.end()) return memo[key];

    if (binDigit_i == 0) {
        if (cur_num <= 2) return 1;
        return 2;
    }

    long long answer = 0;

    if (cur_num + (1 << binDigit_i) >= n || binDigit_i % 2 != 0) {
        answer = solve(binDigit_i - 1, cur_num, n, memo);
    } else {
        long long useIt_answer = solve(binDigit_i - 1, cur_num + (1 << binDigit_i), n, memo);
        long long loseIt_answer = solve(binDigit_i - 1, cur_num, n, memo);
        answer = useIt_answer + loseIt_answer;
    }

    memo[key] = answer;
    return answer;
}

long long f(long long n) {
    if (n <= 1) return 0;

    std::map<std::pair<long long, long long>, long long> memo;
    int binDigits_count = int(log2(n)) + 1;
    long long answer = solve(binDigits_count - 1, 0, n, memo);

    return answer;
}

int main() {
    assert(f(1) == 0);
    assert(f(10) == 3);
    assert(f(289) == 23);
    assert(f(274776452) == 20479);
    
    return 0;
}