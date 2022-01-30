def maxSubArray(nums: list[int]) -> int:
    maxSum = nums[0]
    currentSum = maxSum
    for num in nums[1:]:
        if currentSum > 0:
            currentSum += num
        else:
            currentSum = num
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

l = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums=l))
