# ok!
def char_index(char):
    return ord(char) - ord('a') + 1

def solution(coupon, k):
    mod = 10**9 + 7
    answer = 0
    
    char_counts = [0 for i in range(27)]
    
    for i in range(k):
        index = char_index(coupon[i])
        char_counts[index] += 1
        answer += (index**char_counts[index])
        
    cur_val = answer
    coupon_length = len(coupon)
    end = k
    while end < coupon_length:
        start = end - (k-1)
        #
        prev_index = char_index(coupon[start-1])
        last_index = char_index(coupon[end])
        
        cur_val -= prev_index**char_counts[prev_index]
        char_counts[prev_index] -= 1
        if char_counts[prev_index] > 0:
            cur_val = (cur_val + prev_index**char_counts[prev_index]) % mod 

        if char_counts[last_index] > 0:
            cur_val -= (last_index**char_counts[last_index])
        char_counts[last_index] += 1
        cur_val = (cur_val + last_index**char_counts[last_index]) % mod
        
        answer = max(answer, cur_val)
        #
        end += 1
    
    return answer

# string = "bcaa"
# k = 3
# answer = solution(string, k)
# print(answer)

string = "abcc"
k = 2
answer = solution(string, k)
print(answer)