
no_students =int(input("Enter no of students: "))

student_info = {}
for i  in range(1,no_students+1):
    name = input("Enter students Name: ").capitalize()
    marks = float(input("Enter students Marks: "))
    #           attach a key and a value
    student_info[name] = marks

    top_student = max(student_info, key=student_info.get)
    low_student = min(student_info, key=student_info.get)


    print(f"Top student: {top_student} ({student_info[top_student]})")
    print(f"Lowest student: {low_student} ({student_info[low_student]})")





