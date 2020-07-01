# Chess rook moves horizontally or vertically. Given two different cells of the chessboard,
# determine whether a rook can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

if x==x1 or y==y1:
    print("YES")
else:
    print("NO")