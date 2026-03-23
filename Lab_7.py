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
        [5,10,15,20,25],
        [30,35,40,45,50]
    ]

    print_matrix(matrix,"Original Matrix: ")

    print("Dimensions:")
    print("Rows =", len(matrix))
    print("Columns =", len(matrix[0]))

    last_column = [row[-1] for row in matrix]
    print("Last column:", last_column)

    first_4_cols = [row[:4] for row in matrix]
    print("All rows, first 4 columns:")
    for row in first_4_cols:
        print(row)

    chosen_row = d1 % len(matrix)
    old_row = matrix[chosen_row][:]
    new_row = [value + k for value in old_row]
    matrix[chosen_row] = new_row

    start_col = d2 % 2
    sliced_subarray = [row[start_col:] for row in matrix]

    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    print_matrix(matrix, "Matrix after row replacement:")

    print("Sliced sub-array from starting column", start_col)
    for row in sliced_subarray:
        print(row)


if __name__ == "__main__":
    main()