def solve(n, startRow, startCol, endRow, endCol):
    
    def is_valid(r, c):
        return (-n <= r < n) and (-n <= c < n)
    
    # the offsets in the eight directions
    offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    visited = set()
    queue = deque([(0, 0)])
    steps = 0

    while queue:
        curr_level_cnt = len(queue)
        has_move = False
        # iterate through the current level
        for i in range(curr_level_cnt):
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) == (endRow, endCol):
                return steps

            for offset_x, offset_y in offsets:
                next_x, next_y = curr_x + offset_x, curr_y + offset_y
                if is_valid(next_x, next_y) and (next_x, next_y) not in visited:
                    has_move = True
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
            
        if not has_move:
            return -1

        # move on to the next level
        steps += 1