nums = [1,2,3,4]
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

combo = list(zip(nums,letters,names))

print(combo) # prints [(1, 'a', 'John'), (2, 'b', 'Eric'), (3, 'c', 'Michael'), (4, 'd', 'Graham')]
# you can as well use a set or a tuple

# to unzip we use

nu,lett,nam = zip(*combo)
# nu,lett,nam - this is called unpacking meaning using the three names you have zipped to create a variable for unzipping

print(nu,lett,nam)

# do the same with dictionary

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

keys= keys.split()
values = values.split()

en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)

# or we can use a dictionary comprehension to do this

new_dict = {key:value for key,value in zip(keys,values)}

print(new_dict)

en,sv = list(en_sv_dict.keys()), list(en_sv_dict.values())

print(en,sv)

en1,sv1 = zip(*en_sv_dict.items())

print(en1,sv1)





