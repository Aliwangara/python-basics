# Nested_loop = A loop within another loop(outer,inner)

            # outer_loop:
            #     inner_loop

row =int(input("Enter row number: "))
columns = int(input("Enter column number: "))
symbol = input("Enter symbol: ")

for y in range(row):
    for x in range(columns):
        print(symbol, end="")
    print()# This prints 1-9 2times  in two different lines


