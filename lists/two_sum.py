# Write a program to find all pairs of integers in array whose sum is equal to a given number

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

myList = [1,2,2,3,4,5,6]
findPairs(myList, 6)

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in d:
            print([d[diff], i])
        else:
            d[nums[i]] = i

print(twoSum(myList, 6))

