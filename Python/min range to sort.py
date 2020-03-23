def findRange(nums):
    
    outOfOrder = []

    for i in range(0, len(nums)):
        if nums[i] < nums[i+1]:
            if outOfOrder:
                break
        else:
            outOfOrder.append(i)
    return outOfOrder

#findRange([1, 7, 9, 5, 7, 8, 10])
print(findRange([1, 2, 3, 7, 9, 5, 7, 8, 10]))
