#1. Lists - Removing Duplicates and Sorting
def remove_duplicates_sorting(numbers):
    return sorted(list(set(numbers)))
# This function takes a list of numbers, removes duplicates using a set(), and then sorts the result using sorted(). It first converts the user input into integers using map(int, input().split()), then returns a sorted list with no repeated values.
# I used "sorted()", "set()" and map() which are built-in funtions. 



#2. Single-Dimensional Arrays - Cumulative Sum
def cumulative_sum(arr):
    result = []                     # new list to store answers
    total = 0                       # running total

    for num in arr:
        total += num                # add number to total
        result.append(total)        # store result  

    return result
#This function takes a list of numbers and builds a new list where each element is the running total. I used a loop to add each number to a total variable, and I used append() to store each intermediate sum in the result list, which is then returned.



#3. Slicing - Extract Every Nth Element
def extract_element(array, nth):
    return array[::nth] # returns every Nth element from the list
#3 This function asks the user for a list of numbers and a step value. It converts the input into integers by using map. I used input(), map(), and function calling with parameters, to return the result of slicing the list with a step.
# THe [:: nth] is used in python slicing and means [start:stop:step] wich means it starts at the beginning until the end and step by nth.



#4. Aritmetic Operations with Arrays - Dot Product
def dot_product(list1, list2):
    return sum(a*b for a, b in zip(list1, list2))  
# zip(list1, list2) pairs elements from both lists
# a * b multiplies each pair
# sum(...) adds all the products → dot product
#This function uses input() and map(int, …) to convert two lists into integers, then I used zip() to pair elements from both lists and a generator expression with sum() to multiply corresponding elements and add them together to compute the dot product.



#5 Arithmetic Operations with Arrays - Matrix Multiplication
def matrix_multiplication(A, B):
    result = []
    # loop through rows of A
    for i in range(len(A)):
        row = []

        # loop through columns of B
        for j in range(len(B[0])):
            total = 0

            # multiply row * column
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)

        result.append(row)

    return result
#This function multiplies two matrices by iterating through rows of the first matrix and columns of the second, multiplying corresponding elements, summing them, and storing the results in a new matrix.

if __name__=="__main__":
    numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
    arr = list(map(int, input("Enter your numbers for cumulative sum: ").split()))
    array = list(map(int, input("Enter your list for every Nth element: ").split()))
    nth = int(input("Enter your step value: "))
    list1 = list(map(int, input("Enter first list for dot product: ").split()))
    list2 = list(map(int, input("Enter second list for dot product: ").split()))

    print(remove_duplicates_sorting(numbers))
    print(cumulative_sum(arr))
    print(extract_element(array,nth))
    print(dot_product(list1,list2))
    print("Enter matrix A row-wise (space seperated):")
    A = [list(map(int, input().split())) for _ in range(2)]
    print("Enter matrix B row-wise (space seperated):")
    B = [list(map(int, input().split())) for _ in range(2)]
    print(matrix_multiplication(A,B))
    