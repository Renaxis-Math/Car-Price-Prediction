const int M = 1000000007;
int mul(long long x, long long y) {
    return x * y % M;
}

int pow(int x, int y) {
    int r = 1;
    for (; y; y >>= 1) {
        if (y & 1) {
            r = mul(r, x);
        }
        x = mul(x, x);
    }
    return r;
}

int solution(int n_intervals, int n_processes) {
    if (n_processes == 1) {
        return n_intervals == 1;
    }
    return mul(n_processes, pow(n_processes - 1, n_intervals - 1)); 
}