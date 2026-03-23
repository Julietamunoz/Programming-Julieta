#Student ID = 6316774
#d1 = 4
#d2 = 7
#k = (4 + 7) % 4 + 2 = 5
#shift = 7-4 = 3
#rows_keep = (4 % 2) + 2 = 4

def print_matrix(matrix,title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    d1 = 4
    d2 = 7
    k = 5
    shift = 3
    rows_keep = 4

    matrix = [
        [22,23,24,25],
        [26,27,28,29],
        [30,31,33,34]
    ]

    print_matrix(matrix,"Original Matrix: ")

    print_matrix(matrix, "Original matrix:")

    print("Specific element matrix[1][2]:", matrix[1][2])
    print("First two rows:", matrix[:2])

    first_column = [row[0] for row in matrix]
    print("First column:", first_column)

    upper_left_2x2 = [row[:2] for row in matrix[:2]]
    print("Upper-left 2x2 sub-array:", upper_left_2x2)

    row_index = d1 % len(matrix)
    col_index = d2 % len(matrix[0])

    for j in range(len(matrix[row_index])):
        matrix[row_index][j] += shift

    for i in range(len(matrix)):
        matrix[i][col_index] *= k

    print_matrix(matrix, "Modified matrix:")

    sub_array = [row[:k] for row in matrix[:rows_keep]]
    print("Sub-array using first rows_keep rows and first k columns:")
    for row in sub_array:
        print(row)


if __name__ == "__main__":
    main()
