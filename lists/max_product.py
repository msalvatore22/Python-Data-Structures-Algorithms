myList = [33, 12, 7, 19, 45, 2, 4, 14]

def findMaxProduct(a):
    maxProduct = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] * a[j] > maxProduct:
                maxProduct = a[i] * a[j]
                pairs = str(a[i]) + "," + str(a[j])
    print(pairs)
    print(maxProduct)

def findMaxProduct2(a):
    max1 = a[0]
    max2 = 0
    for i in a:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i < max1:
            max2 = i
    print(max1, max2)
    print(max1*max2)

findMaxProduct2(myList)