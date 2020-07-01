# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.

a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())

if(a+b)%2==(a1+b1)%2:
    print("YES")
else:
    print("NO")