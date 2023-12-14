def solve(rowA, rowB):
    if rowA.count(0) == 0 and rowB.count(0) == 0 and sum(rowA) != sum(rowB):
        return -1
    
    if rowA.count(0) == 0 and sum(rowA) + rowA.count(0) < sum(rowB) + rowB.count(0):
        return -1
    
    if rowB.count(0) == 0 and sum(rowB) + rowB.count(0) < sum(rowA) + rowA.count(0):
        return -1
    
    return max(sum(rowA) + rowA.count(0), sum(rowB) + rowB.count(0))