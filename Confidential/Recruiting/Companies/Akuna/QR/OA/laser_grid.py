def solve(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    seen = set([(initR, initC)])
    end_cell = (finalR, finalC)    

    def is_valid(cell):
        r, c = cell
        return 0 <= r <= finalR and 0 <= c <= finalC
    
    # memo = {}
    # def solve_helper(start_cell) -> int:
    #     key = start_cell
    #     if key in memo: return memo[key]
        
    #     if start_cell == end_cell: return 0
    #     if not is_valid(start_cell): return float('inf')
        
    #     answer = float('inf')
    #     move_answer = float('inf')
        
    #     moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     for move in moves:
    #         next_cell = (start_cell[0] + move[0], start_cell[1] + move[1])
    #         if next_cell in seen: continue
            
    #         seen.add(next_cell)
    #         sub_answer = solve_helper(next_cell)
    #         if sub_answer == float('inf'): continue
            
    #         if move[0] == 0: sub_answer += costCols[start_cell[1]]
    #         else: sub_answer += costRows[start_cell[0]]
    #         move_answer = min(move_answer, sub_answer)
    #         seen.remove(next_cell)
    
    #     answer = move_answer
    #     memo[key] = answer
    #     return answer
    
    # answer = solve_helper((initR, initC))
    # return answer
    
    dp = [[float('inf') for dp_c in range(cols)] for dp_r in range(rows)]
    dp[finalR][finalC] = 0
    
    for dp_r in range(finalR, -1, -1):
        for dp_c in range(finalC, -1, -1):
            if dp_r == finalR and dp_c == finalC: continue
            
            cell = (dp_r, dp_c)
            
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for move in moves:
                next_cell = (dp_r + move[0], dp_c + move[1])
                if not is_valid(next_cell): continue
                
                seen.add(next_cell)
                
                sub_answer = dp[next_cell[0]][next_cell[1]]
                if sub_answer == float('inf'): continue
                
                if move[0] == 0: sub_answer += costCols[dp_c]
                else: sub_answer += costRows[dp_r]
                
                dp[dp_r][dp_c] = min(dp[dp_r][dp_c], sub_answer)
                seen.remove(next_cell)            
    
    return dp[initR][initC]

rows = 4
cols = 4
initR = 1
initC = 0
finalR = 2
finalC = 3
costRows = [1, 2, 3]
costCols = [4, 5, 6]
answer = solve(rows, cols, initR, initC, finalR, finalC, costRows, costCols)
assert answer == 17, print(answer)