class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.empty_cells = []

        # 1. Populate constraints and find empty cells
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != '.':
                    num = self.board[r][c]
                    box_idx = (r // 3) * 3 + c // 3
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.boxes[box_idx].add(num)
                else:
                    self.empty_cells.append((r, c))
        
        # Sort empty cells based on the number of possible valid numbers (MRV heuristic)
        self.empty_cells.sort(key=self.get_valid_count)

        # 2. Start backtracking
        self.backtrack(0)

    def get_valid_count(self, cell):
        r, c = cell
        box_idx = (r // 3) * 3 + c // 3
        count = 0
        for num in "123456789":
            if num not in self.rows[r] and num not in self.cols[c] and num not in self.boxes[box_idx]:
                count += 1
        return count

    def backtrack(self, k: int) -> bool:
        # Base case
        if k == len(self.empty_cells):
            return True

        row, col = self.empty_cells[k]
        box_idx = (row // 3) * 3 + col // 3

        # 3. Try to place a valid number
        for num in "123456789":
            if num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box_idx]:
                self.board[row][col] = num
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.boxes[box_idx].add(num)

                if self.backtrack(k + 1):
                    return True

                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.boxes[box_idx].remove(num)
                self.board[row][col] = '.'

        return False