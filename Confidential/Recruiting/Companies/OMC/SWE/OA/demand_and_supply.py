def solve(customers, shops):
    n = len(customers)
    p = len(customers[0])
    
    answer = 0

    for customer_i, customer_items in enumerate(customers):
        for shop_j, shop_items in enumerate(shops):
            seen_complements_set = set()
            finished_items_str, remaining_items_str = "", ""
            for customer_item in customer_items:
                if customer_item in shop_items:
                    finished_items_str += str(customer_item)
                else:
                    remaining_items_str += str(customer_item)
            
            if len(finished_items_str) == len(customer_items) or \
                finished_items_str in seen_complements_set:
                answer += 1
                break

            else:
                seen_complements_set.add(remaining_items_str)
                        
    return answer
  
# customers1 = [
#     [1,2], [1,5]
# ]

# shops1 = [
#     [1,2,3,4], [2,3,4,5], [1,2,4,5]
# ]

# test1 = solve(customers1, shops1)
# assert test1 == 2, print(test1)

# customers2 = [
#     [1,2,3], [1,4,2]
# ]

# shops2 = [
#     [1,2,3,4,5], [2,3,4,6,7]
# ]

# test2 = solve(customers2, shops2)
# assert test2 == 2, print(test2)

customers3 = [
    [1,2,3], [1,7,2]
]

shops3 = [
    [1,2,3,4,5], [2,3,4,6,1]
]

test3 = solve(customers3, shops3)
assert test3 == 1, print(test2)