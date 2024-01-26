def solution(heights):
    rows, cols = len(heights), len(heights[0])

    pac, atl = set(), set()
    def dfs(r,c, visited, prevHeight):
        if(r < 0 or c < 0 or (r,c) in visited or r >= rows or c >= cols or heights[r][c] < prevHeight):
            return
        visited.add((r,c))
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])
    for col in range(cols):
        dfs(0, col, pac, heights[0][col])
        dfs(rows-1, col, atl, heights[rows-1][col])
        
    for row in range(rows):
        dfs(row, 0, pac, heights[row][0])
        dfs(row, cols-1, atl, heights[row][cols-1])
    res = []
    for (r,c) in pac:
        if (r,c) in atl:
            res.append((r,c))
    return res
