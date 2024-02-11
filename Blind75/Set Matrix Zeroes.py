def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transformed = []

    def row_transformer(x_pos, lim):
        y_pos = 0
        while y_pos < lim:
            if matrix[x_pos][y_pos] != 0:
                transformed.append((x_pos,y_pos))

            matrix[x_pos][y_pos] = 0
            
            y_pos += 1

    def col_transformer(y_pos, lim):
        x_pos = 0
        while x_pos < lim:
            if matrix[x_pos][y_pos] != 0:
                transformed.append((x_pos,y_pos))
            matrix[x_pos][y_pos] = 0
            x_pos += 1
            
    for row in range(rows):
        for col in range(cols):
            if (row,col) in transformed:
                continue
            elif matrix[row][col] == 0:
                row_transformer(row, cols)
                col_transformer(col, rows)
