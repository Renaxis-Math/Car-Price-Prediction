import math

def f(n):
    if n <= 1:
        return 0
    
    memo = {}
    
    def solve(binDigit_i, cur_num):
        key = (binDigit_i, cur_num)
        if key in memo: return memo[key]

        if binDigit_i == 0:
            if cur_num <= 2:
                return 1
            return 2
        
        answer = None
        
        if cur_num + (2 ** binDigit_i) >= n or binDigit_i % 2 != 0:
            answer = solve(binDigit_i - 1, cur_num)
        else:
            useIt_answer = solve(binDigit_i - 1, cur_num + (2 ** binDigit_i))
            loseIt_answer = solve(binDigit_i - 1, cur_num)
            answer = useIt_answer + loseIt_answer
        
        memo[key] = answer
        return answer
    
    binDigits_count = int(math.log(n, 2)) + 1
    answer = solve(binDigit_i=binDigits_count - 1, cur_num=0)
    
    return answer

assert f(1) == 0, print(f(1))
assert f(10) == 3, print(f(10))
assert f(289) == 23, print(f(289))
assert f(274776452) == 20479, print(f(274776452))