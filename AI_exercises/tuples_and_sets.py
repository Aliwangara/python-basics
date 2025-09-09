u_number = input("Enter couple of numbers leave spaces between them: ")

number_tuple = tuple(map(int, u_number.split()))

number_set = set(number_tuple)

print(number_set)

print("Tuple:", number_tuple)
print("Set:", number_set)
print("Length of tuple:", len(number_tuple))
print("Length of set:", len(number_set))

print(help(map))