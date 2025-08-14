my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'




print(my_list,'original')
print(my_list.sort()) # this gives the original list although:
print(my_list) # now this gives the sorted list version
print(list(reversed(my_list))) # reverses the list
# print(my_list.reverse())
print(sorted(my_list)) # this sorts immediately and return the answer on print you dont have to cvall the variable again

# if we sort a tuple we get a list eg:

print(sorted(my_tuple)) # = ['a', 'b', 'c', 'd', 'e']

# sorting a sting converts it into a list eg:
print(sorted(my_string)) # = ['h', 'n', 'o', 'p', 't', 'y']

# sorting a dictionary results in it loosing some information eg:
print(sorted(my_dict)) # = ['add', 'bee', 'car', 'dog'] from {'car':4,'dog':2,'add':3,'bee':1} meaning we only get the key
print(sorted(my_dict.items())) # returns tuples inside a list eg [('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]


my_new_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_new_list)) # sorts them in this order [-3, -2, 1, 5, 7]
print(sorted(my_new_list, key=abs)) # arranges it this way [1, -2, -3, 5, 7] checks the number not the sign before.

print(sorted(my_llist)) # prints this list [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]
print(sorted(my_llist, key = lambda item: item[1])) # sorts the second elements in the inner list eg: 1,2,3,4


