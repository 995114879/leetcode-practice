from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检查行
        for row in board:
            unit = [i for i in row if i != '.']
            if not len(unit) == len(set(unit)):
                return False

        # 检查列
        for col in zip(*board):
            unit = [i for i in col if i != '.']
            if not len(unit) == len(set(unit)):
                return False

        # 检查 3x3 宫格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                unit = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                unit = [i for i in unit if i != '.']
                if not len(unit) == len(set(unit)):
                    return False

        return True


    
board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

res1 = Solution().isValidSudoku(board=board1)
print(res1)
board2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
res2 = Solution().isValidSudoku(board=board2)
print(res2)
row = [[0] * 9 for _ in range(9)]
print(row)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #先明白这个row,col,block二维矩阵代表什么意思
        #即对于每一行、一列、一块而言，在1-9这个索引处是否有值
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    #注意这个num其实是索引
                    num = int(board[i][j]) - 1
                    #这个b可以算下，其就是就代表里3*3的格子是哪个块
                    b = (i // 3) * 3 + j // 3
                    #最难理解的是这个地方，首先我们知道数独中的数字填的值是1-9
                    #对于每一行，即i=0-8行而言，对应的数字索引num处有2个以上的值
                    #即row[i][num]！=0，则出错，否则在这个索引处把0改为1，
                    #证明在此次遍历时这个索引处有值了
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True