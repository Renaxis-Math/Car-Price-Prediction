int countPalindromesAroundCenter(const string& ss, int lo, int hi) {
    int ans = 0;

    while (lo >= 0 and hi < ss.size()) {
        if (ss[lo] != ss[hi])
            break;      // the first and last characters don't match!

        // expand around the center
        lo--;
        hi++;

        ans++;
    }

    return ans;
}

int countPalindromes(string s) {
    int ans = 0;

    for (int i = 0; i < s.size(); ++i) {
        // odd-length palindromes, single character center
        ans += countPalindromesAroundCenter(s, i, i);

        // even-length palindromes, consecutive characters center
        ans += countPalindromesAroundCenter(s, i, i + 1);
    }

    return ans;
}