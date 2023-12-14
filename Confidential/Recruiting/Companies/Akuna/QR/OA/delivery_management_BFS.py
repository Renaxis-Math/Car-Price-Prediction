import heapq
from collections import deque

def order(cityNodes, cityFrom, cityTo, company):
    answers = []
    
    def build_cityNeighbors_map():
        answer = {}
        
        for city_num in range(1, cityNodes + 1):
            answer[city_num] = []
            heapq.heapify(answer[city_num])
            
        for i, city in enumerate(cityFrom):
            city, city_neighbor = cityFrom[i], cityTo[i]
            heapq.heappush(answer[city], city_neighbor)
            heapq.heappush(answer[city_neighbor], city)
        
        return answer
    
    cityNeighbors_map = build_cityNeighbors_map()  
    
    def solve(start_city):
        seenCity_set = set([start_city])
        city_queue = deque([start_city])
        
        while city_queue:
            cur_length = len(city_queue)
            for _ in range(cur_length):
                cur_city = city_queue.popleft()
                
                if cur_city != start_city:
                    answers.append(cur_city)
                
                city_neighbors_heap = cityNeighbors_map[cur_city]
                while len(city_neighbors_heap) > 0:
                    city_neighbor = heapq.heappop(city_neighbors_heap)
                    if city_neighbor not in seenCity_set:
                        seenCity_set.add(city_neighbor)
                        city_queue.append(city_neighbor)

        return
    
    solve(start_city=company)
    return answers

cityNodes = 5
cityFrom = [1, 1, 2, 3, 1]
cityTo = [2, 3, 4, 5, 5]
company = 1
print(order(cityNodes, cityFrom, cityTo, company))

cityNodes = 3
cityFrom = [1]
cityTo = [2]
company = 2
print(order(cityNodes, cityFrom, cityTo, company))

cityNodes = 4
cityFrom = [1, 2, 2]
cityTo = [2, 3, 4]
company = 1
print(order(cityNodes, cityFrom, cityTo, company))