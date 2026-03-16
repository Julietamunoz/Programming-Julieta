# Lecture 7: Lab 5 â€” Sensor List Builder and Calibrator
# I am using the dummy student ID you specified earlier:
#Student ID = 2672601
#d1 = 1
#d2 = 0
#k = (1 + 0) % 4 + 2 = 3
#shift = 1 - 0 = 1
#rows_keep = (1 % 2) + 2 = 3
#So all personalized outputs below use:
#k = 3
#shift = 1
#rows_keep = 3
#

def main():
    d1 = 1
    d2 = 0
    k = 3
    shift = 1
    rows_keep = 3

    numbers = []
    b = int(input("How many items do you want to enter? "))

    for i in range(b):
        val = int(input(f"Enter item {i +1}: "))
        numbers.append(val)


    print("Original readings:", numbers)

    if len(numbers) > 0:
        print("First reading:", numbers[0])
        print("Last reading:", numbers[-1])
    else:
        print("The list is empty.")

    if len(numbers) >= 4:
        print("Slice from index 1 to index 3:", numbers[1:4])
    else:
        print("Not enough values for slice [1:4].")

    total = sum(numbers)
    print("Sum of readings:", total)

    shifted = [x + shift for x in numbers]
    scaled = [x * k for x in numbers]
    zipped_sum = [a + b for a, b in zip(numbers, shifted)]

    print("Shifted readings:", shifted)
    print("Scaled readings:", scaled)
    print("Element-wise sum of original and shifted:", zipped_sum)

    print("\nManual check for first 3 elements:")
    for i in range(3):
        print(f"Original={numbers[i]}, Shifted={shifted[i]}, Scaled={scaled[i]}, ZipSum={zipped_sum[i]}")

if __name__ == "__main__":
    main()