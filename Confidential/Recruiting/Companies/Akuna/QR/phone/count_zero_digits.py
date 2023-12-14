# def count_zero_digits_0_to_n(n, d):
    
#     def count_zero_digits_at_num(num):
#         answer = 0
#         while num != 0:
#             last_digit = num % 10
#             answer += (last_digit == d)
#             num //= 10
#         return answer
    
#     if n < 10: return d > 0 and n >= d
    
#     if (n % 10 != 9):
#         return count_zero_digits_at_num(n) + count_zero_digits_0_to_n(n-1, d)
    
#     return 10 * count_zero_digits_0_to_n(n // 10, d) + (n // 10) + (d > 0)

def count_single_number(num):
    answer = 0
    while num > 0:
        answer += (num % 10 == 0)
        num //=10
    return answer

def solve_1_n(n):
    if n == 0: return 0
    if n <= 10: return 1
    
    next_num = n // 10
    remainder = n % 10
    
    answer = next_num + 10 * (solve_1_n(next_num) - 1) # -1 for 0, next_num ~ 10, 100, 1000
    if remainder > 0:
        answer += remainder * count_single_number(next_num) + 1
    return answer

answer = solve_1_n(105)
print(answer)