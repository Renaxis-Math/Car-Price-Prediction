def countAndSay(n):
    dp = [''] * (n + 1)

    dp[1] = '1'
    for i in range(2, n + 1):
        prev = dp[i - 1]
        curr = ''
        j = 0
        while j < len(prev):
            count = 1
            while j + 1 < len(prev) and prev[j] == prev[j + 1]:
                count += 1
                j += 1
            curr += str(count) + prev[j]
            j += 1
        dp[i] = curr
    return dp

def solve(n, q):
    answers = []
    
    max_pos = max(q)
    
    sequence_nums = countAndSay(max_pos)
    
    for i in range(n):
        pos = q[i]
        cur_sum = 0
        for c in sequence_nums[pos]:
            cur_sum += int(c)
        answers.append(cur_sum)
    
    return answers

n = 3
q = [1, 2, 3]
answers = solve(n, q)
assert answers == [1, 2, 3], print(f"f({n}, {q}) -> {answers}")