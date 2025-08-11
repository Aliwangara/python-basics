

# Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

if "John" in friends and "Eric" in friends:
    print("John and Eric exist")
else:
    print("John and Eric does not exist")


print(friends.intersection(my_friends)) # graham and john or we can use  print(friends & my_friends)
print(friends.union(my_friends)) # combines the two sets or we can use  print(friends | my_friends)
print(friends.difference(my_friends)) # find names that are only in friends or we can use friends - my_friends and gives
                                    # name that only exist in the first variable friends
print(my_friends.difference(friends)) # gives name that only exist in the second variable my_friends
print(friends.symmetric_difference(my_friends))# Show only the names who only appear in one of the lists. use ^ character

cars = set(cars) # turned it into a set because it doesn't contain duplicates

print(cars)




