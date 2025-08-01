#conditional expression  = shortcut for the if-else statement (ternary Operator)
#                       print or assign one of the two values based on a condition
#                       x if condition else y

user_role = "Admin"
num = 0
# print("positive" if num > 0 else "negative")

result = "Even" if num %2 == 0 else "ODD"

age  = 19

status = "adult" if age>=18 else "Child"

role = "You are logged in as an admin" if user_role == "Admin" else 'Student'
print(role)

print(status)
