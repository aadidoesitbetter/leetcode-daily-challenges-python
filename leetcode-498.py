class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        from collections import defaultdict
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
        result = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])
        return result