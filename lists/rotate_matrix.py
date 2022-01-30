m = [[1,2,3], [4,5,6], [7,8,9]]

def rotate(m):
    n = len(m)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save left element
            top = m[layer][i]
            # move left element to top
            m[layer][i] = m[-i-1][layer]
            # move bottom element to left
            m[-i-1][layer] = m[-layer-1][-i-1]
            # move right to bottom
            m[-layer-1][-i-1] = m[i][-layer-1]
            # move top to right
            m[i][-layer] = top
    return m


def rotateMatrix(matrix):

    for j  in matrix:

        print(j)

    print("----------GETS ROTATED BY 90 DEGREES TO FORM THIS------------")

    for i in range(len(matrix)):

        for j in range(i + 1, len(matrix[i])):

            temp = matrix[i][j]

            matrix[i][j] = matrix[j][i]

            matrix[j][i] = temp

    for i in range(len(matrix)):

        matrix[i] = matrix[i][::-1]

    for j in matrix:

        print(j)

rotateMatrix(m)