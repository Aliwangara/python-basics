for number in range(3):
    print("Attempt", number+1, (number + 1) * ".")
    # it prints
    # Attempt 1 .
    # Attempt 2 ..
    # Attempt 3 ...

#  or we can use:
for numbers in range(1,11, 2):
    print("Attempt", numbers, numbers* ".")