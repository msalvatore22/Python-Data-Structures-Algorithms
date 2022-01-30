myList = [33, 12, 7, 19, 45, 2, 14, 17, 17]
myList2 = [14, 2, 45, 33, 12, 7, 19, 17, 17]

def permutation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False

# print(permutation(myList, myList2))

def permutation2(arr1, arr2):
    d = {}
    if len(arr1) != len(arr2):
        return False
    for item in arr1:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    for item in arr2:
        if item in d:
            d[item] += 1
        else:
            return False
    
    for v in d.values():
        if v % 2 != 0:            
            return False
    return True
    
    

print(permutation2(myList, myList2))

    