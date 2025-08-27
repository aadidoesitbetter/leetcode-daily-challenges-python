class Solution:
    def lenOfVDiagonal(self, grid):
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])
        memo = {} 

        def dfs(cx, cy, direction, turn, target):
            key = (cx, cy, direction, turn, target)
            if key in memo:
                return memo[key]

            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                memo[key] = 0
                return 0

            max_step = dfs(nx, ny, direction, turn, 2 - target)

            if turn:
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target)
                )

            memo[key] = max_step + 1
            return memo[key]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        return res