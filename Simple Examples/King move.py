# Chess king moves horizontally, vertically or diagonally to any adjacent cell.
# Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
a= int(input())
b= int(input())
a1= int(input())
b1= int(input())

if (a1==a-1 or a1==a+1 or a1==a) and (b1==b-1 or b1==b+1 or b1==b):
    print("YES")
else:
    print("NO")