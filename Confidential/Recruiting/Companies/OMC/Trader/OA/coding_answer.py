import math

def numDupDigitsAtMostN(N):
    L = list(map(int, str(N + 1)))
    n = len(L)
    res = sum(9 * math.perm(9, i) for i in range(n - 1))
    s = set()
    for i, x in enumerate(L):
        for y in range(i == 0, x):
            if y not in s:
                res += math.perm(9 - i, n - i - 1)
        if x in s: break
        s.add(x)
    return res

def countNumbers(arr):
    for num_tuple in arr:
        left, right = num_tuple[0], num_tuple[1]
        
        answer = numDupDigitsAtMostN(right) - numDupDigitsAtMostN(left-1)
        print(answer)
        
arr = [[80, 87]]
print(countNumbers(arr))