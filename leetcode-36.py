import collections

class Solution(object):
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue

                box_key = (r // 3, c // 3)

                if num in rows[r]:
                    return False
                
                if num in cols[c]:
                    return False
                
                if num in boxes[box_key]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_key].add(num)

        return True