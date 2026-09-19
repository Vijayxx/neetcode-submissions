class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = True
        col = True
        box = True

        r = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                            continue

                if board[i][j] in r:
                    row = False

                r.add(board[i][j])
            r.clear()

        r.clear()

        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in r:
                    col = False

                r.add(board[j][i])
            r.clear()

        r.clear()

        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == ".":
                            continue

                        if board[k][l] in r:
                            box = False
                        
                        r.add(board[k][l])
                r.clear()
                        
        if row and col and box:
            return True
        else: return False
            