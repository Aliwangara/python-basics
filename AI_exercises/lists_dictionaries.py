
no_of_students = int(input("Enter number of students: "))

student_info = []

for i in range(1, no_of_students + 1):
    name = input("Enter name: ").capitalize()
    marks = int(input("Enter marks: "))
    user = {"name": name, "marks": marks}
    student_info.append(user)

highest_num = max(student_info, key=lambda x: x["marks"])
lowest_num = min(student_info, key=lambda x: x["marks"])