def get_duplicates(pos_nums) -> int:
    mask = 0
    answers = []
    
    for num in pos_nums:
        if mask & (1 << num) == 0: # not seen
            mask |= (1 << num)
        else: answers.append(num)
    
    return answers