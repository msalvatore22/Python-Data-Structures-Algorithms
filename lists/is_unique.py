myList = [33, 12, 7, 19, 45, 2, 4, 14]

def isUnique(a):
    if len(set(a)) == len(a):
        return True
    else:
        return False

print(isUnique(myList))

def is_unique(data: list) -> bool:
    values = {}
 
    for i in range(len(data)):
        if values.get(data[i], -1) == -1:
            values[data[i]] = 1
        elif values.get(data[i], -1) == 1:
            return False
    return True
