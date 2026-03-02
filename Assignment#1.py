#Question 1
#Task 1: 
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
if __name__ == "__main__":
    number = float(input("Enter a number: "))
    print(check_number(number))

#Task 2: Explanation
# This function uses conditional statement (if statement) to check whether a number is positive or negative. 
# Input:The only imput parameter is {number}
# Output: The function will output a string:
# "Positive" if number>0
# "Negative" if number<0
# "Zero" if number is 0

#Task 3: New feature of asking the user if they want to continue
def modcheck_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    while True:
        number = float(input("Enter a number: "))
        print(modcheck_number(number))

        choice = input("Do you want to continue? (yes or no): ")

        if choice == "no":
            print("Program ended.")
            break

#Question 2:
#Task1
def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()  # Remove trailing newline at the end

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print(star_shape(rows))

#Task 2: Explanation
# This function uses for loop to create a star shape with given number of rows
# Input:The only imput parameter is {rows} which is the number of rows
# Output: The function will output joining strings of stars in a triangle shape

#Task 3: New feature of checking that the user enters a positive number, without any extra things
def modstar_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()  # Remove trailing newline at the end

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print(modstar_shape(rows))
    if rows > 0:
      print(modstar_shape(rows))
    else:
      print("Error: Enter a positive number!")

#Question 3:
#Task1
def count_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()  # Remove trailing newline at the end

if __name__ == "__main__":
    limit = int(input("Enter a positive number: "))
    print(count_multiples_of_3(limit))

#Task 2: Explanation
# This function uses While Loop to count multiples of 3
# Input:The only imput parameter is {limit} which is the maximum number to count to (user provides this).
# Output: The function will output a string containing numbers from 1 to limit.
# Main variables: {num} is to keeps track of the current number in the loop and {result} is to store output string

#Task 3: New feature to make sure the user enters a positive number
def modcount_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()


# Main program block with simple validation
if __name__ == "__main__":
    limit = int(input("Enter a positive number: "))
    
    # Validation: check if limit is positive
    if limit > 0:
        print(modcount_multiples_of_3(limit))
    else:
        print("Error: Enter a positive number!")

#Question4
#Task1
def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

#Task2:Explanation
# This function calculates the sum of even numbers in a range
# User input: {start} is the first number in the range and {end} is the last number in the range 
# Output: The function will output {total} which is the sum of all even numbers between start and end.
# Main variables: {total} is to accumulates the sum and {num} is to iterates through the range.

#Task3: Add new feature to ensure that start is less than or equal to end.
def modsum_of_even_numbers(start, end):
    # Same logic as before
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total


# Main program block with simple validation
if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    # Validation: start should not be greater than end
    if start <= end:
        print("Sum of even numbers:", modsum_of_even_numbers(start, end))
    else:
        print("Error: Starting number must be less than or equal to ending number!")

