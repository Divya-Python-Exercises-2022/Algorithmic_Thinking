matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5]
]

if __name__ == '__main__':
    print(matrix[1][2])

num_lines = len(matrix)
print(f"Number of lines in the matrix is {num_lines}")

num_columns = len(matrix[0])
print(f'Number of columns in the matrix is {num_columns}')


for line in range(num_lines):
    for column in range(num_columns):
        print(f'{matrix[line][column]} ', end='')
    print()
