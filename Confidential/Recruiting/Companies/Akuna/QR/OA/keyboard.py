from collections import deque

def get_2D_index_from_1D_index(i, n_col):
    passed_rows_count = i // n_col
    passed_cols_down = i % n_col

    r = passed_rows_count
    c = passed_cols_down
    
    return (r, c)

def get_1D_index_from_2D_index(r, c, n_col):
    passed_rows_count = r
    passed_cols_count = c

    return passed_rows_count * n_col + passed_cols_count

def entryTime(s, keypad):
    
    def is_valid(r, c):
        return (0 <= r < 3) and (0 <= c < 3)
    
    def build_keyNeighbors_map(s):
        answer = {}

        for i in range(1, 10):
            answer[str(i)] = set()
        
        moves = [(0, 1), (0, -1), (1, 0), (1, -1),
                 (1, 1), (-1, 0), (-1, 1), (-1, -1)]
        
        for i in range(len(s)):
            c = s[i]
            cur_r, cur_c = get_2D_index_from_1D_index(i, 3)
            for move in moves:
                next_r, next_c = cur_r + move[0], cur_c + move[1]
                if is_valid(next_r, next_c):
                    next_i = get_1D_index_from_2D_index(next_r, next_c, 3)
                    answer[c].add(s[next_i])

        return answer
                    
    keyNeighbors_map = build_keyNeighbors_map(keypad)
    
    answer = 0
    for i in range(1, len(s)):
        prev_c, cur_c = s[i], s[i-1]
        neighbors = keyNeighbors_map[prev_c]

        if prev_c == cur_c: continue
        elif cur_c in neighbors: answer += 1
        else: answer += 2
    
    return answer

s = "423692"
keypad = "923857614"
print(entryTime(s, keypad))

s = "5111"
keypad = "752961348"
print(entryTime(s, keypad))