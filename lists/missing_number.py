# How to find the missing number ibn an integer array of 1 to 20?
# sum of series

def findMissing(list, n):
    sum1 = 20*21/2
    sum2 = sum(list)
    return sum1-sum2

l = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]

print(findMissing(l, 20))
