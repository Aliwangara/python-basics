name = {
    "name": 'Ali',
    "age" : 21,
    "Location": "Nairobi"
}

movie = {
    "title" : "Life of Ali",
    'year' : 1979,
    'cast' : ["John", "Eric", "Michael", "George"]
}
movie["title"] = "Holy grail"
# to update we use movie.update
movie.update({"title":"My_movie",'year':1975,'cast':['John','Eric','Michael','George','Terry']})

# del movie['year']
# movie.pop('cast')
print(movie.get('title'))
movie.items() # gives a tuple as an answer  ('title', 'My_movie') ('year', 1975) ('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])



for key, value in movie.items() :
    print(key,value)

# Dictionaries 2:

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# membershp test:

print("Arthur" in holy_grail)

#concatenating dictionaries

people = {}
people1 = {}
people2 = {}
# people.update(python)
# people.update(holy_grail)
# print(people)

# method2: comprehension
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print("sum", sum(people1.values()))
