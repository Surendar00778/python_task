# Input the number of rows and columns
m, n = map(int, input().split())

# Initialize an empty matrix
matrix = []

# Input the matrix elements
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate the sum of each row and find the row with the maximum sum
max_sum = -1
max_row = -1

for i in range(m):
    row_sum = sum(matrix[i])
    print(f"Row {i + 1} : {row_sum}")
    if row_sum > max_sum:
        max_sum = row_sum
        max_row = i + 1

print(f"Row {max_row} is having the maximum sum : {max_sum}")
