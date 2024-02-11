def spiralOrder(matrix):
    result = []

    left = 0
    right = len(matrix[0])
    up = 0
    down = len(matrix)

    while left < right and up < down:

        for i in range(left,right):
            result.append(matrix[up][i])
        up += 1

        for i in range(up,down):
            result.append(matrix[i][right-1])
        right -= 1

        if not (left < right and up < down):
            break

        for i in range(right-1,left-1,-1):
            result.append(matrix[down-1][i])
        down -= 1

        for i in range(down-1,up-1,-1):
            result.append(matrix[i][left])
        left += 1

    return result
