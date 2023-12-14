# def merge(row, left_or_down):
#     i, new_row = 0, []
#     transposed = [e for e in row if e]

#     if not left_or_down: 
#         transposed = transposed[::-1]

#     while i < len(transposed):
#         if i == len(transposed) - 1:
#             new_row += [transposed[i]]
#             break
#         if transposed[i] == transposed[i + 1]:
#             new_row += [2 * transposed[i]]
#             i += 2
#         else:
#             new_row += [transposed[i]]
#             i += 1

#     if not left_or_down: 
#         new_row = [0]*(4 - len(new_row)) + new_row[::-1]

#     return new_row + [0]*(4 - len(new_row))

# def update_grid(grid, direc): 
#     if direc in 'LR':
#         grid = [merge(row, direc == 'L') for row in grid]

#     if direc in 'UD':
#         grid = [merge(row[::-1], direc == 'D') for row in zip(*grid)]
#         grid = [list(row) for row in zip(*grid)][::-1]

#     return grid

# def f(moves):
#     grid = [
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]
#     ]
    
#     for move in moves:
#         move_package = move.split(' ')
#         direction = move_package[0]
#         c, r, val = int(move_package[1]), int(move_package[2]), int(move_package[3])
        
#         grid = update_grid(grid, direction)
#         if grid[r][c] != 0:
#             return "Error"
#         grid[r][c] = val
        
#     answer = ""
#     for r in range(4):
#         for c in range(4):
#             if grid[r][c] == 0: answer += '.'
#             else: answer += str(grid[r][c])
            
#             if c == 4 - 1:
#                 if r < 4 - 1: answer += '\n'
#             else: answer += ','
    
#     return answer

class Game2048:
    def __init__(self, init_grid, n_row, n_col):
        self.grid = init_grid
        self.grid_str = ""
        self.n_row = n_row
        self.n_col = n_col
        
    def transpose_grid_attr(self): # O(n_row * n_col)
        return zip(*self.grid)
        
    def update_row(self, row, left_or_down): # O(n_row)
        i, new_row = 0, []
        onlyPositive_nums = [e for e in row if e > 0] # O(n_row)

        if not left_or_down: onlyPositive_nums = onlyPositive_nums[::-1] # O(n_row)

        while i < len(onlyPositive_nums): # O(n_row)

            if i == len(onlyPositive_nums) - 1:
                new_row.append(onlyPositive_nums[i])
                break
            
            # Combine similar values or not
            if onlyPositive_nums[i] == onlyPositive_nums[i + 1]:
                new_row.append(2 * onlyPositive_nums[i])
                i += 2
            else:
                new_row.append(onlyPositive_nums[i])
                i += 1
            # \Combine similar values or not

        if not left_or_down: # O(n_row)
            reversed_new_row = new_row[::-1]
            new_row = [0] * (self.n_row - len(new_row))
            new_row.extend(reversed_new_row)

        new_row.extend([0] * (self.n_row - len(new_row)))
        return new_row

    def update_grid(self, direc, r, c, val):
        
        # Merge values
        if direc in 'LR': # O(n_row * n_col)
            self.grid = [self.update_row(row, direc == 'L') for row in self.grid]

        if direc in 'UD': # O(n_row * n_col)
            #  transpose the grid to update rows similar to direction 'L', 'R'
            transposed_grid = self.transpose_grid_attr()
            self.grid = [self.update_row(row[::-1], direc == 'D') for row in transposed_grid]
            
            # revert the grid back to its original direction.
            original_direction_grid = self.transpose_grid_attr()
            self.grid = [list(row) for row in original_direction_grid][::-1]
        # \Merge values
        
        # Update value
        if self.grid[r][c] == 0: self.grid[r][c] = val
        else: self.grid_str = "Error"
        # \Update value
                
        return
    
    def output_grid_str(self):
        if self.grid_str == "Error": return self.grid_str
        
        self.grid_str = ""
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.grid[r][c] == 0: self.grid_str += '.'
                else: self.grid_str += str(self.grid[r][c])
                
                if c == self.n_col - 1:
                    if r < self.n_row - 1: self.grid_str += '\n'
                else: self.grid_str += ','

        return self.grid_str

def f(moves):
    init_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    game = Game2048(init_grid = init_grid, n_row = len(init_grid), n_col = len(init_grid[0]))
    
    for move in moves:
        # Extract input
        move_package = move.split(' ')
        direction = move_package[0]
        c, r, val = int(move_package[1]), int(move_package[2]), int(move_package[3])
        # \Extract input
        
        game.update_grid(direc = direction, r = r, c = c, val = val) # O(n_row * n_col)
    
    answer = game.output_grid_str()
    return answer

moves = ["U 0 0 2", 
 "U 1 0 2", 
 "L 3 3 4"]
assert f(moves) == "4,.,.,.\n.,.,.,.\n.,.,.,.\n.,.,.,4", print(f(moves))

moves = ["L 0 0 2", 
 "L 0 0 2"]
assert f(moves) == "Error", print(f(moves))

moves = ["L 2 3 4", 
 "U 1 3 4", 
 "U 0 0 2", 
 "R 3 2 2"]
assert f(moves) == ".,.,2,8\n.,.,.,.\n.,.,.,2\n.,.,.,.", print(f(moves))

moves = ["U 1 0 4", 
 "U 2 1 4", 
 "U 1 1 2", 
 "U 0 0 2", 
 "U 2 1 2"]
assert f(moves) == "2,4,4,.\n.,2,2,.\n.,.,.,.\n.,.,.,.", print(f(moves))

moves = ["L 0 2 2", 
 "R 2 0 4", 
 "U 0 1 4", 
 "L 2 3 4", 
 "D 1 1 2", 
 "U 2 1 2", 
 "R 1 3 4", 
 "R 3 2 2"]
assert f(moves) == ".,.,.,16\n.,.,.,2\n.,.,.,2\n.,.,.,4", print(f(moves))