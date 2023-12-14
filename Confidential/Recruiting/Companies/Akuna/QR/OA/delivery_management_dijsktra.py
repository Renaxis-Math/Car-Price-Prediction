import heapq

def order(city_nodes, city_from, city_to, company):
    graph = [[] for _ in range(city_nodes)]
    
    for i in range(len(city_from)):
        
        graph[city_from[i] - 1].append((1, city_to[i] - 1))
        
        graph[city_to[i] - 1].append((1, city_from[i] - 1))
        
        heap = [(0, company - 1)]
        
        distance = [city_nodes + 1 for _ in range(city_nodes)]
        
        distance[company - 1] = 0
        
        city_order = []
        while heap:
            cur = heapq.heappop(heap)
            
            if cur[1] + 1 != company:
                
                city_order.append(cur[1] + 1)
                
            for vertex in graph[cur[1]]:
                
                if distance[cur[1]] + vertex[0] < distance[vertex[1]]:
                    
                    distance[vertex[1]] = distance[cur[1]] + vertex[0]
                    
                    heapq.heappush(heap, (distance[vertex[1]], vertex[1]))
                    
    return city_order

city_nodes = 5
city_from = [1, 2, 2]
city_to = [2, 3, 4]
company = 1
print(order(city_nodes, city_from, city_to, company))

city_nodes = 5
city_from = [1,1,2,3,1]
city_to = [2,3,4,5,5]
company = 1
print(order(city_nodes, city_from, city_to, company))

city_nodes = 3
city_from = [1]
city_to = [2]
company = 2
print(order(city_nodes, city_from, city_to, company))