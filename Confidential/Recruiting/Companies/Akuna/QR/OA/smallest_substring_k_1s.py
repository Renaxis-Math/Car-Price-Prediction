from collections import deque

def solve(input_str, k):
    
    def init_left_i():
        answer = -1
        
        left_i = 0
        while left_i < len(input_str):
            if input_str[left_i] == '1': return left_i    
            else: None
            #
            left_i += 1 
        
        return answer
    
    def init_right_i(left_i):
        answer = -1
        
        seenOne_count = 0
        right_i = left_i
        while right_i < len(input_str):
            
            # Current state
            seenOne_count += (input_str[right_i] == '1')
            if seenOne_count == k: return right_i
            else: None
            
            # Future state
            right_i += 1
            
        return answer
    
    def update_seen_one_count(seen_one_count, remove_i, add_i):
        seen_one_count -= (input_str[remove_i] == '1')
        seen_one_count += (input_str[add_i] == '1')
        
        return seen_one_count
    
    if k == 0:
        if '0' in input_str: return '0'
        else: return ''
    
    left_i = init_left_i()
    if left_i == -1: return ''
    
    right_i = init_right_i(left_i)
    if right_i == -1: return ''
    
    answer = (left_i, right_i)
    seen_one_count = k
    
    left_i += 1
    right_i += 1
    while right_i < len(input_str):
        seen_one_count = update_seen_one_count(seen_one_count, left_i - 1, right_i)
        
        if seen_one_count == k:
            cur_substr_length = right_i - left_i + 1
            
            while left_i < right_i and input_str[left_i] == '0':
                left_i += 1
            
            new_substr_length = right_i - left_i + 1
            
            if new_substr_length < cur_substr_length: 
                answer = (left_i, right_i)
            elif cur_substr_length == new_substr_length:
                new_substr = input_str[left_i : right_i + 1]
                compared_substr = input_str[answer[0] : answer[1] + 1]

                if new_substr < compared_substr: 
                    answer = (left_i, right_i)
        
        right_i += 1
    
    # return answer
    return input_str[answer[0] : answer[1] + 1]

str1 = "0101101"
k1 = 3
answer1 = solve(str1, k1)
assert answer1 == "1011", print(f"{str1, k1} -> {answer1}")

str1 = "0101101"
k1 = 5
answer1 = solve(str1, k1)
assert answer1 == '', print(f"{str1, k1} -> {answer1}")

str1 = "0101101"
k1 = 2
answer1 = solve(str1, k1)
assert answer1 == '11', print(f"{str1, k1} -> {answer1}")

str1 = "0101101"
k1 = 1
answer1 = solve(str1, k1)
assert answer1 == '1', print(f"{str1, k1} -> {answer1}")

str1 = "0101101"
k1 = 4
answer1 = solve(str1, k1)
assert answer1 == '101101', print(f"{str1, k1} -> {answer1}")