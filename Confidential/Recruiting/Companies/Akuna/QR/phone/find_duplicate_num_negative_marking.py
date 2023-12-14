def findDuplicate(nums) -> int:
    for num in nums:
        abs_num = abs(num)
        
        if nums[abs_num] < 0: # found duplicate
            duplicate = abs_num
            break

        nums[abs_num] = -nums[abs_num]

    # Restore numbers
    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return duplicate