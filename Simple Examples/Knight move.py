#Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically,
# or two cells vertically and one cells horizontally.
# Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.


a= int(input())
b= int(input())
a1= int(input())
b1= int(input())


if a!=a1 and abs(a-a1)+abs(b-b1)==1 or  a!=a1 and abs(a-a1)+abs(b-b1)==3:
    print("YES")
else:
    print("NO")

# Or

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

