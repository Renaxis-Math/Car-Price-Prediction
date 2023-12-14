def solution(n, connections):
    adj = [set() for _ in range(n)]
    for i, j in connections:
        adj[i].add(j)
        adj[j].add(i)
    common = [{} for _ in range(n)]
    # Total number of items in all the maps is at most 30 * m.
    for u1, u2 in connections:
        # u2 is the common friend
        for u3 in adj[u2]:
            if u3 != u1 and u3 not in adj[u1]:
                if u3 not in common[u1]:
                    common[u1][u3] = 0
                common[u1][u3] += 1
                # print("a = ", u1, " b = ", u3, " common = ", u2)
        # u1 is the common friend
        for u3 in adj[u1]:
            if u3 != u2 and u3 not in adj[u2]:
                if u3 not in common[u2]:
                    common[u2][u3] = 0
                common[u2][u3] += 1
                # print("a = ", u2, " b = ", u3, " common = ", u1)
    r = [-1] * n
    for i in range(n):
        # Nobody has common friend with user i.
        if len(common[i]) == 0:
            # This loop will execute at most 15 times.
            for j in range(n):
                if j not in adj[i]:
                    r[i] = j
                    break
        else:
            c = -1
            for user, num in common[i].items():
                if c < num or (c == num and user < r[i]):
                    r[i] = user
                    c = num
    return r

print(solution(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]))
print(solution(3, [[0, 1], [1, 2], [2, 0]]))

# https://leetcode.com/discuss/interview-question/3736983/Paypal-OA-or-Chennai-or-Senior-Backend-Engineer/1965773
# https://leetcode.com/discuss/interview-question/3742851/Citadel-OA-question