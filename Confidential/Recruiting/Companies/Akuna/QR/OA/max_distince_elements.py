# https://www.geeksforgeeks.org/maximize-the-count-of-distinct-elements-in-array-after-at-most-k-changes/

def solve(n, a, b, k):
    pass

a = [2, 3, 3, 2, 2]
n = len(a)
b = [1, 3, 2, 4, 1]
k = 2
answer = solve(n, a, b, k)
assert answer == 4, print(answer)

a = [1, 2, 1, 4, 6, 4, 4]
n = len(a)
b = [1, 2, 3, 4, 5]
k = 2
answer = solve(n, a, b, k)
assert answer == 6, print(answer)

a = [1, 2, 1, 4, 6, 4, 4]
n = len(a)
b = [1, 2, 3, 4, 5]
k = 1
answer = solve(n, a, b, k)
assert answer == 5, print(answer)