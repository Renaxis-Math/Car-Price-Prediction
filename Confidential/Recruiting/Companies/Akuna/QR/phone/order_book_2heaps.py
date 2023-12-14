class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        # Average
        total, nums_count = 0.0, sum(count)
        # \Average

        # Mode
        most_count, mode = -float('inf'), None
        #\Mode

        # Min, Max
        min_num, max_num = float('inf'), -float('inf')
        # \Min, Max

        # Median
        min_stack, max_stack = [], []
        smaller_median, bigger_median = None, None
        # \Median

        answers = []
        cur_nums_count = 0
        for num, num_count in enumerate(count):
            if num_count == 0: continue

            # Update for average
            total += (num * num_count)
            cur_nums_count += num_count
            # \Update for average

            # Mode
            if num_count > most_count:
                most_count = num_count
                mode = num
            # \Mode

            # Min, Max
            if num < min_num: min_num = num
            if num > max_num: max_num = num
            # \Min, Max

            # Median

            # 0 <= len(max_stack) - len(min_stack) <= 1
            # max_stack[0] <= min_stack[0]

            for _ in range(num_count):
                if len(max_stack) == 0: heapq.heappush(max_stack, -num)
                elif len(min_stack) == 0: heapq.heappush(min_stack, num)
                else:                    
                    if num < -max_stack[0]:
                        heapq.heappush(max_stack, -num)
                        while not (0 <= len(max_stack) - len(min_stack) <= 1):
                            transfer_num = -heapq.heappop(max_stack)
                            heapq.heappush(min_stack, transfer_num)
                    elif num > min_stack[0]:
                        heapq.heappush(min_stack, num)
                        while not (0 <= len(max_stack) - len(min_stack) <= 1):
                            transfer_num = heapq.heappop(min_stack)
                            heapq.heappush(max_stack, -transfer_num)
                    else:
                        if len(max_stack) - len(min_stack) == 0:
                            heapq.heappush(max_stack, -num)
                        else: # len(max_stack) - len(min_stack) == 1
                            heapq.heappush(min_stack, num)
            # \Median

        median = None
        if nums_count % 2 == 0: 
            median = ((-max_stack[0]) + min_stack[0]) / 2.0
        else:
            median = -max_stack[0]
        
        mean = total / nums_count
        answers.extend([min_num, max_num, mean, median, mode])
        return answers