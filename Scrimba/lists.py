friends = ["micheal", "John", "Terry" , 'Eric', "Graham"]
cars = [911,130,328,535,740,308]

# print(friends[0:4])
# print(len(friends))
# print(friends.index('Eric'))
# print(friends.count('Eric'))
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)

print(min(cars))
friends.append("Ali")
friends.insert(1,"Wangara")
friends[2] = "George" # removes Terry and adds george
friends.extend(cars)
print(friends)
friends.remove("Graham")
friends.pop() #removes the last item by default or you can specify the number you want to pop by doing friends.pop(1) - removes the item in index 1
# friends.clear() - clears the list
# del friends - deletes the entire friends list or you can specify the index you want to delete eg del friends[3] - removes item in index 3
cars[1] = "Mercedes"
print(cars)

#  to copy a list we do:
new_friends = friends[:] # or:
my_friends = friends.copy() #or:
our_friends = list(friends)
print(new_friends)
print(my_friends)
print(our_friends)

# Exercise


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
day = int(input("Enter a day: "))
sales_w2.append(day)

sales = []
sales.extend(sales_w1)
sales.extend(sales_w2)
best_day = max(sales) *1.5
worst_day = min(sales) *1.5
total = worst_day + best_day

print(f"On your worst day you sold $ {worst_day} which differs from your best day which you sold $ {best_day} and the total sales over the two weeks were {total}")


