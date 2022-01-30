def maxProductSubArray(nums: list[int]) -> int:
    totalMax = prevMax = prevMin = nums[0]
    for i,num in enumerate(nums[1:]):
        currentMin = min(num, prevMax*num, prevMin*num)
        currentMax = max(num, prevMax*num, prevMin*num)
        totalMax = max(currentMax, totalMax)
        prevMax = currentMax
        prevMin = currentMin
    return totalMax

l = [-3,-1,-1,5,6,3,2]
print(maxProductSubArray(nums=l))
