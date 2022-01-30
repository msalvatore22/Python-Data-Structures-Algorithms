def max3(nums: list[int]) -> int:
    max1=max2=max3= float("-inf")
    min1=min2= float("inf")
    for num in nums:
        # num is greater than max1,max2,max3
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        # num is between max1 and max2
        elif num > max2:
            max3 = max2
            max2 = num  
        # num is between max2 and max3 
        elif num > max3:
            max3 = num              
        
        if num < min1:
            min2 = min1
            min1 = num
        # num is between min1 and min2
        elif num < min2:
            min2 = num
    
    return max(max1* max2* max3, min1*min2*max1)

print(max3([1,2,3,4]))