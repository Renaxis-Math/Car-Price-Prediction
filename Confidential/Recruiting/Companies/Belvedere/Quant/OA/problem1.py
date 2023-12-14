from collections import deque
import sys
# import numpy as np
# import pandas as pd
# from sklearn import
def calculate_rolling_average(window_quantity, window_trade_count, trades):
    """
    10
    2
    
    [(1.0, 8), (1.5, 5)]
    
    trade[1] < window_quantity
    cur_quantity_sum <= window_quantity
    
    cur_quantity_sum + trade[1] - window_quantity < window_quantity
    deque_trade[1] 
    """
    trade_queue = deque()
    quantity_sum = 0
    weighted_price_sum = 0
    answers = []
    
    for i, trade in enumerate(trades):
        trade_amount, trade_count = trade
        
        if len(trade_queue) == window_trade_count:
            first_trade = trade_queue.popleft()
            weighted_price_sum -= first_trade[0] * first_trade[1]
            quantity_sum -= first_trade[1]
        
        if trade_count >= window_quantity:
            trade_queue = deque()
            
            trade[1] = window_quantity
            trade_queue.append(trade)
            
            quantity_sum = window_quantity
            weighted_price_sum = trade[0] * trade[1]
        
        else:
            if trade_count + quantity_sum > window_quantity:
                cur_trade_count = trade_count + quantity_sum
                removing_trade_count = cur_trade_count - window_quantity
                
                while (len(trade_queue) > 0 and trade_queue[0][1] <= removing_trade_count):
                    remove_trade = trade_queue.popleft()
                    removing_trade_count -= remove_trade[1]

                    cur_trade_count -= remove_trade[1]
                    weighted_price_sum -= remove_trade[0] * remove_trade[1]
                
                first_trade_count = trade_queue[0][1]
                trade_queue[0][1] -= removing_trade_count
                cur_trade_count -= removing_trade_count
                weighted_price_sum -= removing_trade_count * trade_queue[0][0]
                
                trade_queue.append(trade)
                quantity_sum = cur_trade_count
                weighted_price_sum += trade[0] * trade[1]
                
            else:
                trade_queue.append(trade)
                quantity_sum += trade[1]
                weighted_price_sum += trade[0] * trade[1]

        answers.append("{:.2f}".format(weighted_price_sum / quantity_sum))
    
    return answers

# for line in sys.stdin:
#     print (line, end="")
#     # Split the input string into parts using the semicolon as a delimiter
#     parts = line.split(";")
#     # Extract the values for x and y from the first part
#     window_quantity, window_trade_count = map(int, parts[0].split(","))
#     # Extract the tuple values from the remaining parts and convert them to the desired format
#     inputs = [[float(val1), int (val2)] for val1, val2 in (part.split("") for part in parts[1:])]
window_quantity = 10
window_trade_count = 2
inputs = [[1.0, 8], [1.50, 5]]
print(calculate_rolling_average(window_quantity, window_trade_count, inputs))

window_quantity = 10
window_trade_count = 2
inputs = [[1.0, 1], [1.50, 1], [2.00,1]]
print(calculate_rolling_average(window_quantity, window_trade_count, inputs))