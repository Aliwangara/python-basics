age = 22

message = "Eligible" if age>= 18 else "Not Eligible"
print(message)

# That message is same as

if age >=18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)