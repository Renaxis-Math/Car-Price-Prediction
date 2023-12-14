def solution(queries):
    answers = []
    start_end_map = {}
    end_start_map = {}
    
    cur_max = 0
    for i, query in enumerate(queries):
        if i == 0:
            start_end_map[query] = query
            end_start_map[query] = query
            cur_max = 1
        else:
            cur_range = [query, query]
            start, end = cur_range
            
            if start - 1 in end_start_map:
                cur_range[0] = end_start_map[start-1]
            if end + 1 in start_end_map:
                cur_range[1] = start_end_map[end + 1]
            
            start_end_map[cur_range[0]] = cur_range[1]
            end_start_map[cur_range[1]] = cur_range[0]
            
            cur_max = max(cur_max, cur_range[1] - cur_range[0] + 1)
        
        answers.append(cur_max)
    
    return answers

queries = [1,4,2,5]
print(solution(queries))

queries = [3,6,1,2,5,4]
print(solution(queries))