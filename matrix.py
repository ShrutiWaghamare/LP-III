# take matrix input from user

Row = int(input("Enter the number of rows: "))
Column = int(input("Enter the number of columns: "))

matrix = []
a = []
print("Entries row wise: ")
for row in range(Row):
    # a = []
    a.clear()
    for column in range(Column):
        b = int(input())
        a.append(b)
    matrix.append(a)

for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end = " ")
    print() 
print(matrix[1][1])