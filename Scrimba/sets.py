friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# faster than a list
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set)) # finds similar items in both sets eg: {'Eric', 'Graham'}
print(friends_set.difference(my_friends_set)) # finds different items in the set
print(friends_set.union(my_friends_set))# combines all sets
print(friends_set.symmetric_difference(my_friends_set)) # finds the items that are unique in each set



