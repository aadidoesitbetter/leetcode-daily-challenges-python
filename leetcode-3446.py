class Solution:
    def sortMatrix(self, grid):
        n = len(grid)

        for i in range(n):
            diagonal = []
            r, c = i, 0
            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1
            
            diagonal.sort(reverse=True)
            
            r, c = i, 0
            k = 0
            while r < n and c < n:
                grid[r][c] = diagonal[k]
                r += 1
                c += 1
                k += 1

        for j in range(1, n):
            diagonal = []
            r, c = 0, j
            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1

            diagonal.sort()

            r, c = 0, j
            k = 0
            while r < n and c < n:
                grid[r][c] = diagonal[k]
                r += 1
                c += 1
                k += 1
                
        return grid