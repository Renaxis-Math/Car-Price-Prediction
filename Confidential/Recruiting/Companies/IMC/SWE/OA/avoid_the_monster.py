import heapq

def is_valid(cell, n_row, n_col): # O(1)
    r, c = cell
    return (0 <= r < n_row) and (0 <= c < n_col)

def get_distance(cell1, cell2): # O(1)
    x1, y1 = cell1
    x2, y2 = cell2
    
    return abs(x1 - x2) + abs(y1 - y2)

def findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn):
    
    def get_min_distance(monsters_cells, cell):
        min_distance = n + m - 2
        for monsters_cell in monsters_cells: # O(len(monsters_cells))
            min_distance = min(min_distance, get_distance(monsters_cell, cell))
        return min_distance

    
    def find_distance(cell):
        if cell not in cell_closestMonsterDistance:
            cell_closestMonsterDistance[cell] = get_min_distance(monsters_cells, cell)
        return cell_closestMonsterDistance[cell]
    

    def mid_or_below_does_not_solve(value):
        """
        Return True if you can find the path with the min_value == value
        """
        if find_distance(start_cell) < value:
            return False

        queue = [(-find_distance(start_cell), start_cell)]
        heapq.heapify(queue)
        
        level = {start_cell : 0}
        parent = {start_cell : None}
        nextLevel = 1
        
        while queue:
            cur_length = len(queue)
            for _ in range(cur_length):
                neg_distance, cell = heapq.heappop(queue)
                if cell == end_cell:
                    return True
                
                moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for move in moves:
                    next_cell = (cell[0] + move[0], cell[1] + move[1])
                    if is_valid(next_cell, n, m) and (next_cell not in level):
                        if not (find_distance(next_cell) < value):
                            level[next_cell] = nextLevel
                            parent[next_cell] = cell                            
                            heapq.heappush(queue, (-find_distance(next_cell), next_cell))
            
            nextLevel += 1
        
        return False
    
    monsters_cells = list(zip(monsterRow, monsterColumn))

    start_cell = (startRow, startColumn)
    end_cell = (endRow, endColumn)
    cell_closestMonsterDistance = {}
    
    min_distance, max_distance = 0, n + m - 2

    left, right = min_distance, max_distance
    while left < right:
        
        # mid = left + (right - left) // 2
        #TODO
        if (right - left + 1) % 2 == 0:
            mid = left + (right - left) // 2 + 1
        else:
            mid = left + (right - left) // 2
        #TODO        

        if mid_or_below_does_not_solve(mid):
            left = mid + 1
        else:
            right = mid
    
    return left - 1

test1 = (5, 3, 1, 1, 4, 2, [0, 2], [2, 2])
answer1 = findBestPath(test1[0], test1[1], test1[2], test1[3], test1[4], test1[5], test1[6], test1[7])
print(answer1)

# n = 3
# m = 3
# startRow = 0
# startColumn = 1
# endRow = 2
# endColumn = 2
# monsterRow = [1, 1, 1]
# monsterColumn = [0, 1, 2]
# result = findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn)
# print(result)


# n = 4
# m = 4
# startRow = 0
# startColumn = 0
# endRow = 3
# endColumn = 3
# monsterRow = [0, 1]
# monsterColumn = [3, 2]
# result = findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn)
# print(result)