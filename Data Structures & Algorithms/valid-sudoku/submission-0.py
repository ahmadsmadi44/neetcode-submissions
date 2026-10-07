class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # make rows
        # make columns

        # go row by row, check number, if it is already in list, ouput false, else add to list
        # same thing w columns
        # for 3x3 boxes u do  r // 3, c // 3

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in boxes[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True
                    
