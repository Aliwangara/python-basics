
data = "Ali,John;Wangara:Eric,,Michael:Anna;Eric;Sarah:Ali"

replaced_data = data.replace(":", ",").replace(";",",").replace(",,", ",")

split_data = replaced_data.strip().split(',')

split_data = set(split_data)

my_friends = {"Reg", "Loretta", "Colin", "Eric", "Graham"}

new_friends = split_data.union(my_friends)

# new_friends = split_data.difference(my_friends)

# new_friends = split_data.intersection(my_friends)
# new_friends = split_data.symmetric_difference(my_friends)
print(new_friends)

# friend_input = input("Pick a friends name From the list:  ").capitalize()

# while True:
#     if friend_input in new_friends:
#        reversed_friend =  friend_input[::-1]
#        print(reversed_friend)
#        break
#     else:
#         print(f"{friend_input} isn't in the list please enter either of these names {new_friends}")
#         break














