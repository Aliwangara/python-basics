# exercise  on splitting and joining

messy_friends = "Ali,John;Wangara:Eric,,Michael:Anna"

messy_friends = ''.join(messy_friends).replace(';',',').replace(':',',').replace(',,',',').split(',')

print(f"Choose a name to reverse from this list: {messy_friends}")

name = input("Enter a name from the list to reverse: ")

new_name = name[::-1]

if name not in messy_friends:
    print("Name is not in the list")
elif name in messy_friends:
    print(f"{name} wrote backwards is {new_name}")



