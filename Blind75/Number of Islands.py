
def numIslandsDFS(grid):
    if grid == []:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    def dfs(r,c, visited):
        if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited:
            return
        elif grid[r][c] == '1':
            visited.add((r,c))
        else:
            return
        dfs(r+1,c,visited)
        dfs(r,c+1,visited)
        dfs(r-1,c,visited)
        dfs(r,c-1,visited)

    for row in range(rows):
        for col in range(cols):
            if (row,col) not in visited and grid[row][col] == '1':
                islands += 1
                dfs(row,col,visited)
    return islands


def numIslandsBFS(grid):
    if grid == []:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    def bfs(r,c, visited):
        q = [(r,c)]
        while q:
            r,c = q.pop(0)
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited:
                continue
            elif grid[r][c] == '1':
                visited.add((r,c))
            else:
                continue
            q.append((r+1,c))
            q.append((r,c+1))
            q.append((r-1,c))
            q.append((r,c-1))
    for row in range(rows):
        for col in range(cols):
            if (row,col) not in visited and grid[row][col] == '1':
                islands += 1
                bfs(row,col,visited)
    return islands