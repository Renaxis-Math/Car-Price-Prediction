import math

def is_outlier(price, mean, std):
    return abs(price - mean) > 3 * std

def can_eliminate_left(mid_idx, x_input, points):
    mid_point = points[mid_idx]
    x_mid, y_mid = mid_point
    
    return x_mid < x_input

def filter_outliers(houses, area_Sum_SumSquared_map): # O(n)
    answers = []
    for house in houses:
        area, price = house
        cur_sum_price, cur_sum_price_squared, count = area_Sum_SumSquared_map[area]
        new_sum_price, new_sum_price_squared, new_count = cur_sum_price - price, cur_sum_price_squared - price * price, count - 1
        
        if new_count == 0:
            answers.append(house)
        else:
            mean = new_sum_price / new_count
            squared_mean = new_sum_price_squared / new_count
            var = squared_mean - mean * mean
            std = math.sqrt(var)
            
            if not is_outlier(price, mean, std):
                answers.append(house)
        
    return answers

def find_nearest(points, x_input, is_right): # O(log n)
    
    left, right = 0, len(points)-1
    while left < right:
        mid = left + (right - left) // 2
        
        if can_eliminate_left(mid, x_input, points):
            left = mid + 1
        else:
            right = mid
            
    if is_right:
        return left
    
    if points[left][0] == x_input:
        return left
    return left - 1 

def compute_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    return (y1 - y2) / (x1 - x2) 

def calculate(point1, point2, x_input, area_meanPrice_map):

    x1, y1 = point1[0], area_meanPrice_map[point1[0]]
    x2, y2 = point2[0], area_meanPrice_map[point2[0]]
    
    if x1 == x2:
        return y1
    
    slope = compute_slope((x1, y1), (x2, y2))

    answer = y1 + (x_input - x1) * slope
    return round(answer)

def get_final_answer(value, int_lower_bound, int_upper_bound):
    if value < int_lower_bound:
        return int_lower_bound
    if value > int_upper_bound:
        return int_upper_bound
    return round(value)

def build_area_meanPrice_map(houses): # O(n)
    answer = {}
    count = {}
    for area, price in houses:
        if area not in answer:
            answer[area] = 0
            count[area] = 0
        answer[area] += price
        count[area] += 1

    for area in answer:
        mean = answer[area] / count[area]
        answer[area] = mean
    
    return answer
    
def findValuation(reqArea, area, price):
    houses = list(zip(area, price))
    INT_LOWER_BOUND = 10**3
    INT_UPPER_BOUND = 10**6
    
    def build_area_Sum_SumSquared_map(): # O(n)
        answer = {}
        for i in range(len(area)):
            if area[i] not in answer:
                answer[area[i]] = [0, 0, 0]

            answer[area[i]][0] += price[i]
            answer[area[i]][1] += price[i] * price[i]
            answer[area[i]][2] += 1

        return answer  

    area_Sum_SumSquared_map = build_area_Sum_SumSquared_map()
    
    filtered_houses = filter_outliers(houses, area_Sum_SumSquared_map)
    filtered_houses.sort()
    area_meanPrice_map = build_area_meanPrice_map(filtered_houses)
    
    n = len(filtered_houses)
    if n == 0:
        return 1000
    if n == 1:
        val_price = filtered_houses[0][1]
        return val_price
    
    left_most_x = filtered_houses[0][0]
    right_most_x = filtered_houses[n-1][0]
    
    if reqArea < left_most_x:
        answer = calculate(filtered_houses[0], filtered_houses[1], reqArea, area_meanPrice_map)
        return get_final_answer(answer, INT_LOWER_BOUND, INT_UPPER_BOUND)
    
    if reqArea > right_most_x:
        answer = calculate(filtered_houses[n-2], filtered_houses[n-1], reqArea, area_meanPrice_map)
        return get_final_answer(answer, INT_LOWER_BOUND, INT_UPPER_BOUND)
    
    nearest_left_x_idx = find_nearest(filtered_houses, reqArea, False)
    nearest_right_x_idx = find_nearest(filtered_houses, reqArea, True)
    
    nearest_left_point = filtered_houses[nearest_left_x_idx]
    nearest_right_point = filtered_houses[nearest_right_x_idx]
    
    answer = calculate(nearest_left_point, nearest_right_point, reqArea, area_meanPrice_map)
    return get_final_answer(answer, INT_LOWER_BOUND, INT_UPPER_BOUND)

reqArea = 1500
area = [1200, 1300, 1200, 1300, 1200, 2000]
price = [12000, 24000, 14000, 22000, 13000, 30000]

answer = findValuation(reqArea, area, price)
print(answer)

reqArea = 2500
area = [1200, 1200, 1200, 2000]
price = [15000, 11000, 17000, 25000]

answer = findValuation(reqArea, area, price)
print(answer)