
def findDuplicate(nums):
    """
    Proof: https://math.stackexchange.com/questions/913499/proof-of-floyd-cycle-chasing-tortoise-and-hare
    """
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare: break
    
    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare