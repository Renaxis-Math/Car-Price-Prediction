# NOT GOOD!

def solve(n, processorTime, taskTime):
    
    processorTime.sort()
    taskTime.sort()
    taskTime.reverse()
    
    result, cur_task = 0, 0
    
    for proctime in processorTime:
        for i in range(4):
            completionTime = proctime + taskTime[cur_task]
            cur_task += 1
            result = max(result, completionTime)
    
    return result

# def solve(n, processorTimes, taskTimes):
    
#     processorTimes.sort()
#     taskTimes.sort(reverse=True)
    
#     answers = []
#     taskTime_i = 0
#     for i, processorTime in enumerate(processorTimes):
#         answers.append(processorTime + taskTimes[taskTime_i])
#         taskTime_i += 4
    
#     return max(answers)

n = 2
processorTime = [8, 10]
taskTime = [2, 2, 3, 1, 8, 7, 4, 5]
answer = solve(n, processorTime, taskTime)
assert answer == 16, print(answer)

n = 2
processorTime = [10, 20]
taskTime = [2, 3, 1, 2, 5, 8, 4, 3]
answer = solve(n, processorTime, taskTime)
assert answer == 23, print(answer)